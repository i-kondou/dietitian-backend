from src.schemas.meal import MealUploadResponse, NutrientList, Advice


def calculate_total_nutrition(dishes: NutrientList, meal_advice: Advice) -> MealUploadResponse:
    """全ての料理の栄養素を合計し、アドバイスを付与する。

    Args:
        dishes (NutrientList): 各料理の栄養素リスト
        meal_advice (Advice): 料理に対するアドバイス

    Returns:
        MealUploadResponse: 合計栄養素とアドバイスを含むレスポンス

    """

    menu_name = ", ".join(str(dish.dish) for dish in dishes.nutrients)

    meal_response = MealUploadResponse(
        menu_name=menu_name,
        calorie=0.0,
        protein=0.0,
        fat=0.0,
        carbohydrate=0.0,
        dietary_fiber=0.0,
        vitamin=0.0,
        mineral=0.0,
        sodium=0.0,
        advice_message=meal_advice.advice
    )

    for dish in dishes.nutrients:
        meal_response.calorie += dish.calorie
        meal_response.protein += dish.protein
        meal_response.fat += dish.fat
        meal_response.carbohydrate += dish.carbohydrate
        meal_response.dietary_fiber += dish.dietary_fiber
        meal_response.vitamin += dish.vitamin
        meal_response.mineral += dish.mineral
        meal_response.sodium += dish.sodium

    return meal_response
