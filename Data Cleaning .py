#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 




# In[3]:


dataset=pd.read_csv("/storage/emulated/0/bluetooth/Gruby Eats.csv", encoding='ISO-8859-1')


# In[4]:


df=dataset


# In[5]:


df.head()


# In[6]:


df.columns


# In[7]:


df.dtypes


# In[8]:


df.shape


# In[16]:


df.isnull().sum()


# In[19]:


feature_na=[feature for feature in df.columns if df[feature].isnull().sum()>0]


# In[22]:


for feature in feature_na: 
    print('{}has{}missing values'.format(feature,df[feature].isnull().sum()/len(df)*100))


# In[28]:


for feature in feature_na:
    print('{}has{}missing values'.format(feature,np.around(df[feature].isnull().sum()/len(df)*100),4))

