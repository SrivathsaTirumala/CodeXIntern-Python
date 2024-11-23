import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.express as px

model = pickle.load(open("health_model.pkl", "rb"))

st.title("Smart Health Monitoring System")

st.sidebar.header("User Input")
age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30)
heart_rate = st.sidebar.number_input("Heart Rate (bpm)", min_value=50, max_value=200, value=80)
weight = st.sidebar.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
glucose = st.sidebar.number_input("Glucose Level (mg/dL)", min_value=50, max_value=250, value=100)
calories = st.sidebar.number_input("Calories Burned", min_value=100, max_value=4000, value=2000)

inputs = np.array([[age, heart_rate, weight, glucose, calories]])

if st.sidebar.button("Predict Risk"):
    prediction = model.predict(inputs)[0]
    risk = "High" if prediction == 1 else "Low"
    st.subheader(f"Health Risk: {risk}")

st.header("Health Metrics Visualization")

data = {
    "Age": np.random.randint(18, 80, 100),
    "Heart Rate": np.random.randint(50, 180, 100),
    "Calories": np.random.randint(1500, 3500, 100)
}

df = pd.DataFrame(data)

fig = px.line(df, x="Age", y="Heart Rate", title="Heart Rate vs Age")
st.plotly_chart(fig)

fig2 = px.scatter(df, x="Age", y="Calories", title="Calories Burned vs Age")
st.plotly_chart(fig2)

st.write(f"**User Input Summary**:")
st.write(f"Age: {age}")
st.write(f"Heart Rate: {heart_rate}")
st.write(f"Weight: {weight}")
st.write(f"Glucose: {glucose}")
st.write(f"Calories Burned: {calories}")
