import pandas as pd

# Загрузка датасета
df = pd.read_csv('/home/sturmtrooper/data1/datasets/titanic/titanic_data.csv')

# Заполнение пропущенных значений в поле "Age" средним значением
mean_age = df['Age'].mean()
df['Age'] = df['Age'].fillna(mean_age)

# Сохранение новой версии датасета
df.to_csv('/home/sturmtrooper/data1/datasets/titanic/titanic_data.csv', index=False)