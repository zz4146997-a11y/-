## 使用python求sinx/x在x趋近无穷时的值
# import sympy
# from sympy import oo #oo表示无穷
# import numpy as np
# x = sympy.Symbol('x')
# f = sympy.sin(x)/x
# a = sympy.limit(f,x,oo)
# print(a)

##使用python求x**2-1/x-1在x趋近1时的极限
# import sympy
# from sympy import oo
# import numpy as np
# x = sympy.Symbol('x')
# f = sympy.sin(x)/(3*x+x**3)
# print(sympy.limit(f,x,0))


# # import sympy
# from sympy import *
# from sympy .abc import x,y,z,f
# # x,y = sympy.Symbol('x,y')
# diff(asin(sqrt(sin(x))))
#
# from sympy import *
# from sympy.abc import x,y,a,b
# f = x**2+3*x*y+y**2
# diff(f,x)
# diff(f,y)5
# fx = diff(f,x)
# a = fx.evalf(subs={x:1,y:2})
# print(a)




import numpy as np

from traceback import print_tb

# A = [3,4]
# B = [4,3]
# arr1 = np.random.randint(3,9,size = A)
# arr2 = np.random.randint(10,30,size = A)
# arr3 = np.random.randint(50,100,size = B)#size=A表示矩阵的大小是3*4的矩阵
# print("arr1 = \n",arr1)
# print("arr2 = \n",arr2)
# print("arr3 = \n",arr3)
# print("arr1与arr2是否同型\n",np.shape(arr1)==np.shape(arr2))
# print("arr3与arr2是否同型\n",np.shape(arr3)==np.shape(arr2))

# A = np.array([[1,1,1],[1,2,4],[1,3,9]])
# B = np.array([[2,3,5]])
# C = np.array([[1,1,1],[1,2,4],[1,3,9]])
# print("A与B是否相等:\n",np.allclose(A,B))
# print("A与C是否相等:\n",np.allclose(A,C))

#矩阵加减法
# A = [[1,2,3],[3,2,1]]
# B = [[6,8,12],[10,5,12]]
# C = np.array(A)
# D = np.array(B)
# print("C+D=\n",C+D)
# print("C-D=\n",C-D)

#矩阵数乘
# A = [[1,2,3],[4,5,6]]
# C =np.array(A)
# print("矩阵数乘结果2C=\n",2*C)

#矩阵乘法
# A = np.array([[1,2,3],[4,5,6]])
# B = np.array([[1,2],[3,4],[5,6]])
# C = np.dot(A,B)
# # C= A.dot(B)
# print("矩阵乘法：\n",C)
# one_vec1 = np.array([1,2,3])
# one_vec2 = np.array([4,5,6])
# one_mulit_result = np.dot(one_vec1,one_vec2)
# print("一维数组乘法：\n",one_mulit_result)
#
#
# A = np.array([[1,2,3],[4,5,6]])
# B = np.array([[7,8,9],[4,7,1]])
# C1 = A * B
# C2 = np.multiply(A,B)
# print("使用*得到的结果：C1=\n",C1)
# print("使用np.multiply得到的结果：C2=\n",C2)

#以下对matix型
# A = np.asmatrix([[1,2,3],[4,5,6]])
# B = np.asmatrix([[1,2],[3,4],[5,6]])
# C = np.asmatrix([[3,2,3],[5,4,6]])
# D1 = np.dot(A,B)
# D2 = A * B
# E = np.multiply(A,C)
# print("用np.dot()函数实现矩阵乘法：\n",D1)
# print("用*实现矩阵乘法：\n",D2)
# print("用np.multiply()函数实现AC对应元素相乘：\n",E)
