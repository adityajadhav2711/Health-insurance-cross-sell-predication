import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model
clf = pickle.load(open('clf.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Health insurance cross sell prediction")

# Gender
Gender = st.selectbox('Gender', df['Gender'].unique())

# Age of person
Age = st.number_input('Age of person',0,100)

# Driving_License

Driving_License = st.selectbox('Driving_License',df['Driving_License'].unique())

# Region_Code
Region_Code = st.selectbox('Region_Code', df['Region_Code'].unique())

# Previously_Insured
Previously_Insured = st.selectbox('Previously_Insured', df['Previously_Insured'].unique())

# Vehicle_Age
Vehicle_Age = st.selectbox('Vehicle_Age', df['Vehicle_Age'].unique())

# Vehicle_Damage
Vehicle_Damage = st.selectbox('Vehicle_Damage', df['Vehicle_Damage'].unique())

# Annual_Premium
Annual_Premium = st.number_input('Annual_Premium')

# Policy_Sales_Channel
Policy_Sales_Channel = st.selectbox('Policy_Sales_Channel', df['Policy_Sales_Channel'].unique())

# Vintage
Vintage = st.number_input('Vintage')

if st.button('Predict Price'):

    query = np.array(
        [Gender, Age, Driving_License, Region_Code, Previously_Insured, Vehicle_Age, Vehicle_Damage, Annual_Premium,
         Policy_Sales_Channel, Vintage])

    query = query.reshape(1, 10)

    # query= pd.DataFrame(data=query, index=np.arange(len(query)),
    #                     columns=['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured', 'Vehicle_Age','Vehicle_Damage', 'Annual_Premium', 'Policy_Sales_Channel', 'Vintage'])

    st.title((int((clf.predict(query)[0]))))
    
    
#     st.title((int((clf.predict(query)[0]))))
    
#     Driving_License
# Driving_License = st.selectbox('Driving_License', ('No', 'Yes'))

# if Driving_License == "Yes":
#     Driving_License = 1
# else:
#     Driving_License = 0
    
#     Previously_Insured
# Previously_Insured = st.selectbox('Previously_Insured', ('No', 'Yes'))

# if Previously_Insured == "Yes":
#     Previously_Insured = 1
# else:
#     Previously_Insured = 0
    
#     Vehicle_Damage
# Vehicle_Damage = st.selectbox('Vehicle_Damage', ('No', 'Yes'))

# if Vehicle_Damage == "Yes":
#     Vehicle_Damage = 1
# else:
#     Vehicle_Damage = 0

    