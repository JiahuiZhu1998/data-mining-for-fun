#############################################################
# from http://cs231n.github.io/python-numpy-tutorial/
# from https://www.jianshu.com/p/743b3bb340f6
# from https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
# from https://blog.csdn.net/u011475210/article/details/77770751
# from https://blog.csdn.net/dongtingzhizi/article/details/12068205
# This also include some matplotlib and scipy
# 布尔索引 与 花式索引
# how to use tail function in numpy****
# how to use argsort()
# how to use operator.itemgetter() and sorted
# how to use .get function in dictionary
# how to use mat in numpy, Show to use multiply() in numpy
# from https://blog.csdn.net/zenghaitao0128/article/details/78715140
# from https://blog.csdn.net/leo_sheng/article/details/80741789
############################################################

import numpy as np
import os
import sys
from scipy.misc import imread, imsave, imresize
import imageio
import matplotlib.pyplot as plt
from numpy import *
import operator


a = np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0] = 5
print(a)

b = np.array([ [1,2,3],[4,5,6] ] )
print(type(b))
print(b.shape)
print(b[0,0], b[0,1],b[0,2],b[1,0],b[1,1],b[1,2])

a1 = np.zeros((2,2))
print(a1)
b1 = np.ones((1,2))
print(b1)
c1 = np.full((2,2),7)
print(c1)
d1 = np.eye(2)## which is identity matrix
print(d1)
e1 = np.random.random((2,2))  ## create an array full of random values
print(e1)



#about array indexing
a2 = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
print(a2)

#### b2 is consisting of the first two rows and columns 1 &2  the starting index of row or column is 0 the 1 represent the second row
b2 = a2[:2,1:3]
print(b2)
print(a2[0,1]) ## this code want the terminal to show the second element in the first row which is 2

b2[0,0]=77
print(a2)    ## these two codes change the first element in b which is (1,2) element in a
print(a2[0,1])


a3 = np.array([ [1,2,3,4],[5,6,7,8],[9,10,11,12] ] )
print(a3)
row_r1 = a3[1,:] ## the first way to show the second row but the shape is not totally same
print(row_r1,row_r1.shape)
row_r2 = a3[1:2,:]  ## the second way to show the second row but the shape is not totally same
print(row_r2,row_r2.shape)

############# Integer Array Indexing
a4 = np.array([[1,2], [3, 4], [5, 6]])
print(a4)

print(a4[[0, 1, 2], [0, 1, 0]]) ## this represent from row0 to row2, choose the element0, element1, element0 respectively
print(np.array( [ a4[0,0],a4[1,1],a4[2,0] ] ) ) ## this represent new array consist of (0,0),(1,1） and（2,0）
print(a4[[0,0],[1,1]]) ## this represent the element(0,1) and two appearance of this element consist a new array
print(a4[[2,2],[1,1]]) ## this represent the element(2,1) and two appearance of this element consist a new array
print(np.array([a4[0,1],a4[0,1]])) ## this represent the element(0,1) and two appearance of this element consist a new array

a5 = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
#print(a5)
b5 = np.array([0,2,0,1])
#print(b5)
print(a5[np.arange(4),b5])## select an element from each row and the index is from b5. Also the number of rows is 4
a5[np.arange(4),b5]+=10 ## the index[1,6,7,11] will be incremented by 10 the first element is 1, the sixth is 6, the seventh is 7,etc
print(a5)


##############################

##Boolean Array Indexing
a6 = np.array([[1,2], [3, 4], [5, 6]])
print(a6)
bool_idx = (a6>2)
print(bool_idx)
print(a6[bool_idx])## this only take the elements that show true in boolean operation and consist a new array
print(a6[a6>2]) ## this is same as line above
####################################

## data types
x1 = np.array([1, 2])
print(x1.dtype)
x2 = np.array([1.0,2.0])
print(x2.dtype)
x3 = np.array([1,2],dtype = np.int64)
print(x3.dtype)

