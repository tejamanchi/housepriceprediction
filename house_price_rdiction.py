print("Hello Machine Leanning")
imort numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
data=pd.read_csv("data/Housing.csv")
print(data.head())
x=data[['area','bedrooms','bathrooms']]
y=data['price']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train, y_train)
y_pred=model.predict(X_test)
from sklearn.metrics import mean_absolute_error,r2_score
mae=mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("MAE:",mae)
print("R2 Score:",r2)
sample_house=[[5000,3,2]]
prediction=model.predict(sample_house)
print("Predicted price:",prediction[0])
plt.scatter(y_test,y_pred)
plt.xlabel("Actual prices")
plt.ylabel("Predicted prices")
plt.title("Actual vs Predicted Prices")
plt.show()