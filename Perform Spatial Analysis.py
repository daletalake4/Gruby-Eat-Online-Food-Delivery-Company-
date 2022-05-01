#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns


# In[2]:


dataset=pd.read_csv('/storage/emulated/0/bluetooth/Gruby Eats.csv',encoding='ISO-8859-1')


# In[3]:


df=dataset


# In[4]:


df.head()


# i.)Total number of Restaurant that have better rating >4& that are affordable

# In[5]:


df.columns


# In[6]:


df[(df['Aggregate rating']>4) & (df['Average Cost for two']<=500)].shape


# In[7]:


len(df[(df['Aggregate rating']>4) & (df['Average Cost for two']<=500)]['Restaurant Name'].unique())


# ii.)Total various affordable hotels at all locations

# In[8]:


df_new=df[(df['Aggregate rating']>4) & (df['Average Cost for two']<=500)]
df_new.head()


# In[9]:


City=[]
total=[]
for loc, City_df in df_new.groupby('City'):
    City.append(loc)
    total.append(len(City_df['Restaurant Name'].unique()))


# In[10]:


City_df=pd.DataFrame(zip(City,total))
City_df.tail()


# In[11]:


City_df.columns=['City','Restaurant']


# In[12]:


City_df.head()


# iii.)Finding Best Restaurant in any location

# In[13]:


def return_budget(City, Restaurant):
    budget=df[(df['Average Cost for two']<=400)
    &(df['City']==City) &(df['Aggregate rating']>4) &(df['Cuisines']==Restaurant)]
    return(budget['Restaurant Name'].unique())


# In[19]:


return_budget('Singapore','Cafe')


# iv.) Which are the foodie areas

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
restaurant_location=df['City'].value_counts()[0:20]
sns.barplot(restaurant_location, restaurant_location.index)
plt.show()


# In[ ]:




