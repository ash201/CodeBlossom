# Customer Churn Prediction

## Project Overview

This project predicts whether a telecom customer is likely to churn (leave the company) based on customer demographics, account information, and service usage.

The project includes:

* Data preprocessing and feature engineering
* Exploratory Data Analysis (EDA)
* Machine Learning model training
* Model evaluation
* Flask web application for predictions
* Docker containerization

## Dataset

Dataset: Telco Customer Churn Dataset

Features include:

* Gender
* Senior Citizen
* Tenure
* Monthly Charges
* Total Charges
* Internet Service
* Contract Type
* Payment Method
* Additional Services

Target Variable:

* Churn (Yes/No)

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Flask
* Joblib
* Docker

## Project Structure

```text
Capstone-Project/
│
├── customer-churn-prediction.ipynb
├── app.py
├── churn_model.pkl
├── scaler.pkl
├── requirements.txt
├── Dockerfile
├── templates/
│   ├── index.html
│   └── result.html
└── README.md
```

## Model Workflow

1. Load and clean the dataset
2. Perform feature engineering
3. Encode categorical variables
4. Scale numerical features
5. Train classification model
6. Evaluate model performance
7. Save trained model
8. Deploy using Flask and Docker

## Running the Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

## Docker Deployment

Build image:

```bash
docker build -t churn-app .
```

Run container:

```bash
docker run -p 5001:5000 churn-app
```

Open:

```text
http://localhost:5001
```

## Future Improvements

* Hyperparameter tuning
* Model monitoring
* Cloud deployment
* Interactive dashboard


