import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load trained model safely using caching so it doesn't reload on every click
@st.cache_resource
def load_model():
    try:
        return pickle.load(open("model.pkl", "rb"))
    except FileNotFoundError:
        return None

model = load_model()

# Page settings
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Design an attractive header
st.title("🏠 House Price Prediction Website")
st.markdown("Estimate the market value of a residential property using Machine Learning.")
st.markdown("---")

if model is None:
    st.error("⚠️ `model.pkl` not found! Please run your machine learning script first to train and save the model.")
else:
    st.subheader("Enter House Details Below")
    
    # Use columns to stack inputs horizontally for a cleaner layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        area = st.number_input(
            "Area (Sq. Ft.)", 
            min_value=100, 
            max_value=25000, 
            value=1200, 
            step=50
        )
        
    with col2:
        bedrooms = st.number_input(
            "Bedrooms", 
            min_value=1, 
            max_value=10, 
            value=2, 
            step=1
        )
        
    with col3:
        bathrooms = st.number_input(
            "Bathrooms", 
            min_value=1, 
            max_value=8, 
            value=1, 
            step=1
        )

    st.markdown("---")

    # Prediction button
    if st.button("Predict Price", type="primary"):
        
        # Pass features as a DataFrame to keep feature names intact and avoid warnings
        features = pd.DataFrame({
            'area': [area],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms]
        })

        # Predict price
        prediction = model.predict(features)
        
        # Extract single value out of the array safely
        predicted_price = prediction[0]
        
        # Display result beautifully with st.metric
        st.success("🎉 Prediction Generated Successfully!")
        st.metric(
            label="Estimated Market Value", 
            value=f"₹ {predicted_price:,.2f}"
        )
