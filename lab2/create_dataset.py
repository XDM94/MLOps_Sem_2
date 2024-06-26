from catboost.datasets import titanic

# загрузка данных
train, test = titanic()

# обработка данных
# заполним данные о поле пассажира числовыми данными (0 или 1) вместо текстовых ('male' или 'female')
train['Sex'] = train['Sex'].apply(lambda x: 0 if 'male' else 1)
test['Sex'] = test['Sex'].apply(lambda x: 0 if 'male' else 1)
# в признаке "Возраст" много пропущенных (NaN) значений, заполним их средним значением возраста
train['Age'] = train['Age'].fillna(train.Age.mean())
test['Age'] = test['Age'].fillna(train.Age.mean())

# запишем созданные датасеты во внешние csv-файлы
train[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Survived']].to_csv('/home/sturmtrooper/PycharmProjects/MLOps_Sem_2/lab2/train/data_train.csv', index=False)
test[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch']].to_csv('/home/sturmtrooper/PycharmProjects/MLOps_Sem_2/lab2/test/data_test.csv', index=False)