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
