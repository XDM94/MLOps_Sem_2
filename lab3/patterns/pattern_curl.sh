# Пример запроса в виде curl
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'Content-Type: application/json' \
  -d '{
  "sepal_length": 4.1,
  "sepal_width": 2.5,
  "petal_length": 1.7,
  "petal_width": 0.4
}'