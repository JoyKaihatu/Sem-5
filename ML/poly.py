import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

# Read data from an Excel file into a DataFrame
data = pd.read_excel("Datas/dataset.xlsx", sheet_name="Training", header=0)
data = pd.DataFrame(data)

training, test = train_test_split(data, test_size=0.2, random_state=1)

u = training['U'].values
v = training['V'].values
w = training['W'].values
x = training['X'].values
z = training['Z'].values

print(training)
# print(training)
# print(test)

polynomial_regression = Pipeline((("poly_features", PolynomialFeatures(degree=10, include_bias=False)),("sgd_reg", LinearRegression())))

polynomial_regression.fit(u, v, w, x, z)
X_test = [[i] for i in np.linspace(-3,3,training.shape[0])]
y_poly = polynomial_regression.predict(X_test)

data.to_excel('c14210047.xlsx', index=False)