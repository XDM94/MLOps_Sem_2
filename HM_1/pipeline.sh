python3 -m venv /home/sturmtrooper/homework1/ || { echo "Ошибка при создании виртуального окружения."; exit 1; }
source /home/sturmtrooper/homework1/bin/activate || { echo "Ошибка при активации виртуального окружения."; exit 1; }
echo "Устанавливаю зависимости"
pip install -r /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/requirements.txt || { echo "Ошибка при установке зависимостей."; exit 1; }
echo "----Create Dataset (begin)-----"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/data_creation.py
echo "----Create Dataset (end)-----"
echo "----Train the Model (begin)-----"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/model_preprocessing.py
echo "----Train the Model (end)-----"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/model_preparation.py
echo "----Use the Model for Prediction (begin)-----"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/model_testing.py
echo "Use test for model MSE"