####Array math
x4 = np.array([[1,2],[3,4]],dtype = np.float64)
y4 = np.array([[5,6],[7,8]],dtype = np.float64)
v1 = np.array([9,10])
w1 = np.array([11,12])
print(x4+y4)
print(np.add(x4,y4)) ## which is same as above
print(x4-y4)
print(np.subtract(x4,y4))
print(x4*y4)
print(np.multiply(x4,y4))
print(x4/y4)
print(np.divide(x4,y4))

print(np.sqrt(x4))

###########
print(v1.dot(w1))  ## 9*11+10*12
print(np.dot(v1,w1)) ## 9*11+10*12
print(x4.dot(v1))
print(np.dot(x4,v1))
print(x4.dot(y4))
print(np.dot(x4,y4))

print(np.sum(x4))  ## 1+2+3+4 = 10
print(np.sum(x4,axis=0)) ## compute the sum of each column
print(np.sum(x4,axis=1)) ## compute the sum of each row

print(x4.T)  ## transpose of x4

## IMPORTANT: Note that taking the transpose of a rank 1 array does nothing
v2 = np.array([1,2,3])
print(v2)
print(v2.T) # these two are same which is wrong in math

##Broadcasting
x5= np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v5= np.array([1, 0, 1])
y5 =np.empty_like(x5) # Create an empty matrix with the same shape as x
print(y5) ## y is truly zero matrix... even though the terminal does not show correctly
for i in range(4):
    y5[i, :] = x5[i, :] + v5
print(y5)

vv1 = np.tile(v5, (4, 1))
print(vv1) # four v1 creates a new array vv1
y5 = x5 + vv1
print(y5)  # the result is same as the for loop
y5= x5+v5 ## add the v to each row of x
print(y5)
##
v6 = np.array([1,2,3])  # v has shape (3,)
w6 = np.array([4,5])    # w has shape (2,)
print(np.reshape(v6, (3, 1)) * w6) ## [1,2,3].T * [4,5] is equal to [4,5],[8,10],[12,15]

x6 = np.array([[1,2,3], [4,5,6]])
print(x6+v6) #add v6 to each row of x6
print((x6.T + w6).T) ## add v6 ti each row of x6.T
print(x6 + np.reshape(w6, (2, 1)))  ## [4,5].T + each column of x6 get [5,6,7],[9,10,11]
print(x6 * 2)
#################

###### SCipy####
# img = imageio.imread('C:/Users/garry/Documents/data-mining-for-fun/003. numpy code intro/cat.jpg')
# print(img)
# arrayIMG = np.array(img)
# #print(arrayIMG.dtype.arrayIMG.shape) --> this line cause error
#
# img_tinted = arrayIMG * [1,0.95, 0.9]
# img_tinted = imresize(img_tinted, (300,300))
# #
# #imsave('C:/Users/garry/Documents/data-mining-for-fun/003. numpy code intro/cat_tinted.jpg',img_tinted)
###IMPORTANT： SCIPY PART will cause warning

#matlab files
##Distance between points
from scipy.spatial.distance import pdist, squareform
x8 = np.array( [ [0,1],[1,0],[2,0] ] )
print(x8)

d8 = squareform(pdist(x8,'euclidean'))
print(d8)

#Using matplotlib
x9 = np.arange(0,3*np.pi,0.1)
y9 = np.sin(x9)
y10 = np.cos(x9)
# plt.plot(x9,y9)
# plt.plot(x9,y10)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title(['Sine', 'Cosine'])
# plt.show()

plt.subplot(2,1,1)
plt.plot(x9,y9)
plt.title('Sine')

plt.subplot(2,1,2)
plt.plot(x9,y10)
plt.title('Cosine')
plt.show()

## Image (this part cause some errors

# img2 = imread('C:/Users/garry/Documents/data-mining-for-fun/003. numpy code intro/cat.jpg')
# img_tinted = img2 * [1,0.95,0.9]
# plt.subplot(1,2,1)
# plt.imshow(img2)
# plt.subplot(1,2,2)
# plt.imshow(np.unit8(img_tinted))
# plt.show()

