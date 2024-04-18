import pickle
import pandas as pd

loaded_model = pickle.load(open('/home/sturmtrooper/PycharmProjects/MLOps_Sem_2/lab2/model/model.pkl', 'rb'))

# прочитаем из csv-файла подготовленный датасет для обучения
data_test = pd.read_csv('/home/sturmtrooper/PycharmProjects/MLOps_Sem_2/lab2/test/data_test.csv')
X_test = data_test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].values


# сделаем предсказание для первых 100 пассажиров из тестовой выборки
model = loaded_model.predict(X_test[0:100])
print(f"Predict: {model}")

