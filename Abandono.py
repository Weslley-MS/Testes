#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


files = pd.read_json(r"input\page-views.json")


# In[3]:


df = pd.DataFrame(files)


# In[154]:


for i in df["customer"].unique():
    p1 = df[df["customer"]==i]["timestamp"].max()
    p2 = df[(df["customer"]==i) & (df["timestamp"]!=p1)]["timestamp"].max()
    status = df[(df["timestamp"]==p1) & (df["customer"]==i)].set_index("page")
    dif = (p1-p2).total_seconds()
    if (dif > 600) | (bool(status.index != "checkout")):
        df_abandono = df[df["timestamp"]==p1]


# In[162]:


df_abandono.to_json(r"output\abandoned-carts.json",orient="records")

