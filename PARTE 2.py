#!/usr/bin/env python
# coding: utf-8

# # Valor total de importaciones y exportaciones.
# 
# Si Synergy Logistics quisiera enfocarse en los países que le generan el 80% del valor de las exportaciones e importaciones **¿en qué grupo de países debería enfocar sus esfuerzos?**
# 

# In[1]:


import pandas as pd

fileLocation = 'data/'
fileName = 'synergy_logistics_database.csv'
synergyDB = pd.read_csv(fileLocation + fileName, index_col='register_id')
synergyDB


# In[2]:


agrupadosPorPais = synergyDB[['direction', 'origin', 'total_value']].groupby(['direction', 'origin']).sum()
agrupadosPorPais.sort_values(by=['total_value'], inplace=True, ascending=False)
agrupadosPorPais


# In[3]:


exportaciones = agrupadosPorPais.xs('Exports')
importaciones = agrupadosPorPais.xs('Imports')


# In[4]:


exportaciones['porcentaje_acumulado'] = 100 * ( exportaciones.total_value.cumsum() / exportaciones.total_value.sum())
exportaciones


# In[5]:


topExportaciones = exportaciones[exportaciones['porcentaje_acumulado'] < 85]
topExportaciones


# In[ ]:




