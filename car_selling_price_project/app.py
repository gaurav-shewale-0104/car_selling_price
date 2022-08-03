from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import pickle
app = Flask(__name__)

model =pickle.load(open("model.pkl", "rb"))
ld = LabelEncoder()
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():
    data = request.form
    input_data = np.zeros(7)
    input_data[0] = float(data["Present_Price"])
    input_data[1] = int(data["Kms_Driven"])
    input_data[2] = data["Fuel_Type"]
    input_data[3] = data["Seller_Type"]
    input_data[4] = data["Transmission"]
    input_data[5] = data["Owner"]
    input_data[6]= (2022 -int(data["Year"]))
    
  
    
    result = model.predict([input_data])
    if result<0:
        result ="Sorry you cannot sell this car"
    else:
       return render_template("index.html", Price="You Can Sell The Car at {}".format(result))

if __name__ == "__main__":
    app.run(debug=True)
    