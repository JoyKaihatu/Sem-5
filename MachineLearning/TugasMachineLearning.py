import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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






# x_b = np.concatenate((np.ones((m,n)),dataset_x),1)
theta = np.linalg.inv(dataset_x_reshape.T.dot(dataset_x_reshape)).dot((dataset_x_reshape.T).dot(dataset_y_reshape))
# print(theta.ravel())


# theta = np.linalg.solve(X_transpose_X, X_transpose_Y)
# print(theta)

y_predict = datatest.dot(theta)
# print(y_predict)



# plt.figure(figsize=(20,6))
plt.scatter(dataset[0],dataset[1], s=5,c='#6C3483')
# plt.scatter(theta,s=5)
plt.plot(datatest,y_predict,color='r')
plt.show()