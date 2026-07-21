from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import OrderFeatures, PredictionResponse
from model import predict, load_model
import uvicorn

app = FastAPI(
    title="CLV Prediction API",
    description="Предсказание высокого Customer Lifetime Value (CLV) по данным заказа.",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Загружаем модель при старте сервера."""
    load_model()
    print("Модель и препроцессор загружены")

@app.get("/")
async def root():
    return {"message": "CLV Prediction API is running. Use /docs for Swagger UI."}

@app.get("/health")
async def health_check():
    """Проверка работоспособности."""
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
async def predict_endpoint(features: OrderFeatures):
    """
    Принимает данные о заказе и возвращает предсказание:
    - prediction: 1 — клиент высокоценный (high CLV), 0 — нет
    - probability: вероятность принадлежности к классу 1
    """
    try:
        
        input_dict = features.dict()
        
        
        pred_class, pred_proba = predict(input_dict)
        
        return PredictionResponse(
            prediction=pred_class,
            probability=pred_proba,
            status="success"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
