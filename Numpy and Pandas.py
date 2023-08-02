#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


simple_list = [6,7,9]
np.array(simple_list)


# In[4]:


arr = np.array([1,2,3])
arr


# In[5]:


list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
np.array(list_of_lists)


# In[8]:


np.arange(5,10)


# In[9]:


np.arange(1,100)


# In[10]:


np.arange(1,31,5)


# In[11]:


np.arange(5)


# In[12]:


np.zeros(10)


# In[13]:


np.zeros(10,int)


# In[16]:


np.ones((2,3))


# In[17]:


np.ones(100)


# In[18]:


np.ones(10,int)


# In[19]:


np.zeros((2,5),int)


# In[20]:


np.ones((2,5))


# In[21]:


np.ones((2,5),int)


# In[22]:


np.linspace(0,2,5)


# In[23]:


np.linspace(0,20,8)


# In[24]:


np.eye((10))


# In[25]:


np.random.rand(3,5)


# In[26]:


np.random.randn(2,5)


# In[28]:


np.random.randint(2,100)


# In[29]:


np.random.randint(20,100,50)


# In[30]:


arr = np.random.randint(20,40,10)
arr


# In[31]:


np.arange(30)


# In[34]:


a = np.eye(5)
a


# In[35]:


a.T


# In[36]:


a = np.random.rand(2,3)
a


# In[37]:


a.T


# In[38]:


arr = np.arange(10,21)
arr


# In[39]:


arr[2]


# In[40]:


arr[2:5]


# In[41]:


arr[1:4]


# In[42]:


arr[0:7]


# In[43]:


arr[1:4] = 100
arr


# ### Two-Dimensional Array 

# In[47]:


import numpy as np


# In[50]:


arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr


# In[52]:


arr[1,2]


# In[53]:


arr[2,:]


# In[54]:


arr[2]


# In[58]:


arr[:,(2,2)]


# In[59]:


arr[(2,2),:]


# In[ ]:




