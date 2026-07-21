import requests
import json

url = "http://localhost:8000/predict"

data = {
    "customer_id": 12345,
    "age": 35,
    "gender": "Female",
    "product_category": "Electronics",
    "product_price": 150.0,
    "quantity": 2,
    "discount_percent": 10,
    "discount_amount": 30.0,
    "total_amount": 300.0,
    "final_amount": 270.0,
    "payment_method": "Credit Card",
    "shipping_days": 5,
    "customer_rating": 4,
    "is_returned": False,
    "region": "North",
    "order_month": 11
}

json_str = json.dumps(data, indent=2)
print("Отправляемый JSON:")
print(json_str)

response = requests.post(
    url,
    data=json_str,
    headers={"Content-Type": "application/json"}
)

print(f"Статус: {response.status_code}")
print("Ответ:")
print(response.json())