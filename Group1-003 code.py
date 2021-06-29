#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv('C:/Users/pavan/Downloads/DataScientist.csv (1)/DataScientist.csv')


# In[2]:


df.head(5)


# In[3]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


pip install missingno


# In[5]:


import missingno as msno


# In[6]:


ax = msno.bar(df, color="Red", figsize=(12,7), fontsize=14)
ax.set_title("Plot for displaying null values",color ="Darkorange" ,fontsize = 24,loc = "Left")
plt.xlabel("Total number of non-null values within resective column",fontsize=16,color = "Green")
plt.ylabel("Number of rows", fontsize=19,color = "Blue")


# In[7]:


corr = df.corr()

ax = sns.heatmap(
corr,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(20, 220, n=200),
square=True
)
ax.set_xticklabels(
ax.get_xticklabels(),
rotation=45,
horizontalalignment='right'
);
ax.set_title("Plot for displaying correlation between various columns",color ="DarkBlue" ,fontsize = 22)
plt.xlabel("Column Names",fontsize=17,color = "GREEN")


# In[8]:


ax = sns.countplot(y ='Sector', data = df)
ax.set_title("Company Count in different Sector", fontsize = 20,color ="Darkred")
plt.xlabel("Count",fontsize=19,color = "Blue")
plt.ylabel("Sector", fontsize=19,color = "Blue")
plt.show()


# In[9]:


msno.dendrogram(df)


# In[10]:


sns.countplot(x='Rating', data = df)
plt.show()


# In[11]:


sns.countplot(x='Easy Apply', data = df)
plt.show()


# In[12]:


sns.countplot(y='Type of ownership', data = df)
plt.show()


# In[ ]:




