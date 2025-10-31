from numpy import *
import numpy #后续调用函数要用numpy打头
import numpy as np # 后续调用函数用np

# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# arr1 = np.array(A)
# print("A = ",A)
# print("通过列表A创建的矩阵\n",arr1)
# B = ((1,2,3,4),(4,5,6,7),(8,9,10,11))
# arr2 = np.array(B)
# print(B)
# print("通过元组B创建的矩阵\n",arr2)
# print("A的类型",type(A))
# print("B的类型",type(B))
# print("arr1的类型：",type(arr1))
# print("arr1的大小：",arr1.shape)
# # C = np.shape(arr1)
# # D = arr1.shape
# arr3 = np.random.random((2,3))
# print("创建的浮点数构成的2*3的矩阵：\n",arr3)
# arr4 = np.random.randint(3,30,size = [2,3])#生成的数属于[low,high]，矩阵的形状取决于size
# print("随机创建的3—30的随机整数组成的矩阵：\n",arr4)

# A = [1,2,3,4,5,6]
# B = np.array(A)
# C1 = B.reshape(2,3)
# # C1 = B.reshape(2,-1)生成的矩阵和C1 = B.reshape(2,3)是一样的，因为如果一位是-1的话，reshape（）会根据另一个参数计算出-1代表的具体值
# C2 = B.reshape(3,2)
# print(B)
# print("2行3列的矩阵\n",C1)
# print("3行2列的矩阵\n",C2)
# print("输出的C1的第0行元素C1[0]\n",C1[0])
# print("输出的C1的前两行元素C1[0：2]\n",C1[0:2])
# print("输出的C1的第0行和第2行元素C1[0，2]\n",C1[0,2])
# print("输出的C1的第1列元素C2[：,1]\n",C2[:,1])
# print("输出的C1的前两列元素C1[：，0：2]\n",C1[:,0:2])
# #在这里“，”是把行和列隔开
# print("输出C2的第二行第一列的数C2[2,1]",C2[2,1])#这里的一二表示计算机里的一二，不是高等代数里的一二

# A = [[1,2,3,4,5]]#A如果是一维数组，如果想要用array生成矩阵，那么A后面一定要是[[]]，用[]只会得到一维数组，不会得到矩阵、
# B = [[1],[2],[3],[4],[5]]
# arr1 = np.array(A)
# arr2 = np.array(B)
# print(arr1)
# print(arr2)
# print("A的类型%s，arr1的类型%s"%(type(A),type(arr1)))
# print("B的类型%s，arr2的类型%s"%(type(B),type(arr2)))
# C = [1,2,3,4,5]
# arr3 = np.array(C)
# print("C的类型：%s，C的大小%s"%(type(C),np.shape(arr3)))
# print("A的类型%s"%(type(A)))

arr1 = np.random.random((3,1))
arr2 = np.random.random((1,3))
arr3 = np.random.randint(3,30,size =(1,3))
arr4 = np.random.randint(3,30,size =(3,1) )
print(arr1)
print(arr2)
print("3—30（不包括30）的1*3的矩阵\n",arr3)
print("3—30的3(不包括30)*1的矩阵\n",arr4)


