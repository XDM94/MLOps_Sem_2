echo "Create Dataset"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/lab2/create_dataset.py
echo "Create Dataset Success"
echo "Start train the Model"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/lab2/train_model.py
echo "Train the Model Success"
echo "Use the Model for Prediction"
python3 /home/sturmtrooper/PycharmProjects/MLOps_Sem_2/lab2/make_prediction.py