#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


sample_array = np.arange(1,20)
sample_array


# In[3]:


sample_array+sample_array


# In[4]:


np.exp(sample_array)


# In[5]:


np.sqrt(sample_array)


# In[6]:


np.log(sample_array)


# In[7]:


np.max(sample_array)


# In[8]:


np.min(sample_array)


# In[9]:


np.argmax(sample_array)


# In[10]:


np.argmin(sample_array)


# In[11]:


np.square(sample_array)


# In[12]:


np.std(sample_array)


# In[13]:


np.var(sample_array)


# In[14]:


np.mean(sample_array)


# In[16]:


array =np.random.randn(3,4)
array


# In[18]:


np.round(array,decimals=3)


# In[21]:


sports = np.array(['golf','cricket','fball','cricket'])
np.unique(sports)


# ### Pandas

# In[23]:


import pandas as pd
import numpy as np


# In[26]:


sports1 = pd.Series([1,2,3,4],index = ['cricket','fball','baseball','golf'])
sports1


# In[27]:


sports1['fball']


# In[28]:


sports2 = pd.Series([1,2,3,4],index = ['cricket','fball','baseball','golf'])
sports2


# In[29]:


sports1+sports2


# In[30]:


import pandas as pd
import numpy as np


# In[32]:


df1 = pd.DataFrame(np.random.rand(8,5),index = 'A B C D E F G H'.split(),columns = 'Score1 Score2 Score3 Score4 Score5'.split())
df1


# In[33]:


df1['Score1']


# In[51]:


df1['Score6'] = df1['Score1'] + df1['Score2']
df1


# In[45]:


df2 = {'ID':['101','102','103','107','176'],'Name':['john','akash','ansh','anshuman','kevin'],'Profit':[20,54,56,87,123]}
df2= pd.DataFrame(df2)
df2


# In[47]:


df2['ID']


# In[52]:


df2.drop(3)


# In[ ]:




