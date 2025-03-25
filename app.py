import streamlit as st
import pandas as pd

st.title("BMI-Calculator");
 
height = st.slider("Enter Your height in (CM): ",100,250,170)
weight = st.slider("Enter Your weight in (kilograms): ",100,250,175)

BMI = weight / ((height /100) ** 2)


st.write(f"Your BMI is: {BMI:2f}")
st.write("### BMI Category ###")
st.write("-Underweight: BMI less then 18.5")
st.write("Normal weight : BMI between 18.5 and 24.5")
st.write("Overweight: BMI between 25 and 29.9")
st.write("Overweight: BMI greater then 30")

  