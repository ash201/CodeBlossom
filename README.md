# Customer Churn Prediction

## About the Project

This project focuses on predicting whether a telecom customer is likely to leave the company's services (churn) based on customer information such as tenure, monthly charges, contract type, and other service-related details.

The goal was not only to build a machine learning model but also to take it all the way to deployment by creating a web application using Flask and Docker.

---

## Problem Statement

Customer churn is a major concern for telecom companies because losing existing customers can directly impact revenue.

Using historical customer data, the objective is to predict whether a customer is likely to churn so that the business can take proactive measures to retain them.

---

## Dataset

Dataset Used: Telco Customer Churn Dataset

The dataset contains information about customers including:

* Customer tenure
* Monthly charges
* Total charges
* Contract type
* Internet service
* Payment method
* Tech support
* Online security
* Demographic information
* Churn status

Target Variable:

* Churn = Yes
* Churn = No

---

## Project Workflow

### 1. Data Cleaning

* Handled missing values
* Fixed data type issues
* Cleaned the TotalCharges column
* Removed inconsistencies in the dataset

### 2. Exploratory Data Analysis (EDA)

Performed EDA to understand customer behaviour and identify factors influencing churn.

Some observations:

* Customers with month-to-month contracts were more likely to churn.
* Customers with shorter tenure showed higher churn rates.
* Customers paying higher monthly charges were more likely to leave.
* Contract type had a strong impact on customer retention.

### 3. Feature Engineering

Created additional features to improve model performance.

Examples:

* Account Age Groups
* Average Monthly Spend

### 4. Data Preprocessing

* One-Hot Encoding for categorical variables
* Feature Scaling using StandardScaler

---

## Models Trained

The following machine learning models were trained and compared:

* Logistic Regression
* Random Forest
* k-Nearest Neighbors (kNN)
* Support Vector Machine (SVM)
* XGBoost

---

## Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Cross Validation

Cross-validation helped compare model stability and generalization performance.

### Cross Validation Scores

| Model               | CV Score |
| ------------------- | -------- |
| Logistic Regression | 0.846    |
| Random Forest       | 0.823    |
| XGBoost             | 0.824    |
| kNN                 | 0.773    |
| SVM                 | 0.800    |

---

## Hyperparameter Tuning

Hyperparameter tuning was performed using GridSearchCV.

The models tuned were:

* Logistic Regression
* Random Forest
* XGBoost

### Best XGBoost Parameters

```python
{
    "learning_rate": 0.1,
    "max_depth": 3,
    "n_estimators": 100
}
```

Best ROC-AUC Score:

```python
0.8472
```

---

## Model Explainability

SHAP (SHapley Additive Explanations) was used to understand which features had the greatest influence on predictions.

Some important features identified were:

* Tenure
* Monthly Charges
* Contract Type
* Internet Service
* Payment Method

---

## Model Deployment

After training the model, it was deployed using Flask.

The application provides:

* A simple web interface
* Real-time churn prediction
* REST API endpoint for predictions

Users can enter customer details and instantly receive churn predictions.

---

## Dockerization

The application was containerized using Docker.

This ensures that the project can run consistently across different environments without manually installing dependencies.

### Build Docker Image

```bash
docker build -t churn-app .
```

### Run Docker Container

```bash
docker run -p 5001:5000 churn-app
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* SHAP
* Flask
* HTML
* Docker

---

## Project Structure

```text
Capstone-Project/
│
├── app.py
├── churn_model.pkl
├── scaler.pkl
├── requirements.txt
├── Dockerfile
├── customer-churn-prediction.ipynb
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── WA_Fn-UseC_-Telco-Customer-Churn.csv
```

---

## Future Improvements

Some improvements that can be added in future:

* Better UI using Bootstrap
* More customer input fields in the web application
* Cloud deployment (AWS/Azure/GCP)
* CI/CD integration
* Database integration

---

## Conclusion

This project helped me understand the complete machine learning lifecycle, from data preprocessing and model building to deployment and Dockerization.

It was a great opportunity to combine machine learning, backend development, and deployment concepts into a single end-to-end project.
