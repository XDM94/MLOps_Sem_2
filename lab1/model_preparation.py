import joblib
import pandas as pd
from sklearn.linear_model import LassoLarsIC
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Загрузка предобработанных данных
data = pd.read_csv('/home/sturmtrooper/data/train/train_data_preprocessed.csv')
X = data[['day']]
y = data['temperature']

# Разделение данных на обучающую и валидационную выборки
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=1, random_state=42)

# Создание и обучение модели
model = LassoLarsIC()
model.fit(X_train, y_train)

predictions = model.predict(X_train)
mse = mean_squared_error(y_train, predictions)

# Сохранение модели
joblib.dump(model, '/home/sturmtrooper/data/model/model.pkl')