#!/usr/bin/env python
# coding: utf-8

# In[5]:


### 5 ###
s1 = 'Nice to have it '
s2 = 'here'
a= [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.append(s1+s2)
print(a)
a.insert(0,s1+s2)
print(a)


# In[8]:


### 4 ###
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])


# In[9]:


s1 = 'Nice to have it '
s2 = 'here'
print(s1+s2)


# In[21]:


### 6 ###
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
for i in range(len(numbers)):
    if (i<=21):
        if (numbers[i]%2==0):
            print(numbers[i])


# In[22]:


### 7 ###
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)


# In[23]:


### 8 ###
c= input("enter a string")
d= c[::-1]
if c==d:
    print(c, " is pangram.")
else:
        print(c, " is not pangam.")
        


# In[24]:


### 9 ###

a= input("Enter a integer")
print(int(a)+int(a*2)+int(a*3))


# In[25]:


### 10 ###
m= input(" enter something in the form of ____#_____.  ")
print(f.split( '#'))


# In[ ]:


without,hello,bag,world

