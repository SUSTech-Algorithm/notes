from randomdata import RandomData
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x_train, y_train = RandomData().generate_data()
model = LinearRegression()
model.fit(x_train, y_train)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
plt.scatter(x_train, y_train, color='blue', label='Data Points')
plt.plot(x_train, model.predict(x_train), color='red', label='Regression Line', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Linear Regression Example')
plt.legend()
plt.show()