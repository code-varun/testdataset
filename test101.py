#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd 
df = pd.read_csv(r"C:\Users\osco\Documents\testdataset.csv")
df


# In[17]:


new_df = df.fillna(0)
new_df


# In[ ]:




