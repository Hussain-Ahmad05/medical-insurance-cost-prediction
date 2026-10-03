import streamlit as st
import pandas as pd
import joblib

model=joblib.load("insurance_model.pkl")

st.title("Medical Insurance Cost Prediction")
st.subheader("Customer Information")

age=st.number_input("Age",min_value=1,max_value=100,value=25)

gender=st.selectbox("Gender",["Female","Male"])

bmi=st.number_input("BMI",min_value=0.0,max_value=100.0,value=25.0)

children=st.number_input("Children",min_value=0,max_value=100,value=0)

smoker=st.selectbox("Smoker",["Yes","No"])

region=st.selectbox("Region",["Northeast","Northwest","Southeast","Southwest"])

st.write("Age",age)
st.write("Gender",gender)
st.write("BMI",bmi)
st.write("Children",children)
st.write("Smoker",smoker)
st.write("Region",region)

if st.button("Predict Insurance Cost"):

    sex_male=1 if gender=="Male" else 0
    smoker_yes=1 if smoker=="Yes" else 0

    region_northwest=1 if region=="Northwest" else 0
    region_southeast=1 if region=="Southeast" else 0
    region_southwest=1 if region=="Southwest" else 0

    input_data=pd.DataFrame({
        "age":[age],
        "bmi":[bmi],
        "children":[children],
        "sex_male":[sex_male],
        "smoker_yes":[smoker_yes],
        "region_northwest":[region_northwest],
        "region_southeast":[region_southeast],
        "region_southwest":[region_southwest]
    })

    prediction=model.predict(input_data)

    st.success(f"Predicted Insurance Cost: ${prediction[0]:.2f}")

    # st.write("Input Data:")
    # st.dataframe(input_data)
    # st.write("sex_male:",sex_male)
    # st.write("smoker_yes:",smoker_yes)
    # st.write("region_northwest:",region_northwest)
    # st.write("region_southeast:",region_southeast)
    # st.write("region_southwest:",region_southwest)
    # st.write("Predict Button clicked!")
    

