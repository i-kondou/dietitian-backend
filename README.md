# Dietitian API

AI を活用した栄養管理アプリケーションのバックエンド API です。料理の画像から栄養情報を自動解析し、個人の身体情報に基づいたパーソナライズされた健康アドバイスを提供します。

## 📖 概要

Dietitian API は、Google の Gemini AI モデルと Firebase を活用した栄養管理サービスです。ユーザーが料理の写真をアップロードすると、AI が料理を自動認識し、栄養成分を推定して、個人の身体情報に基づいたカスタマイズされた健康アドバイスを生成します。

### 主な機能

- 🍽️ **料理画像認識**: AI による料理の自動検出と名前の特定
- 📊 **栄養成分分析**: カロリー、タンパク質、脂質、炭水化物などの詳細な栄養成分推定
- 👤 **ユーザープロフィール管理**: 身長、体重、年齢、性別に基づく個人情報管理
- 💡 **パーソナライズされたアドバイス**: 個人の身体情報と食事内容に基づいた健康アドバイス
- 📱 **Firebase 統合**: ユーザー認証とデータ永続化
- 🔐 **JWT 認証**: セキュアなユーザー認証システム

## 🏗️ アーキテクチャ

### 技術スタック

- **Backend Framework**: FastAPI
- **AI/ML**: Google Gemini 2.5 Flash (LangChain 経由)
- **Database**: Google Cloud Firestore
- **Authentication**: Firebase Auth
- **Image Processing**: Pillow
- **Python Version**: 3.12+

### プロジェクト構成

```
backend/
├── src/
│   ├── api.py                          # FastAPI メインアプリケーション
│   ├── core/
│   │   ├── deps.py                     # 依存性注入とユーザー認証
│   │   ├── firebase.py                 # Firebase 初期化設定
│   │   └── nutrition_advice_agent/     # AI 栄養アドバイスエージェント
│   │       ├── common.py               # 共通ユーティリティ
│   │       ├── step1_dish_detect.py    # ステップ1: 料理検出
│   │       ├── step2_nutrition.py      # ステップ2: 栄養成分分析
│   │       ├── step3_advice.py         # ステップ3: アドバイス生成
│   │       └── step4_total.py          # ステップ4: 栄養成分合計
│   ├── routers/
│   │   ├── meal.py                     # 食事関連エンドポイント
│   │   └── user.py                     # ユーザー関連エンドポイント
│   └── schemas/
│       ├── meal.py                     # 食事データモデル
│       └── user.py                     # ユーザーデータモデル
├── secrets/                            # Firebase 認証キー
├── Dockerfile                          # 本番用 Docker 設定
├── Dockerfile.dev                      # 開発用 Docker 設定
└── pyproject.toml                      # Python プロジェクト設定
```

## 🚀 セットアップ

### 前提条件

- Python 3.12+
- Docker & Docker Compose
- Google Cloud プロジェクト
- Firebase プロジェクト
- Google AI Studio API キー

### 環境変数

以下の環境変数を設定してください：

```bash
GOOGLE_API_KEY=your_google_api_key
FIREBASE_ADMINSDK_JSON=/secrets/firebase-adminsdk.json
```

### Firebase 設定

1. Firebase コンソールでプロジェクトを作成
2. Firestore データベースを有効化
3. Firebase Admin SDK の秘密鍵をダウンロード
4. `backend/secrets/firebase-adminsdk.json` に配置

### Docker を使用した起動

```bash
# リポジトリをクローン
git clone <repository-url>
cd dietitian

# Docker Compose で起動
docker-compose up --build
```

### ローカル開発環境

```bash
cd backend

# 依存関係をインストール
pip install -e .

# 開発サーバーを起動
uvicorn src.api:app --host 0.0.0.0 --port 8080 --reload
```

## 📚 API エンドポイント

### ユーザー管理

#### `POST /user/create`
新規ユーザーを作成または既存ユーザーのプロフィールを取得

```json
{
  "uid": "user123",
  "name": "",
  "height": 0.0,
  "weight": 0.0,
  "sex": "male",
  "age": 0
}
```

#### `POST /user/update`
ユーザープロフィールを更新

```json
{
  "name": "田中太郎",
  "height": 170.5,
  "weight": 65.0,
  "sex": "男性",
  "age": 30
}
```

#### `GET /user/read`
ユーザープロフィールを取得

### 食事管理

#### `POST /meal/upload`
料理画像をアップロードして栄養分析とアドバイスを取得

**リクエスト:**
```json
{
  "image_url": "https://example.com/food-image.jpg"
}
```

**レスポンス:**
```json
{
  "menu_name": "唐揚げ, サラダ, ご飯",
  "calorie": 650.5,
  "protein": 25.2,
  "fat": 18.7,
  "carbohydrate": 85.3,
  "dietary_fiber": 4.2,
  "vitamin": 0.8,
  "mineral": 1.5,
  "sodium": 2.1,
  "advice_message": "バランスの取れた食事ですが、塩分が少し多めです。野菜を多めに摂取し、水分補給を心がけてください。"
}
```

## 🤖 AI 栄養アドバイスの仕組み

Dietitian API の AI システムは、4つのステップで動作します：

### Step 1: 料理検出 (`step1_dish_detect.py`)
- Gemini Vision API を使用して画像から料理を自動認識
- 重複を除いた料理名リストを生成

### Step 2: 栄養成分分析 (`step2_nutrition.py`)
- 検出された料理と画像から栄養成分を推定
- カロリー、三大栄養素、ビタミン、ミネラル等を算出

### Step 3: アドバイス生成 (`step3_advice.py`)
- ユーザーの個人情報（身長、体重、年齢、性別）を考慮
- 栄養成分データと組み合わせてパーソナライズされたアドバイスを生成

### Step 4: 総栄養計算 (`step4_total.py`)
- 複数の料理の栄養成分を合計
- 最終的なレスポンスデータを構築

## 🗃️ データベース構造

### Users Collection
```
users/{uid}
├── name: string
├── height: number
├── weight: number
├── sex: string
├── age: number
├── createdAt: timestamp
├── updatedAt: timestamp
└── meals/{mealId}
    ├── imageUrl: string
    ├── menu_name: string
    ├── calorie: number
    ├── protein: number
    ├── fat: number
    ├── carbohydrate: number
    ├── dietary_fiber: number
    ├── vitamin: number
    ├── mineral: number
    ├── sodium: number
    ├── advice_message: string
    └── eatenAt: timestamp
```

## 🔐 認証

Firebase Authentication を使用した JWT ベースの認証システムを実装しています。

```python
# Authorization ヘッダーに Bearer トークンを付与
headers = {
    "Authorization": "Bearer <firebase-id-token>"
}
```

