import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data={'Experience':[1,2,3,4,5,6,7,8,9,10],
      'Salary':[45000,50000,60000,80000,110000,150000,200000,330000,410000,500000]}

df=pd.DataFrame(data)
print(df)

X = df[['Experience']]
y = df['Salary']
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

model=LinearRegression()
model.fit(X_poly, y)

y_pred = model.predict(X_poly)
mae=mean_absolute_error(y, y_pred)
mse=mean_squared_error(y, y_pred)
rmse=np.sqrt(mse)
r2=r2_score(y, y_pred)

print("nEvaluation Metrics:")
print("---------------------")
print("MAE :", round(mae,2))
print("MSE :", round(mse,2))
print("RMSE:", round(rmse,2))
print("R2 Score :", round(r2,3))
print("Accuracy :", round(r2*100,2), "%")

plt.figure(figsize=(8,6))
plt.scatter(X['Experience'], y, color='blue', label='Actual Data')

X_grid = pd.DataFrame({'Experience': np.arange(X['Experience'].min(), X['Experience'].max(), 0.1)})

plt.plot(X_grid['Experience'], model.predict(poly.transform(X_grid)), color='blue', linewidth=4, label='Polynomial regression curve')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Polynomial Regression")
plt.legend()
plt.grid(True)

plt.show()