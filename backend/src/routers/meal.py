from fastapi import APIRouter, Depends, HTTPException
from google.cloud.firestore_v1.base_document import DocumentSnapshot
from google.cloud.firestore_v1.collection import CollectionReference
from google.cloud.firestore_v1.query import Query
from google.cloud.firestore_v1 import SERVER_TIMESTAMP

from src.schemas.meal import MealUploadResponse, NutrientList, Advice, MealInput, MealRecord, MealRecordList
from src.core.deps import get_current_uid, user_doc
from src.core.nutrition_advice_agent.step1_dish_detect import detect_dishes
from src.core.nutrition_advice_agent.step2_nutrition import get_nutrition
from src.core.nutrition_advice_agent.step3_advice import make_advice
from src.core.nutrition_advice_agent.step4_total import calculate_total_nutrition
from src.schemas.meal import BodyInfo

router = APIRouter()


@router.post("/upload", response_model=MealUploadResponse)
async def upload_meal(image_url: str, uid: str = Depends(get_current_uid)) -> MealUploadResponse:
    """料理の画像をアップロードし、栄養情報とアドバイスを取得する。

    Args:
        image_url (str): 料理の画像 URL または base64 エンコードされた画像データ。
        uid (str): ユーザーの一意の識別子。認証システムから取得される。

    Returns:
        MealUploadResponse: 料理の栄養情報とアドバイスを含むレスポンスモデル。

    Raises:
        HTTPException: ユーザーのプロフィールが見つからない場合や、料理の検出に失敗した場合、または栄養情報が取得できなかった場合に発生。

    """

    # プロフィール取得
    snap: DocumentSnapshot = await user_doc(uid).get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail="User profile not found")

    body = BodyInfo.model_validate(snap.to_dict() or {})

    dishes = detect_dishes(image_url)

    if not dishes:
        raise HTTPException(
            status_code=400, detail="No dishes detected in the image")

    nutrition = get_nutrition(image_url, dishes)

    if not nutrition:
        raise HTTPException(
            status_code=400, detail="No nutrition information found")

    nutrition_dicts = [n.model_dump() for n in nutrition]
    advice_str = make_advice(nutrition_dicts, body)

    nutrient_list_obj = NutrientList(nutrients=nutrition)
    advice_obj = Advice(advice=advice_str)

    total_nutrition = calculate_total_nutrition(nutrient_list_obj, advice_obj)

    meal_data = MealInput(
        imageUrl=image_url,
        menu_name=str(nutrition[0].dish),
        calorie=nutrition[0].calorie,
        protein=nutrition[0].protein,
        fat=nutrition[0].fat,
        carbohydrate=nutrition[0].carbohydrate,
        dietary_fiber=nutrition[0].dietary_fiber,
        vitamin=nutrition[0].vitamin,
        mineral=nutrition[0].mineral,
        sodium=nutrition[0].sodium,
        advice_message=advice_str,
    )

    await user_doc(uid).collection("meals").add(
        meal_data.model_dump(by_alias=True) | {"eatenAt": SERVER_TIMESTAMP}
    )

    return total_nutrition

@router.get("/list", response_model=MealRecordList)
async def list_meals_desc(uid: str = Depends(get_current_uid)) -> MealRecord:
    """料理の画像URL、栄養情報、アドバイスの一覧を降順で取得する。

    Args:
        uid (str): ユーザーの一意の識別子。認証システムから取得される。

    Returns:
        MealRecordList: 料理の画像URL、栄養情報、アドバイスのリストを表すモデル。

    Raises:
        HTTPException: ユーザーのプロフィールが見つからない場合や、料理の検出に失敗した場合、または栄養情報が取得できなかった場合に発生。

    """
    # プロフィール取得
    snap: DocumentSnapshot = await user_doc(uid).get()
    if not snap.exists:
        raise HTTPException(status_code=404, detail="User profile not found")

    # 食事記録を降順で取得
    meals_collection_ref: CollectionReference = user_doc(uid).collection("meals") # FIXME: user_doc(uid)を切り分けてawaitすべき?
    meals_collection_query: Query = meals_collection_ref.order_by("eatenAt", direction=Query.DESCENDING)
    meal_records = [meal_doc.to_dict()
                    async for meal_doc in meals_collection_query.stream()]

    return MealRecordList(meal_records=meal_records)
