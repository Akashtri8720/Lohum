#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn
get_ipython().run_line_magic('matplotlib', 'inline')


# Reading a Json File 

# In[3]:


data=pd.read_json("CRS-16.json",lines=True)


# Exploratary Data Analysis Of Dataset

# In[4]:


data.info()


# In[7]:


data


# In[5]:


data.head(10)


# In[6]:


data.describe()


# In[8]:


data.columns


# Plotting Graph's for understading insights and Relationship between their Different Coloumns.

# In[9]:


sns.distplot(data['time'],bins=10,kde=False,color='blue')


# In[10]:


sns.distplot(data['velocity'],bins=10,kde=False,color='blue')


# In[11]:


sns.distplot(data['altitude'],bins=10,kde=False,color='blue')


# In[12]:


sns.jointplot(x='time',y='velocity',data=data,kind = "reg")


# In[13]:


sns.jointplot(x='time',y='altitude',data=data,kind = "reg")


# In[14]:


sns.jointplot(x='altitude',y='velocity',data=data,kind = "reg")


# In[15]:


data.corr()

The output above shows presence of strong linear correlation between the variables time and velocity and between altitude and time.
# In[18]:


data['altitude'].value_counts(normalize= True)


# In[17]:


data['velocity'].value_counts().value_counts()


# In[16]:


df = data[['time','velocity','altitude']]

sns.pairplot(df, kind="scatter")


# In[30]:


sns.pairplot(x_vars=['time'], y_vars=['velocity','altitude'], data=data,kind='reg')


# In[19]:


data['time'].value_counts().value_counts(normalize=True)


# In[20]:


sns.heatmap(data.corr(),cmap='coolwarm')


# # Calculate and Plot acceleration profile of the spacecraft.
# With the timestamp and velocity data, calculate acceleration profile

# In[21]:


# as we know acceleration is defined as the rate of change of velocity with respect of time,So caluclating the acceleration by using time and velocity columns
data['acceleration']=(data['velocity']-data['velocity'].shift(1))/(data['time']-data['time'].shift(1))
data


# In[22]:


sns.jointplot(x='acceleration',y='velocity',data=data,kind = "reg")


# In[23]:


sns.jointplot(x='time',y='acceleration',data=data,kind = "reg")


# In[36]:


sns.pairplot(x_vars=['time'], y_vars=['acceleration'], data=data,kind='reg')


# #rate of change of altitude with respect of time

# In[24]:


# Rate of change of Altitude is Represented as ,
# rate of change of altitude = Δ(Altitude)/time
data['rate of change of altitude']=(data['altitude']-data['altitude'].shift(1))/(data['time'])
data


# In[25]:


data['rate of change of altitude'].value_counts(normalize= True)


# In[29]:


data.columns


# In[50]:


sns.pairplot(x_vars=['time'], y_vars=['rate of change of altitude'], data=data,kind='reg')
sns.pairplot(x_vars=['time'], y_vars=['velocity'], data=data,kind='reg')

Que:-Calculate rate of change of altitude with respect to time. Is it the same as velocity?
Why and why not - justify your answer with appropriate graphs
Ans- As shown in graphs upside the rate of change of velocity is not related to Time in 1st case But in 2nd case the velocity
is nearly in uniform motion with time which states that velocity is related to Time.Thank You,