🏠 House Price Prediction
📌 Overview
This project predicts house prices using machine learning. It trains a regression model on housing data and provides a simple app interface for making predictions.

⚙️ Features
Data preprocessing and feature engineering
Model training and saving (model.pkl)
Web app (app.py) for user-friendly predictions
Example dataset included in data/

📂 Project Structure
Code
SCT_ML_1/
│── data/                # Dataset files
│── src/                 # Source code (preprocessing, training, prediction)
│── app.py               # Web app entry point
│── requirements.txt     # Dependencies
│── model.pkl            # Trained model
│── README.md            # Documentation
│── tests/               # Unit tests

🚀 Installation
Clone the repository and install dependencies:
bash
git clone https://github.com/tejamanchi/SCT_ML_1.git
cd SCT_ML_1
pip install -r requirements.txt

▶️ Usage
Run the web app:
bash
python app.py
Or, if using Streamlit:
bash
streamlit run app.py

📊 Results
Model: Linear Regression (baseline)
Metrics: RMSE = XX, MAE = XX, R² = XX
(replace XX with your actual results)
Example prediction:
Code
Input: 3-bedroom house, 1200 sq ft
Output: ₹45 lakhs

🔮 Future Improvements
Add advanced models (Random Forest, XGBoost)
Deploy with Docker or cloud services
Add API endpoints for predictions
Improve dataset with more features

🤝 Contributing
Contributions are welcome! Fork the repo and submit a pull request.

## Live Demo
sctml1-xm67bsthkaujjfkkanmnb4

##Author
Tejaswini Manchi
