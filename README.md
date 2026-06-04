Python Starter Projects: Chatbot & Iris Classifier
Welcome to this repository! This collection includes two straightforward Python scripts: a text-based chatbot and a machine learning classifier using the K-Nearest Neighbors (KNN) algorithm.
1. Dictionary-Based Chatbot
This is a simple, lightweight chatbot built as a learning project to demonstrate dictionary-based conversational agents.
Features:
Predefined Responses: The bot looks up user inputs in a built-in dictionary to answer phrases like "hello", "what is your name", and "who made you".
Fallback Mechanism: If it doesn't recognize a phrase, it gently informs the user and suggests typing "help" to see what it can understand.
Continuous Loop: The chat runs continuously in the terminal until the user types the "exit" command.
2. K-Nearest Neighbors Classifier
This script implements a complete machine learning pipeline to classify flowers using the famous Iris dataset.
How It Works:
Data Preprocessing: It loads the dataset, scales the features using StandardScaler, and performs a three-way data split: 60% for training, 20% for validation, and 20% for testing.
Hyperparameter Tuning: The script iterates through K values (number of neighbors) from 1 to 20. It calculates the validation error rate to automatically find and select the best K.
Model Evaluation: The final model combines the training and validation sets for fitting, then evaluates its performance against the unseen test set, outputting both the accuracy and a weighted F1 score.
Sample Prediction: It demonstrates real-world usage by predicting the species of a new, completely unseen flower with the measurements [5.1, 3.5, 1.4, 0.2]
Visualizations
Running this script automatically generates and saves two visual reports to help you understand the model's performance:
elbow_plot.png: A line chart showing the validation error rate across different K values, which helps visually confirm the optimal number of neighbors.
confusion_matrix.png: A heatmap visualizing the final model's predictions versus the actual flower species.
Requirements:
To run the machine learning script, you will need the following Python libraries installed:
numpy  pandas  matplotlib  seaborn  scikit-learn  
