import numpy as np
import pprint as pp
import matplotlib.pyplot as plt

dataset = np.load("dataset.npy")
datatest = np.load("datatest.npy")

m,n = dataset.shape
a,b = datatest.shape



print(m,n)
print(a,b)

dataset_x = np.array(dataset[0, :])
dataset_y = np.array(dataset[1, :])

dataset_x_reshape = dataset_x.reshape(300,1)
dataset_y_reshape = dataset_y.reshape(300,1)

# print(dataset_x.shape)
# print(dataset_y.shape)
# print(dataset_x_reshape.shape)
# print(dataset_y_reshape.shape)
# np.savetxt('datasetXAfterReshape.csv',dataset_x_reshape)
# np.savetxt('datasetYAfterReshape.csv',dataset_y_reshape)
# print(dataset_x)

X_with_intercept = np.c_[np.ones((dataset_x_reshape.shape[0], 1)), dataset_x_reshape]

X_transpose = np.transpose(X_with_intercept)
X_transpose_X = np.dot(X_transpose,X_with_intercept)
X_transpose_Y = np.dot(X_transpose, dataset_y_reshape)


# x_b = np.concatenate((np.ones((m,n)),dataset_x),1)
# theta = np.linalg.inv(dataset_x_reshape.T.dot(dataset_x_reshape)).dot((dataset_x_reshape.T).dot(dataset_y_reshape))
# print(theta.ravel())
theta = np.linalg.solve(X_transpose_X,X_transpose_Y)
print(theta.ravel())



# theta = np.linalg.solve(X_transpose_X, X_transpose_Y)
# print(theta)

model = np.dot(X_with_intercept,theta)


# print(y_predict)
#
X_test_with_intercept = np.c_[np.ones((datatest.shape[0], 1)), datatest]
predictions = np.dot(X_test_with_intercept, theta)
# pp.pprint(predictions)

#
#
# plt.figure(figsize=(20,6))
plt.scatter(dataset[0],dataset[1], s=5,c='#6C3483', label="dataset")
# plt.scatter(theta,s=5)
plt.plot(dataset_x_reshape,model,color='r',label="model")
plt.scatter(datatest,predictions,s=5,c='g', label="predictions")
plt.legend(loc="upper left")
plt.show()