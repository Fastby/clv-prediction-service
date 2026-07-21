import pickle
import pandas as pd
from pathlib import Path

# Пути к сохранённым файлам
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / 'models' / 'rf_clv_model.pkl'
PREPROCESSOR_PATH = BASE_DIR / 'models' / 'preprocessor_clv.pkl'

model = None
preprocessor = None

def load_model():
    """Загружает модель и препроцессор из .pkl файлов."""
    global model, preprocessor
    if model is None:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(PREPROCESSOR_PATH, 'rb') as f:
            preprocessor = pickle.load(f)
    return model, preprocessor

def predict(features: dict):
    """Принимает словарь с признаками, возвращает предсказание и вероятность."""
    model, preprocessor = load_model()
    
    # Преобразуем словарь в DataFrame
    df_input = pd.DataFrame([features])
    
    # Преобразуем через препроцессор
    X_processed = preprocessor.transform(df_input)
    
    # Предсказание класса и вероятности
    pred_class = model.predict(X_processed)[0]
    pred_proba = model.predict_proba(X_processed)[0][1]  # вероятность класса 1
    
    return int(pred_class), float(pred_proba)