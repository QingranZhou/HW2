#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Create matrix A with size (3,5) containing random numbers.
import numpy as np
A=np.random.randint(0,100,(3, 5))
print(A)


# In[25]:


#Find the size of matrix A.
A.size


# In[26]:


#Find the length of matrix A.
len(A)


# In[27]:


#Resize (crop/slice) matrix A to size (3,4).
A.resize((3, 4))
print(A)


# In[33]:


#Find the transpose of matrix A and assign it to B.
B=A.transpose()
print(B)


# In[37]:


#Find the minimum value in column 1 of matrix B.
B[::,0:1:].min()


# In[38]:


#Find the minimum values for the entire matrix A.
A.min()


# In[39]:


#Find the maximum values for the entire matrix A.
A.max()


# In[57]:


#Create vector X (an array) with 4 random numbers.
X=np.random.randint(0,100,4)
print(X)


# In[56]:


#Create a function and pass vector X and matrix A in it.
#In the new function multiply vector X with matrix A and assign the result to D.
def f(X,A):
    return np.dot(A,X.T)
D=f(X,A)
print(D)


# In[72]:


#Create a complex number Z with absolute and real parts != 0.
Z=5+12j
Z


# In[73]:


#Show its real part.
Z.real


# In[74]:


#Show its imaginary part.
Z.imag


# In[75]:


#Show its absolute value.
abs(Z)


# In[77]:


#Multiply result D with the absolute value of Z and record it to C.
C=D*abs(Z)
print(C)


# In[81]:


#Convert matrix B from a matrix to a string and overwrite B.
str(B)


# In[104]:


#Display a text on the screen: ‘Name is done with HW2‘, but pass your ‘Name’ as a string variable.
s='Qingran Zhou'
print("%s is done with HW2."%(s))

