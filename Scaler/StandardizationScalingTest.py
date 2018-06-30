import numpy as np
import matplotlib.pyplot as plt

X = np.random.randint(0, 100, (20, 2))
X = np.array(X, dtype=float)
print(X)

#均值方差归一化
X[:,0] = (X[:,0] - np.mean(X[:,0])) / np.std(X[:,0])
X[:,1] = (X[:,1] - np.mean(X[:,1])) / np.std(X[:,1])

print(X)
print("np.mean(X[:,0])",np.mean(X[:,0]))
print("np.std(X[:,0])",np.std(X[:,0]))

print("np.mean(X[:,1])",np.mean(X[:,1]))
print("np.std(X[:,1])",np.std(X[:,1]))


plt.scatter(X[:,0], X[:,1])
plt.show()

