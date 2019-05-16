#############################################################
# from http://cs231n.github.io/python-numpy-tutorial/
# from https://www.jianshu.com/p/743b3bb340f6
# from https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
# This also include some matplotlib and scipy
# 布尔索引 与 花式索引
############################################################

import numpy as np
import os
import sys

# a = np.array([1,2,3])
# print(type(a))
# print(a.shape)
# print(a[0],a[1],a[2])
# a[0] = 5
# print(a)
#
# b = np.array([ [1,2,3],[4,5,6] ] )
# print(type(b))
# print(b.shape)
# print(b[0,0], b[0,1],b[0,2],b[1,0],b[1,1],b[1,2])

# a1 = np.zeros((2,2))
# print(a1)
# b1 = np.ones((1,2))
# print(b1)
# c1 = np.full((2,2),7)
# print(c1)
# d1 = np.eye(2)## which is identity matrix
# print(d1)
# e1 = np.random.random((2,2))  ## create an array full of random values
# print(e1)



# #about array indexing
# a2 = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
# print(a2)
#
# #### b2 is consisting of the first two rows and columns 1 &2  the starting index of row or column is 0 the 1 represent the second row
# b2 = a2[:2,1:3]
# print(b2)
# print(a2[0,1]) ## this code want the terminal to show the second element in the first row which is 2
#
# b2[0,0]=77
# print(a2)    ## these two codes change the first element in b which is (1,2) element in a
# print(a2[0,1])


# a3 = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
# print(a3)
# row_r1 = a3[1,:] ## the first way to show the second row but the shape is not totally same
# print(row_r1,row_r1.shape)
# row_r2 = a3[1:2,:]  ## the second way to show the second row but the shape is not totally same
# print(row_r2,row_r2.shape)

# ############# Integer Array Indexing
# a4 = np.array([[1,2], [3, 4], [5, 6]])
# print(a4)
#
# print(a4[[0, 1, 2], [0, 1, 0]]) ## this represent from row0 to row2, choose the element0, element1, element0 respectively
# print(np.array( [ a4[0,0],a4[1,1],a4[2,0] ] ) ) ## this represent new array consist of (0,0),(1,1） and（2,0）
# print(a4[[0,0],[1,1]]) ## this represent the element(0,1) and two appearance of this element consist a new array
# print(a4[[2,2],[1,1]]) ## this represent the element(2,1) and two appearance of this element consist a new array
# print(np.array([a4[0,1],a4[0,1]])) ## this represent the element(0,1) and two appearance of this element consist a new array

# a5 = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# #print(a5)
# b5 = np.array([0,2,0,1])
# #print(b5)
# print(a5[np.arange(4),b5])## select an element from each row and the index is from b5. Also the number of rows is 4
# a5[np.arange(4),b5]+=10 ## the index[1,6,7,11] will be incremented by 10 the first element is 1, the sixth is 6, the seventh is 7,etc
# print(a5)
#
#
# ##############################

# ##Boolean Array Indexing
# a6 = np.array([[1,2], [3, 4], [5, 6]])
# print(a6)
# bool_idx = (a6>2)
# print(bool_idx)
# print(a6[bool_idx])## this only take the elements that show true in boolean operation and consist a new array
# print(a6[a6>2]) ## this is same as line above
# ####################################

### data types
# x1 = np.array([1, 2])
# print(x1.dtype)
# x2 = np.array([1.0,2.0])
# print(x2.dtype)
# x3 = np.array([1,2],dtype = np.int64)
# print(x3.dtype)

#####Array math
# x4 = np.array([[1,2],[3,4]],dtype = np.float64)
# y4 = np.array([[5,6],[7,8]],dtype = np.float64)
# v1 = np.array([9,10])
# w1 = np.array([11,12])
# print(x4+y4)
# print(np.add(x4,y4)) ## which is same as above
# print(x4-y4)
# print(np.subtract(x4,y4))
# print(x4*y4)
# print(np.multiply(x4,y4))
# print(x4/y4)
# print(np.divide(x4,y4))

# print(np.sqrt(x4))

############
# print(v1.dot(w1))  ## 9*11+10*12
# print(np.dot(v1,w1)) ## 9*11+10*12
# print(x4.dot(v1))
# print(np.dot(x4,v1))
# print(x4.dot(y4))
# print(np.dot(x4,y4))

# print(np.sum(x4))  ## 1+2+3+4 = 10
# print(np.sum(x4,axis=0)) ## compute the sum of each column
# print(np.sum(x4,axis=1)) ## compute the sum of each row
#
# print(x4.T)  ## transpose of x4
#
# ## IMPORTANT: Note that taking the transpose of a rank 1 array does nothing
# v2 = np.array([1,2,3])
# print(v2)
# print(v2.T) # these two are same which is wrong in math

# ##Broadcasting
# x5= np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
# v5= np.array([1, 0, 1])
# y5 =np.empty_like(x5) # Create an empty matrix with the same shape as x
# print(y5) ## y is truly zero matrix... even though the terminal does not show correctly
# for i in range(4):
#     y5[i, :] = x5[i, :] + v5
# print(y5)
#
# vv1 = np.tile(v5, (4, 1))
# print(vv1) # four v1 creates a new array vv1
# y5 = x5 + vv1
# print(y5)  # the result is same as the for loop
# y5= x5+v5 ## add the v to each row of x
# print(y5)
# ##
# v6 = np.array([1,2,3])  # v has shape (3,)
# w6 = np.array([4,5])    # w has shape (2,)
# print(np.reshape(v6, (3, 1)) * w6) ## [1,2,3].T * [4,5] is equal to [4,5],[8,10],[12,15]
#
# x6 = np.array([[1,2,3], [4,5,6]])
# print(x6+v6) #add v6 to each row of x6
# print((x6.T + w6).T) ## add v6 ti each row of x6.T
# print(x6 + np.reshape(w6, (2, 1)))  ## [4,5].T + each column of x6 get [5,6,7],[9,10,11]
# print(x6 * 2)
# #################

###### SCipy####



