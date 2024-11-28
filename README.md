# Student Math Score Prediction 🎓
This project is an end-to-end machine learning pipeline designed to predict student math scores based on various features like gender, parental education, and test preparation efforts. The model is deployed on AWS EC2 for real-time predictions.

# Features
## Predicts math scores using:
Gender, Race/Ethnicity, Parental Level of Education, Lunch Type, Test Preparation Course, Reading Score, Writing Score.

## Tech Stack 🛠️
Programming Language: Python 🐍
Libraries: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
Deployment: Flask, Docker, AWS EC2 ☁️

## Steps Involved
1. EDA & Feature Engineering: Visualized trends and processed data for training.
2. Data Ingestion & Transformation Pipelines: Automated preprocessing workflows.
3. Model Training: Trained multiple regression models, including Linear Regression, Random Forest, and XGBoost.
4. Model Evaluation: Selected Linear Regression as the best-performing model with 87% accuracy.
5. Hyperparameter Tuning: Optimized model parameters using GridSearchCV.
6. Prediction Pipeline: Integrated preprocessing and model inference.
7. Deployment: Deployed the model API via Docker on AWS EC2.

## Key Highlights 🌟
--> Developed a scalable pipeline for efficient ML processing.
--> Used containerization with Docker for portability.
--> Deployed on AWS EC2 to enable real-time predictions.

## How to Run the Project 🚀
 - Clone the repository:
 git clone https://github.com/Aro-Anand/MLproject.git
 - Install dependencies:
 pip install -r requirements.txt
Run the application:
 - python app.py
Access the API at: http://<your-ec2-ip>:5000.
