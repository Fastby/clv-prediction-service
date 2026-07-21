from pydantic import BaseModel
from typing import Optional

class OrderFeatures(BaseModel):
    """Входные данные для предсказания."""
    customer_id: int
    age: int
    gender: str
    product_category: str
    product_price: float
    quantity: int
    discount_percent: float
    discount_amount: float
    total_amount: float
    final_amount: float
    payment_method: str
    shipping_days: int
    customer_rating: int
    is_returned: bool
    region: str
    order_month: int  

class PredictionResponse(BaseModel):
    """Ответ сервера."""
    prediction: int          
    probability: float      
    status: str