### creating a 7*4 array
arr1 = np.arange(28).reshape((7,4))
print(arr1)
print('\n')
booling1 = np.array([True,False,False,True,True,False,False])
print(arr1[booling1])## the first row, the fourth row , the fifth row

#another example
names = np.array(['Ben','Tom','Ben','Jeremy','Jason','Michael','Ben'])
print('\n')
print(names=='Ben')
print('\n')
print(arr1[names=='Ben'])
print('\n')
print(arr1[names =='Ben',3]) #which the column index is 3 so the answer is [3 11 27]
print('\n')
print(arr1[names=='Ben',1:4]) # which the column index is 1:4 so the answer is [1 2 3] [9 10 11] [25 26 27]
print('\n')
print(arr1[names!='Ben'])# showing rows which does not contain ben
print('\n')
print(arr1[~(names=='Ben')]) # also showing rows which does not contain ben
print('\n')
print(arr1[(names=='Jason')|(names=='Tom')]) #showing rows which contain jason or contain tom
print('\n')
arr1[(names=='Jason')|(names=='Tom')]=0; ## clear rows which contain jason or contain tom
print(arr1)
print('\n')
print(arr1[arr1>15]) ## pick up all elements which is bigger than 15 and group them to become a new array
print('\n')
arr1[arr1<=15]=0;
print(arr1)
print('\n') ## replace all elements by 0 which is smaller than or equal to 15
print()

###### new chapter: Fancy Indexing花式索引
arr2 = np.array(['zero','one','two','three','four'])
print(arr2[[1,4]])## print the second element and the fifth element
arr3 = np.empty((8,4),dtype=np.int)
for i in range(8):
    arr3[i]=i;
print(arr3)## fill different number in each row because arr3[i] i represent row and neglect column index
print('\n')
print(arr3[[4,3,0,6]])
print('\n')
print(arr3[[-3,-5,-7]])##negtive index

arr4 = np.arange(42).reshape(6,7)
print('\n')
print(arr4)
print('\n')
print(arr4[[1,3,5],[2,4,6]])#### [1,3,5] represents row and [2,4,6] represents column
# so the result is [9 25 41]

### relationship between boolean indexing and fancy indexing
arr5 = np.arange(12).reshape(3,4)
i = np.array([True,False,True])
j = np.array([True,True,False,False])
print('\n')
print(i.nonzero()) ## which is the first element and the third element which is array[0,2]
print('\n')
print(arr5[i])
print('\n')
print(arr5[i.nonzero()]) ## because i only show true and the first row and the third row is true which is 1. so the nonzero is the same meaning of i
print('\n')

print(i)
print('\n')
print(j)
print('\n')
print(i.nonzero())
print(j.nonzero())
#### these three lines above
print(arr5[i,j])
print(arr5[i.nonzero(),j.nonzero()])
print(arr5[[0,2],[0,1]]) ## the element (1,1) and(2,2) are 0 and 9 and these two elements consist a new list or an array

### use tile function in python
arr555 = [1,2,3]
arr556 = tile(arr555,3)
print(arr556)
print('\n')

### use argsort() function in numpy
arr557 = np.array([1,2,3])
print(np.argsort(arr557))
print('\n')
arr557_2 = np.array([[2,3,5],[5,7,9]])
print(np.argsort(arr557_2,axis=0)) ##index by line
print(np.argsort(arr557_2,axis=1)) ##index by column
print(np.argsort(arr557_2))
print(np.argsort(-arr557_2))

### use operator.itemgetter()  arr557 = [1,2,3]
print('\n')
get558 = operator.itemgetter(1)
print(get558(arr557))
get558_2 = operator.itemgetter([0,1])
print(get558_2(arr557))
### use sorted function in detail
students559 = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(sorted(students559, key=lambda student : student[2])) ## sort 15,12,10
###

