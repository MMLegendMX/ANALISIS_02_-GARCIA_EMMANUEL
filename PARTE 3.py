#!/usr/bin/env python
# coding: utf-8

# # Medio de transporte utilizado.
# 
# ¿Cuáles son los 3 medios de transporte 
# más importantes para Synergy logistics considerando el valor de las 
# importaciones y exportaciones? ¿Cuál es medio de transporte que podrían 
# reducir?

# In[2]:


import pandas as pd

fileLocation = 'data/'
fileName = 'synergy_logistics_database.csv'

synergyDB = pd.read_csv(fileLocation + fileName, index_col='register_id', parse_dates=['date'])
# synergyDB['date'] = pd.to_datetime(synergyDB['date'])
synergyDB['month'] = synergyDB['date'].dt.month
synergyDB


# In[4]:


conteoTransporte = synergyDB['transport_mode'].value_counts()


# In[3]:


import seaborn as sns


# In[12]:


sns.barplot(data=conteoTransporte, x=conteoTransporte.index, y=conteoTransporte.values)


# In[4]:


anualValue = synergyDB.groupby(['year', 'month', 'transport_mode']).count()
anualValue
# anualCount = synergyDB.groupby(['year', 'transport_mode']).count()


# In[7]:


sns.set_theme(style="whitegrid")
sns.set(rc={"figure.figsize": (15, 6)})  #width=15, height=6
sns.lineplot(data=anualValue.reset_index(), x='year', y='origin', hue='transport_mode')


# In[45]:


anualValue.reset_index()


# In[ ]:




