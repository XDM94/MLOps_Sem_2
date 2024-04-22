from sklearn.preprocessing import StandardScaler
import pandas as pd

# Загрузка данных
train_data = pd.read_csv('/home/sturmtrooper/data/train/train_data.csv')
test_data = pd.read_csv('/home/sturmtrooper/data/test/test_data.csv')

# Предобработка данных
scaler = StandardScaler()
train_data['temperature'] = scaler.fit_transform(train_data[['temperature']])
test_data['temperature'] = scaler.transform(test_data[['temperature']])

# Сохранение предобработанных данных
train_data.to_csv('/home/sturmtrooper/data/train/train_data_preprocessed.csv', index=False)
test_data.to_csv('/home/sturmtrooper/data/test/test_data_preprocessed.csv', index=False)