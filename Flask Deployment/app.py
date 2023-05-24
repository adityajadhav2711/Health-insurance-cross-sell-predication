from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd


app = Flask(__name__)
df = pd.read_csv('Prediction_on_test_by_Knn.csv')
model = pickle.load(open('clf.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    gender = request.form.get('Gender')
    age = request.form.get('Age')
    driving_license = request.form.get('Driving_License')
    region_code = request.form.get('Region_Code')
    previously_insured = request.form.get('Previously_Insured')
    vehicle_age = request.form.get('Vehicle_Age')
    vehicle_damage = request.form.get('Vehicle_Damage')
    annual_premium = request.form.get('Annual_Premium')
    policy_sales_channel = request.form.get('Policy_Sales_Channel')
    vintage = request.form.get('Vintage')
    
    print(gender,age,driving_license,region_code,previously_insured,vehicle_age,vehicle_damage,annual_premium,policy_sales_channel,vintage)
    
    input = pd.DataFrame([[gender,age,driving_license,region_code,previously_insured,vehicle_age,vehicle_damage,annual_premium,policy_sales_channel,vintage]],columns=['Gender','Age','Driving_License','Region_Code','Previously_Insured','Vehicle_Age','Vehicle_Damage','Annual_Premium','Policy_Sales_Channel','Vintage'])
    
    prediction = model.predict(input)[0]
    
    if prediction == 0:
        return "Customer is not intrested to buy Insurance"
    else:
        return "Customer is intrested to buy Insurance"

if __name__ == '__main__':
    app.run(debug=True)