echo "----Create Dataset (begin)-----"
python3 /home/ubuntu/project/create_dataset.py
echo "----Create Dataset (end)-----"
echo "----Train the Model (begin)-----"
python3 /home/ubuntu/project/train_model.py
echo "----Train the Model (end)-----"
echo "----Use the Model for Prediction (begin)-----"
python3 /home/ubuntu/project/prediction.py
echo "----Use the Model for Prediction (begin)-----"