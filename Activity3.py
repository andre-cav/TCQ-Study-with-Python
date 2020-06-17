#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from matplotlib import pyplot as plt


# #Importando o arquivo 

# In[2]:


dados = pd.read_csv('Dados2.csv', delimiter =';',decimal=',')
dados.set_index('Amostra',inplace=True)
dados


# In[3]:


tamanho_piloto=dados[:20].size/6
media= dados.mean(axis=1)
desvio=dados.std(axis=1)
desvio_piloto=desvio[:20].mean()
media_piloto=media[:20].mean()


# In[4]:


desvio_amostral=(desvio_piloto/(20)**0.5)


# In[5]:


dados.insert(loc=6,column='Média da Amostra', value=media)
dados.insert(loc=7,column='Desvio Padrão', value=desvio)


# In[6]:


dados


# In[7]:


linha_media=media_piloto
linha_superior=media_piloto+(3*desvio_amostral)
linha_inferior=media_piloto-(3*desvio_amostral)
linha_intermediaria_s=media_piloto+(2*desvio_amostral)
linha_intermediaria_i=media_piloto-(2*desvio_amostral)


# In[8]:


t=0
contador_consec=0
contador_2em3=0

while t<=38:
    
    
    if media.iloc[t]>=linha_superior and media.iloc[t+1]>=linha_superior:
        contador_consec=contador_consec+1          
        
    if media.iloc[t]<=linha_inferior and media.iloc[t+1]<=linha_inferior:        
        contador_consec=contador_consec+1
        
    t=t+1
t=0        
while t<=37:        
    teste=0
    if media.iloc[t]>=linha_superior:
        teste=teste+1    
        
    if media.iloc[t+1]>=linha_superior:
        teste=teste+1    
        
    if media.iloc[t+2]>=linha_superior:
        teste=teste+1
            
        
        
        
    if media.iloc[t]<=linha_inferior:
        teste=teste+1    
        
    if media.iloc[t+1]<=linha_inferior:
        teste=teste+1    
        
    if media.iloc[t+2]<=linha_inferior:
        teste=teste+1
            

        
    if teste >= 2:
        contador_2em3=contador_2em3 + 1
    
    
    t=t+1


# In[9]:


dados.insert(loc=8,column='Linha Média', value=media_piloto)
dados.insert(loc=9,column='LSC', value=linha_superior)
dados.insert(loc=10,column='LIC', value=linha_inferior)


# In[10]:


dados.insert(loc=11,column='LSC 2sigma', value=linha_intermediaria_s)
dados.insert(loc=12,column='LIC 2sigma', value=linha_intermediaria_i)


# In[11]:


dados['Média da Amostra'].plot(figsize=(10,7),color='blue',marker='s')
dados['Linha Média'].plot(color='green',linestyle='--')
dados['LSC'].plot(color='red',linestyle='--')
dados['LIC'].plot(color='red',linestyle='--')
dados['LSC 2sigma'].plot(color='yellow',linestyle='--')
dados['LIC 2sigma'].plot(color='yellow',linestyle='--')
plt.title('Controle das Amostras')
plt.xlabel('Amostras')
plt.ylabel('Média')
plt.legend(bbox_to_anchor=(1,1),loc=0)
plt.grid(True)
plt.savefig('grafico.pdf',format='pdf',transparent=True,dpi=300)
plt.show()


# In[12]:


arquivo=open('Resultado.txt','w')
arquivo.write('LM: '+str(linha_media)+'\n')
arquivo.write('LSC: '+str(linha_superior)+'\n')
arquivo.write('LIC: '+str(linha_inferior)+'\n')
arquivo.write('Duas Fugas Consecutivas: '+str(contador_consec)+'\n')
arquivo.write('Duas Fugas em Três Amostras Consecutivas: '+str(contador_2em3)+'\n')
arquivo.close()

