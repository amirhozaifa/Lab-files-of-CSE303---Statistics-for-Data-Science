# 3. First look into Numpy

import numpy as np
cvalues = [20.1,20.8,21.9,22.5,22.7,22.3,21.8,21.2,20.9,20.1]
C = np.array(cvalues)

print(cvalues)
print(type(cvalues))

print(C)
print(type(C))
#%%
# 4. Element-wise Operations in Numpy (Scalar Operations)

F = C * 9/5 + 32
print(F)

A = np.array([[1,2,3],[4,5,6]])
print(A)
print(A.shape)

B = np.array([[7,8,9],[10,11,12]])
print(B)
print(B.shape)

C = A + B
print(C)
print(C.shape)

#%%
# 5. Array Indexing

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:,0:2]
print(b)
print(a[0,0])
print(a)

#%%
# 6. Boolean Array Indexing (for Filtering)

a = np.array([[1,2], [3, 4], [5, 6]])
bool_idx = (a > 2)
print(bool_idx)
print(a[bool_idx])

# Alternatively
print(a[a > 2]) 

#%%
# 7. Numpy Simple Math

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))

#%%
# 8. Numpy Dot product and Vector and Matrix Multiplication

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
v = np.array([9,10])
w = np.array([11, 12])

print(v.dot(w))
print(np.dot(v, w))

print(x.dot(v))
print(np.dot(x, v))

print(x.dot(y))
print(np.dot(x, y))

#%%
# 9. Numpy Mathematical Functions

x = np.array([[1,2],[3,4]])

print(np.sum(x))

print(np.sum(x, axis=0))

print(np.sum(x, axis=1))

#%%
# 10. Numpy Statistical Functions

data1 = np.arange(1.5)
print(data1)
print(np.average(data1))

data2 = np.arange(6).reshape(3,2)
print(data2)

print(np.average(data2, axis = 0))
print(np.average(data2, axis = 1))

#%%
# 11. Broadcasting

#%%
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)

for i in range(4):
    y[i, :] = x[i, :] + v
print(y)
    
#%%
# Better Solution
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
vv = np.tile(v, (4, 1))
y = x + vv
print(y)

#%%
# Using Broadcasting
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = x + v
print(y)

#%%
# 12. Some special Numpy Arrays
x = np.zeros(5)
print(x)
x = np.zeros((2,3))
print(x)

x = np.random.rand(2,3)
print(x)

x = np.full((2,2),7)
print(x)

x = np.eye(3)
print(x)

x = np.arange(2,10,2)
print(x)

x = np.linspace(0,1,5)
print(x)

a = np.array([3,6,9,12])
a = np.reshape(a,(2,2))
print(a)

a = np.ones((2,2))
print(a)

b = a.flatten()
print(b)

a = np.array([[1,2,3],[4,5,6]])
b = np.transpose(a)
print(b)

#%%
# 13. Basic Plotting
import matplotlib.pyplot as plt

x = np.array([1,2,3])
y = np.array([2,4,1])

plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('My first graph!')

plt.show()

#%%
import matplotlib.pyplot as plt

left = [1, 2, 3, 4, 5]
height = [10, 24, 36, 40, 5]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red', 'green'])

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('My bar chart!')

plt.show()