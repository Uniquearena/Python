#!/usr/bin/env python
# coding: utf-8

# ## **Cardio Good Fitness Case Study - Descriptive Statistics**

# The market research team at AdRight is assigned the task to identify the profile of the typical customer for each tredmill product offered by CardioGood Fitness. The market research team decides to investigate whether there are differences across the product lines with respect to customer characteristics. The team decides to collect data on indivisuals who purchased a tredmill at a CardioGoodFitness retail store during the prior three months. The data are stored in the CardioGoodFitness.csvfile.

#     the team identifies the following customer variables to study: product purchased,TM195, TM498 or TM798; gender; age,in years; education,in years; relationship status,single or partnered; annual household income ; average number of times the customer plans to use the tredmill each week; average number of miles the customer expects to walk/run each week; and self-rated ftness on an 1-to-5 scale,where 1 is poor shape and 5 is excellent shape

# In[3]:


## import libraries and packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


## load the dataset
df = pd.read_csv("CardioGoodFitness-1.csv")


# In[5]:


df.head()


# In[7]:


df.shape


# ## there are 180 rows and 9 columns

# In[8]:


df.dtypes


# In[9]:


df.info()


# In[10]:


df.isnull().sum()


# In[11]:


df.describe(include="all")


# In[14]:


df.hist(figsize=(10,10))
plt.show()


# In[15]:


sns.countplot(x="Product",data = df)


# In[16]:


sns.countplot(x="Gender",data = df)


# In[17]:


sns.countplot(x="MaritalStatus",data = df)


# In[18]:


sns.countplot(x="Product",hue = "Gender",data = df)


# In[19]:


sns.countplot(x="Product",hue = "MaritalStatus",data = df)


# In[20]:


sns.boxplot(x="Age",data = df)


# In[21]:


iqr = 33-24
iqr


# In[22]:


24-1.5*9


# In[23]:


33+1.5*9


# In[24]:


sns.boxplot(df)


# In[27]:


sns.boxplot(x="Age",data = df,palette = "Set3")


# In[33]:


sns.boxplot(x="Income",data = df,palette="Set1")


# In[34]:


sns.boxplot(x="Product",y="Age",data = df)


# In[35]:


sns.boxplot(x="Product",y="Income",data = df)


# In[36]:


sns.pairplot(df)


# In[38]:


corr = df.corr()
corr


# In[39]:


sns.heatmap(corr,annot = True)


# In[ ]:




