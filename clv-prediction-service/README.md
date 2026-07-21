# E-Commerce Sales Data Pipeline & Analysis

## Обзор проекта
Анализ 10 000+ транзакций интернет-магазина. Полный пайплайн: загрузка → очистка → feature engineering → EDA → визуализация → бизнес-инсайты.

## Технологический стек
- Python 3.10.11
- Pandas, NumPy - работа с данными
- Matplotlib, Seaborn - визуализация
- Scikit-learn - ML
- Jupyter notebook


## Ключевые бизнес - инсайты
1. **Сезонность:** Пик продаж - октябрь, спады - февраль, июнь, сентябрь.
2. **Топ-категория:** "Спорт" приносит 17,6 % общей выручки.
3. **Регионы:** Западный регион - ключевой рынок (25,8% общей выручки).

## ML: Предсказание ценности клиента
**Задача** Бинарная классификация - определить, "ценный" ли клиент (CLV выше медианы)

**Модели**
- Logistic Regression - ROC-AUC: 0.63, Точность: 0.60
- Random Forest - ROC-AUC: 0.62, Точность: 0.59

**Ключевые признаки (RF)**
1. **'final_amount'** - итоговая сумма заказа
2. **'total_amount'** - сумма до скидки
3. **'product_price'** - цена товара

**Запуск**
   Запустите notebooks\analysis.ipynb

---
# CLV-prediction-service

**End-to-end ML-сервис для анализа клиентских данных и предсказания поведения покупателей.**

## Технологический стек
- Python 3.10.11
- FastAPI, Unicorn, Pydantic - API
- Docker - Контейнеризация
- Scikit-learn - ML

## Запуск
**Перед запуском сервера необходимо создать модели LR и RF, для этого запустите notebooks\analysis.ipynb**
### Вариант 1. Локальный запуск (без Docker)

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Fastby/clv-prediction-service.git
   cd clv-prediction-service

2. **Создайте виртуальное окружение и установите зависимости**
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
    pip install -r api/requirements.txt

3. **Запустите сервер**
    ```bash
    cd api
    uvicorn app:app --reload

4. **Откройте Swagger UI**
    http://[ip]:8000/docs

### Вариант 2. Docker

1. **Соберите образ**
    ```bash
    docker build -t clv-api -f api/Dockerfile .

2. **Запустите контейнер**
    ```bash
    docker run -p 8000:8000 clv-api

## Пример запроса к API
### через Swagger UI:
    Перейдите на /docs, найдите эндпоинт POST /predict, вставьте JSON и выполните.

### Через Python(test_api.py)
    запустите test_api.py
