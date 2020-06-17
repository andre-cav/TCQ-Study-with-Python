#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
dados = pd.read_csv('Andre Gomes Prado Cavalcanti - Dados1.csv', delimiter =';',decimal=',')


# In[4]:


media= dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].mean(axis=1)
desvio=dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].std(axis=1)
maximo=dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].max(axis=1)
minimo=dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].min(axis=1)
amplitude=maximo-minimo


# In[5]:


dados.insert(loc=7,column='Média', value=media)
dados.insert(loc=8,column='Amplitude', value=amplitude)
dados.insert(loc=9,column='Desvio Padrão', value=desvio)
dados


# In[ ]:




