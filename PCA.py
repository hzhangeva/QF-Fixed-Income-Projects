#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import math
from sklearn.decomposition import PCA


# In[3]:


df=pd.read_csv('/Users/shuying/Desktop/FRB_H15.csv')


# In[4]:


df['Date']=pd.to_datetime(df['Date'])
df.set_index(df['Date'],inplace=True)
df.drop(columns=['Date'],inplace=True)
df.dropna(inplace=True)


# In[5]:


df_pre=df[:"2008-12-31"].copy() #before crisis
df_after=df["2009-01-01":].copy() #after crisis


# In[6]:


pca=PCA(n_components=3)
pca.fit(df_pre)


# In[7]:


pca.explained_variance_ratio_


# In[8]:


pca=PCA(n_components=3)
pca.fit(df_after)


# In[9]:


pca.explained_variance_ratio_


# In[ ]:




