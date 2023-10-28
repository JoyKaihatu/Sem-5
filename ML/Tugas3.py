from sklearn.datasets import make_regression
import pandas as pd
from sklearn.linear_model import BayesianRidge, Ridge, LinearRegression, Lasso, ElasticNet
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import SymLogNorm
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

figure, axis = plt.subplots(2,2,constrained_layout=True)

# Bayessian Ridge
X, y, true_weights = make_regression(
 n_samples=100,
 n_features=100,
 n_informative=10,
 noise=8,
 coef=True,
 random_state=42,
)
brr = BayesianRidge(compute_score=True, n_iter=30).fit(X, y)
rng = np.random.RandomState(0)
n_samples = 110

# sort the data to make plotting easier later
X = np.sort(-10 * rng.rand(n_samples) + 10)
noise = rng.normal(0, 1, n_samples) * 1.35
y = np.sqrt(X) * np.sin(X) + noise
full_data = pd.DataFrame({"input_feature": X, "target": y})
X = X.reshape((-1, 1))
# extrapolation
X_plot = np.linspace(10, 10.4, 10)
y_plot = np.sqrt(X_plot) * np.sin(X_plot)
X_plot = np.concatenate((X, X_plot.reshape((-1, 1))))
y_plot = np.concatenate((y - noise, y_plot))
brr_poly = make_pipeline(
 PolynomialFeatures(degree=10, include_bias=False),
 StandardScaler(),
 BayesianRidge(),
).fit(X, y)



# plt.figure(figsize=(10, 6))
y_brr, y_brr_std = brr_poly.predict(X_plot, return_std=True)

ax = sns.scatterplot( ax=axis[0,0],
 data=full_data, x="input_feature", y="target", color="black",
 alpha=0.75)
ax.plot(X_plot, y_plot, color="black", label="Ground Truth")
ax.plot(X_plot, y_brr, color="red",
 label="BayesianRidge with polynomial features")
ax.fill_between(X_plot.ravel(), y_brr - y_brr_std, y_brr + y_brr_std,
 color="red", alpha=0.3,)
ax.legend()
_ = ax.set_title("Polynomial fit of a non-linear feature")



#Ridge
# plt.figure(figsize=(10, 6))
X, y, true_weights = make_regression(
 n_samples=100,
 n_features=100,
 n_informative=10,
 noise=8,
 coef=True,
 random_state=42,
)

rdg = Ridge(alpha=0.01).fit(X,y)
rng = np.random.RandomState(0)
rdg_samples = 110

X = np.sort(-10 * rng.rand(rdg_samples) + 10)
noise = rng.normal(0,1,rdg_samples) * 1.35
y = np.sqrt(X) * np.sin(X) + noise
full_data_rdg = pd.DataFrame({"input_feature": X, "target": y})

X = X.reshape((-1, 1))

X_plot = np.linspace(10, 10.4, 10)
y_plot = np.sqrt(X_plot) * np.sin(X_plot)
X_plot = np.concatenate((X, X_plot.reshape((-1, 1))))
y_plot = np.concatenate((y - noise, y_plot))

rdg_poly = make_pipeline(PolynomialFeatures(degree=10,include_bias=False),
           StandardScaler(), Ridge()).fit(X,y)
y_rdg= rdg_poly.predict(X_plot)
# residual = y - y_rdg
y_rdg_std = np.std(X_plot/2)


ax = sns.scatterplot( ax=axis[0,1],
 data=full_data_rdg, x="input_feature", y="target", color="black",
 alpha=0.75)
ax.plot(X_plot, y_plot, color="black", label="Ground Truth")
ax.plot(X_plot, y_rdg, color="red",
 label="Ridge With Polynomial Features")
ax.fill_between(X_plot.ravel(), y_rdg  - y_rdg_std, y_rdg + y_rdg_std ,
 color="blue", alpha=0.3,)
ax.legend()
_ = ax.set_title("Ridge Plot")


#Lasso
# plt.figure(figsize=(10, 6))
X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)

# Fit a Lasso model
lasso = Lasso(alpha=0.01).fit(X, y)

# Generate sample data for plotting
rng = np.random.RandomState(0)
lasso_samples = 110
X = np.sort(-10 * rng.rand(lasso_samples) + 10)
noise = rng.normal(0, 1, lasso_samples) * 1.35
y = np.sqrt(X) * np.sin(X) + noise
full_data_lasso = pd.DataFrame({"input_feature": X, "target": y})

X = X.reshape((-1, 1))

X_plot = np.linspace(10, 10.4, 10)
y_plot = np.sqrt(X_plot) * np.sin(X_plot)
X_plot = np.concatenate((X, X_plot.reshape((-1, 1))))
y_plot = np.concatenate((y - noise, y_plot))

lasso_poly = make_pipeline(PolynomialFeatures(degree=10, include_bias=False),
                          StandardScaler(), Lasso(alpha=0.01)).fit(X, y)
y_lasso = lasso_poly.predict(X_plot)
y_lasso_std = np.std(X_plot / 2)

# Create the Lasso plot
ax = sns.scatterplot( ax = axis[1,0],
    data=full_data_lasso, x="input_feature", y="target", color="black",
    alpha=0.75)
ax.plot(X_plot, y_plot, color="black", label="Ground Truth")
ax.plot(X_plot, y_lasso, color="blue",
        label="Lasso With Polynomial Features")
ax.fill_between(X_plot.ravel(), y_lasso - y_lasso_std, y_lasso + y_lasso_std,
                color="blue", alpha=0.3,)
ax.legend()
_ = ax.set_title("Lasso")

#Elastic Net
# plt.figure(figsize=(10, 6))
X, y, true_weights = make_regression(
    n_samples=100,
    n_features=100,
    n_informative=10,
    noise=8,
    coef=True,
    random_state=42,
)

# Fit an ElasticNet model
elastic_net = ElasticNet(alpha=0.01, l1_ratio=0.5).fit(X, y)

# Generate sample data for plotting
rng = np.random.RandomState(0)
elastic_net_samples = 110
X = np.sort(-10 * rng.rand(elastic_net_samples) + 10)
noise = rng.normal(0, 1, elastic_net_samples) * 1.35
y = np.sqrt(X) * np.sin(X) + noise
full_data_elastic_net = pd.DataFrame({"input_feature": X, "target": y})

X = X.reshape((-1, 1))

X_plot = np.linspace(10, 10.4, 10)
y_plot = np.sqrt(X_plot) * np.sin(X_plot)
X_plot = np.concatenate((X, X_plot.reshape((-1, 1))))
y_plot = np.concatenate((y - noise, y_plot))

elastic_net_poly = make_pipeline(PolynomialFeatures(degree=10, include_bias=False),
                                StandardScaler(), ElasticNet(alpha=0.01, l1_ratio=0.5)).fit(X, y)
y_elastic_net = elastic_net_poly.predict(X_plot)
y_elastic_net_std = np.std(X_plot / 2)

# Create the ElasticNet plot
ax = sns.scatterplot( ax=axis[1,1],
    data=full_data_elastic_net, x="input_feature", y="target", color="black",
    alpha=0.75)
ax.plot(X_plot, y_plot, color="black", label="Ground Truth")
ax.plot(X_plot, y_elastic_net, color="green",
        label="ElasticNet With Polynomial Features")
ax.fill_between(X_plot.ravel(), y_elastic_net - y_elastic_net_std, y_elastic_net + y_elastic_net_std,
                color="green", alpha=0.3,)
ax.legend()
_ = ax.set_title("ElasticNet Plot")



# figure.tight_layout()
plt.show()