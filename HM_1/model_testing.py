from sklearn.metrics import mean_squared_error
import pandas as pd
import joblib

# Загрузка модели
model = joblib.load('/home/sturmtrooper/data/model/model.pkl')

# Загрузка тестовых данных
test_data = pd.read_csv('/home/sturmtrooper/data/test/test_data_preprocessed.csv')
X_test = test_data[['day']]
y_test = test_data['temperature']

# Предсказание и оценка модели
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)

print(f'MSE: {mse}')
print(f'Predict: {predictions}')