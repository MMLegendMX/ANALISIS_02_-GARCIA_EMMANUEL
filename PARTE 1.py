#!/usr/bin/env python
# coding: utf-8

# # DATA FORCE
# 
# Synergy logistics está 
# considerando la posibilidad de enfocar sus esfuerzos en las 10 rutas más 
# demandadas. Acorde a los flujos de importación y exportación, ¿cuáles son esas 
# 10 rutas? ¿le conviene implementar esa estrategia? ¿porqué? 
# 

# In[1]:


# necesitamos los datos en un dataframe
import pandas as pd

fileLocation = 'data/'
fileName = 'synergy_logistics_database.csv'

synergyDB = pd.read_csv(fileLocation+fileName, index_col='register_id')
synergyDB


# Definimos una ruta, como la combinacion de `direction`, `origin`, `destination`, `transport_mode`

# In[6]:


rutasUnicasDF = synergyDB[['direction', 'origin', 'destination', 'transport_mode', 'total_value']]
rutasUnicasDF


# In[14]:


rutasConteoDF = rutasUnicasDF.groupby(['direction', 'origin', 'destination', 'transport_mode']).count()
rutasConteoDF


# Voy a ordenarla

# In[18]:


rutasConteoDF = rutasConteoDF.sort_values(by='total_value', ascending=False)
rutasConteoDF.head(10)


# ## Separarlos por exports e imports
# 
# Usando `xs`

# In[24]:


top10exp = rutasConteoDF.xs('Exports').head(10)
top10imp = rutasConteoDF.xs('Imports').head(10)
top10exp


# # Crear columna 

# In[25]:


top10exp['nombre'] = top10exp.index.to_list()
top10exp


# In[28]:


def cambiar_nombre(lista):
    nombreNuevo = f'{lista[0]} - {lista[1]}\n{lista[2]}'
    return nombreNuevo

top10exp['nombre'] = top10exp['nombre'].apply(cambiar_nombre)
top10exp


# # Graficar

# In[22]:


import seaborn as sns


# In[32]:


top10exp = top10exp.rename(columns={'total_value' : 'conteo'})
sns.set(rc={"figure.figsize": (18, 6)})  #width=18, height=6
sns.barplot(data=top10exp, x='nombre', y='conteo')


# In[ ]:




