import numpy as np

A = np.arange(1,16).reshape(3,5)

print(A + 1)
'''
[[ 2  3  4  5  6]
 [ 7  8  9 10 11]
 [12 13 14 15 16]]
'''

print(A - 1)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]
'''

print(A * 2)
'''
[[ 2  4  6  8 10]
 [12 14 16 18 20]
 [22 24 26 28 30]]
'''

print(A / 2)
'''
[[0.5 1.  1.5 2.  2.5]
 [3.  3.5 4.  4.5 5. ]
 [5.5 6.  6.5 7.  7.5]]
'''

print(A // 2)
'''
[[0 1 1 2 2]
 [3 3 4 4 5]
 [5 6 6 7 7]]
'''

print(A % 2)
'''
[[1 0 1 0 1]
 [0 1 0 1 0]
 [1 0 1 0 1]]
'''

print(1 / A)
'''
[1.         0.5        0.33333333 0.25       0.2       ]
 [0.16666667 0.14285714 0.125      0.11111111 0.1       ]
 [0.09090909 0.08333333 0.07692308 0.07142857 0.06666667]]
'''

print(np.abs(A))
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]]
'''

print(np.sin(A))
'''
[[ 0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427]
 [-0.2794155   0.6569866   0.98935825  0.41211849 -0.54402111]
 [-0.99999021 -0.53657292  0.42016704  0.99060736  0.65028784]]
'''

print(np.arctan(A))
'''
[[0.78539816 1.10714872 1.24904577 1.32581766 1.37340077]
 [1.40564765 1.42889927 1.44644133 1.46013911 1.47112767]
 [1.48013644 1.48765509 1.49402444 1.49948886 1.50422816]]
'''

print(np.exp(A))
'''
[[2.71828183e+00 7.38905610e+00 2.00855369e+01 5.45981500e+01
  1.48413159e+02]
 [4.03428793e+02 1.09663316e+03 2.98095799e+03 8.10308393e+03
  2.20264658e+04]
 [5.98741417e+04 1.62754791e+05 4.42413392e+05 1.20260428e+06
  3.26901737e+06]]
'''

print(np.power(3,A))
print(3 ** A)
'''
[[       3        9       27       81      243]
 [     729     2187     6561    19683    59049]
 [  177147   531441  1594323  4782969 14348907]]
'''

print(np.log2(A))
'''
[[0.         1.         1.5849625  2.         2.32192809]
 [2.5849625  2.80735492 3.         3.169925   3.32192809]
 [3.45943162 3.5849625  3.70043972 3.80735492 3.9068906 ]]
'''

##################################################
#矩阵运算
X = np.arange(1,5).reshape(2,2)
Y = np.full((2,2),10)

#对应元素相乘，非矩阵乘法
print(X * Y)
'''
[[10 20]
 [30 40]]
'''

#矩阵乘法
print(X.dot(Y))
'''
[[30 30]
 [70 70]]
'''

#矩阵转置
print(X.T)
'''
[[1 3]
 [2 4]]
'''

v = np.array([5,6])

#将一个向量转换为与矩阵行数相同的矩阵
#print(np.vstack([v] * X.shape[0])),重要，常用！！！
print(np.tile(v, (2,1)))
'''
[[5 6]
 [5 6]]
'''

#逆矩阵，重要，常用！！！方阵才可能有逆矩阵，
#原矩阵.dot(逆矩阵)=对角线为1，其余元素为0的单位矩阵
#逆矩阵.dot(原矩阵)=对角线为1，其余元素为0的单位矩阵
print(np.linalg.inv(X))
'''
[[-2.   1. ]
 [ 1.5 -0.5]]
'''

#伪逆矩阵，重要，常用！！！实际应用中，经常不是方阵，但需要求逆，此时用伪逆矩阵，
#原矩阵.dot(伪逆矩阵)=对角线为1，其余元素为0的单位矩阵
print(np.linalg.pinv(A).shape)
#(5, 3)
print(np.linalg.pinv(A))
'''
[[-2.46666667e-01 -6.66666667e-02  1.13333333e-01]
 [-1.33333333e-01 -3.33333333e-02  6.66666667e-02]
 [-2.00000000e-02 -2.51534904e-17  2.00000000e-02]
 [ 9.33333333e-02  3.33333333e-02 -2.66666667e-02]
 [ 2.06666667e-01  6.66666667e-02 -7.33333333e-02]]
'''

