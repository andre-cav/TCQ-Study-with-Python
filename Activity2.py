#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from matplotlib import pyplot as plt


# In[2]:


Tk().withdraw()
arquivo = askopenfilename()
dados = pd.read_csv(arquivo, delimiter =';',decimal=',')


# In[3]:


media= dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].mean(axis=1)
desvio=dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].std(axis=1)
maximo=dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].max(axis=1)
minimo=dados[["Obs1","Obs2","Obs3","Obs4","Obs5","Obs6"]].min(axis=1)
amplitude=maximo-minimo


# In[4]:


dados.insert(loc=7,column='Média da Amostra', value=media)
dados.insert(loc=8,column='Amplitude', value=amplitude)
dados.insert(loc=9,column='Desvio Padrão', value=desvio)
dados.set_index('Amostra',inplace=True)
dados


# In[5]:


media_geral= dados['Média da Amostra'].mean()
media_dp= dados['Desvio Padrão'].mean()
dados['LM']=media_geral
dados['LSC']=media_geral+(3*media_dp)
dados['LIC']=media_geral-(3*media_dp)


# In[6]:


dados['Média da Amostra'].plot(figsize=(14,6),color='blue')
dados['LM'].plot(color='green',linestyle='--')
dados['LSC'].plot(color='purple',linestyle='--')
dados['LIC'].plot(color='red',linestyle='--')
plt.title('Controle das Amostras')
plt.xlabel('Amostras')
plt.ylabel('Média')
plt.legend(bbox_to_anchor=(1,1),loc=0)
plt.grid(True)
plt.show()

