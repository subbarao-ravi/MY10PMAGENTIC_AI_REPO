import numpy as np

a = np.array([1,2,3,4,5,6])
print(a)
print(a.shape)#1D with 6 elements(6,)


b= np.array([[10,20,30],[40,50,60]])
print(b)
print(b.shape)#(2,3)

c= np.array([[10,20,30],[1,2,3],[5,6,7]])
print(c)
print(c.shape)#(3,3)

d=np.array([[1,2,3,4],[5,6,7,8]])
print(d)
print(d.shape)

e=np.array([[1],[2],[3],[4]])
print(e.shape)

e=np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]])
print(e.shape)