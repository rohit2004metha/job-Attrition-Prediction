from flask import Flask, render_template, jsonify, request
import joblib
import json
import pandas as pd
import numpy as np

# Loading model
model = joblib.load("website/model.joblib")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/team")
def team():
    return render_template("team.html")

# Function which accepts new data and gives prediction
def predict_attrition(new_data):
    prediction = model.predict(new_data)
    return prediction

@app.route('/predict', methods=['POST'])
def predict():
    data={
    'Age' : int(request.form['Age']),
    'BusinessTravel' : int(request.form['BusinessTravel']),
    'DailyRate' : int(request.form['DailyRate']),
    'Department' : int(request.form['Department']),
    'DistanceFromHome' : int(request.form['DistanceFromHome']),
    'Education' : int(request.form['Education']),
    'EducationField' : int(request.form['EducationField']),
    'EnvironmentSatisfaction' : int(request.form['EnvironmentSatisfaction']),
    'Gender' : int(request.form['Gender']),
    'HourlyRate' : int(request.form['HourlyRate']),
    'JobInvolvement' : int(request.form['JobInvolvement']),
    'JobLevel' : int(request.form['JobLevel']),
    'JobRole' : int(request.form['JobRole']),
    'JobSatisfaction' : int(request.form['JobSatisfaction']),
    'MaritalStatus' : int(request.form['MaritalStatus']),
    'MonthlyIncome' : int(request.form['MonthlyIncome']),
    'MonthlyRate': int(request.form['MonthlyRate']),
    'NumCompaniesWorked' : int(request.form['NumCompaniesWorked']),
    'OverTime' : int(request.form['OverTime']),
    'PercentSalaryHike' : int(request.form['PercentSalaryHike']),
    'PerformanceRating' : int(request.form['PerformanceRating']),
    'RelationshipSatisfaction' : int(request.form['RelationshipSatisfaction']),
    'StockOptionLevel' : int(request.form['StockOptionLevel']),
    'TotalWorkingYears' : int(request.form['TotalWorkingYears']),
    'TrainingTimesLastYear' : int(request.form['TrainingTimesLastYear']),
    'WorkLifeBalance' : int(request.form['WorkLifeBalance']),
    'YearsAtCompany' : int(request.form['YearsAtCompany']),
    'YearsInCurrentRole' : int(request.form['YearsInCurrentRole']),
    'YearsSinceLastPromotion' : int(request.form['YearsSinceLastPromotion']),
    'YearsWithCurrManager' : int(request.form['YearsWithCurrManager'])
    }
    df = pd.DataFrame(data, index=[0])
    prediction = predict_attrition(df)
    prediction = int(prediction[0])
    if prediction:
        value = "leave"
    else:
        value = "not leave"
    return render_template("result.html", result = value)


if __name__ == "__main__":
    app.run(debug=True)
