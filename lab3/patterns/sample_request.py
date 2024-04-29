# Пример запроса в виде requests
import requests

# URL для отправки POST-запроса
url = "http://127.0.0.1:8000/predict/"

# Данные для отправки
data = {
    "sepal_length": 1.7,
    "sepal_width": 1.2,
    "petal_length": 5.0,
    "petal_width": 1.4
}

# Отправка POST-запроса
response = requests.post(url, json=data)

# Вывод ответа
print(response.json())