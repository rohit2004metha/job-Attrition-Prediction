from flask import Flask,render_template, request
import joblib
import jsonify

#Loading model
model = joblib.load("model.joblib")

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

#Function which accepts new data and give prediction
def predict_attrition(new_data):
    prediction = model.predict(new_data)
    return prediction

@app.route('/predict', methods=['POST'])
def predict():
    new_data = request.get_json()
    prediction = predict_attrition(new_data)
    return jsonify({'prediction': prediction})



if __name__=="__main__":
    app.run(debug=True)

