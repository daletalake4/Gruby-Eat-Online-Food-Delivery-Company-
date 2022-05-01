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


df.tail(20)


# In[5]:


location=pd.DataFrame({'Name':df['City'].unique()})
location.head(30)


# In[6]:


import geopy.geocoders


# In[7]:


import geopy.geocoders as geocoders


# In[8]:


from geopy.geocoders import Nominatim


# In[9]:


geolocator=Nominatim(user_agent='app')


# In[10]:


df.columns


# In[11]:


lat_lon=[]
for City in location['Name']:
    City=geolocator.geocode(City)
    if City is None:
        lat_lon.append(np.nan)
    else:
            geo=(City.latitude,City.longitude)
            lat_lon.append(geo)


# In[12]:


location['geo_loc']=lat_lon


# In[13]:


location.head()


# In[14]:


location.shape


# In[15]:


Rest_locations=pd.DataFrame(df['City'].value_counts().reset_index())
Rest_locations.head()


# In[16]:


Rest_locations.columns=['Name','Count']
Rest_locations.head()


# In[17]:


Restaurant_locations=Rest_locations.merge(location,on='Name',how='left').dropna()
Restaurant_locations.head()


# In[18]:


np.array(Restaurant_locations['geo_loc'])


# In[19]:


lat,lon=zip(*np.array(Restaurant_locations['geo_loc']))


# In[20]:


type(lat)


# In[21]:


Restaurant_locations['lat']=lat 
Restaurant_locations['lon']=lon


# In[22]:


Restaurant_locations.head()


# In[23]:


Restaurant_locations.drop('geo_loc',axis=1,inplace=True)


# In[24]:


Restaurant_locations.head()


# In[25]:


import folium


# In[26]:


from folium.plugins import HeatMap


# In[27]:


def generatebasemap(default_location=[12.97,77.59],default_zoom_start=12):
    basemap=folium.Map(location=default_location,zoom_start=default_zoom_start)
    return basemap


# In[28]:


basemap=generatebasemap()


# In[29]:


get_ipython().run_line_magic('matplotlib', 'inline')
basemap 

