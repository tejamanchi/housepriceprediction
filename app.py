import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Page settings
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠"
)

# Website title
st.title("🏠 House Price Prediction Website")

st.write("Enter House Details Below")

# Inputs
area = st.number_input("Area in Square Feet")

bedrooms = st.number_input(
    "Number of Bedrooms",
    step=1
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    step=1
)

# Prediction button
if st.button("Predict Price"):

    # Create feature array
    features = np.array([
        [area, bedrooms, bathrooms]
    ])

    # Predict price
    prediction = model.predict(features)

    # Display result
    st.success(
        f"Estimated House Price: ₹ {prediction[0]:,.2f}"
    )