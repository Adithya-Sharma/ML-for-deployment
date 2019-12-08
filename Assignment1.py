#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 1: Problem 2
x=[]
for i in range(2000,3200):
    if(i%7==0 and i%5!=0):
        x.append(i)
        
print(x)


# In[2]:


#Task 1:Problem 3
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
print(last_name+" "+first_name)


# In[14]:


#Task 1: Problem 4
pi=3.14
diameter=12
v=4/3*pi*(diameter/2)**3
print("The volume of the sphere: ",v)


# In[16]:


#Task 2: Problem 1
numbers=input("enter numbers: ")
list=numbers.split(",")
print("List: ",list)


# In[17]:


#Task 2: Problem 2
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# In[20]:


#Task 2: Problem 3
a=input("Enter a word: ")[::-1]
print(a)


# In[ ]:




