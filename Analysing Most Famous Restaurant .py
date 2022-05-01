#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 


# i.) Ration between Restaurant that provides tools and do not tools

# In[8]:


dataset=pd.read_csv("/storage/emulated/0/bluetooth/Gruby Eats.csv",encoding='ISO-8859-1')


# In[9]:


df=dataset


# In[10]:


df.head()


# In[5]:


df['Has Table booking'].value_counts()


# In[6]:


x=df['Has Table booking'].value_counts() 
x


# In[7]:


labels=['not book','book']


# In[8]:


get_ipython().system(' pip install plotly ')
import plotly.express as px


# In[9]:


import plotly.graph_objs as go 
from plotly.offline import iplot


# In[10]:


trace=go.Pie(labels=labels,values=x,hoverinfo='label + percent',textinfo='value')
iplot([trace])


# ii.)Indepth Analysis of Types of Restaurant we have

# In[42]:


df['restuarant_type']=df['Cuisines']


# In[43]:


df['restuarant_type'].isna().sum()


# In[44]:


df['restuarant_type'].dropna(inplace=True)


# In[45]:


df = df.dropna(how='any')           # assign back
df.dropna(how='any', inplace=True)  # set inplace parameter


# In[46]:


df['restuarant_type'].isna().sum()


# In[47]:


len(df['restuarant_type'].unique())


# In[18]:


trace1=go.Bar(x=df['restuarant_type'].value_counts().nlargest(20).index,
              y=df['restuarant_type'].value_counts().nlargest(20).index 
              )


# In[19]:


iplot([trace1])


# iii.) Highest Voted Restuarant

# In[20]:


trace1=go.Bar(x=df.groupby('Restaurant Name')['Votes'].sum().nlargest(20).index,
              y=df.groupby('Restaurant Name')['Votes'].sum().nlargest(20))


# In[21]:


iplot([trace1])


# iv.)Total restaurant at different locations of 

# In[11]:


Restaurant=df['Country Code'].value_counts()
Restaurant


# In[13]:


Restaurant=[]
City=[]
for key, City_df in df.groupby('City'):
    City.append(key)
    Restaurant.append(len(City_df['Restaurant Name'].unique()))


# In[16]:


df_total=pd.DataFrame(zip(City, Restaurant))
df_total.columns=['City','Restaurant']
df_total.head(200)

