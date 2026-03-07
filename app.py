import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 Diabetes Learning Prediction App")
st.write("This app predicts results using a trained Logistic Regression model.")

# Load model
try:
    model = pickle.load(open("Test.pkl", "rb"))
except:
    st.error("Model file not found!")
    st.stop()

# Sidebar
st.sidebar.header("Enter Feature Values")

f1 = st.sidebar.number_input("Pregnancies")
f2 = st.sidebar.number_input("Glucose")
f3 = st.sidebar.number_input("BloodPressure")
f4 = st.sidebar.number_input("SkinThickness")
f5 = st.sidebar.number_input("Insulin")
f6 = st.sidebar.number_input("BMI")
f7 = st.sidebar.number_input("DiabetesPedigreeFunction")
f8 = st.sidebar.number_input("Age")

# Prediction button
if st.button("Predict"):

    features = np.array([[f1, f2, f3, f4, f5, f6, f7, f8]])

    prediction = model.predict(features)

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("Positive Prediction")
    else:
        st.warning("Negative Prediction")

    # Probability
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(features)
        st.write("Prediction Probability:", probability)
