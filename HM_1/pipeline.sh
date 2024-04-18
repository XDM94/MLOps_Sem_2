echo "Create Dataset"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/data_creation.py
echo "Create Dataset Success"
echo "Start train the Model"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/model_preprocessing.py
echo "Train the Model Success"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/model_preparation.py
echo "Use the Model for Prediction"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/HM_1/model_testing.py

