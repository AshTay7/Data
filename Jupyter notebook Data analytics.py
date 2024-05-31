#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[21]:


dataframe = pd.read_csv('4303974_dataset.csv')
dataframe.head()


# In[20]:


#import package 
import matplotlib.pyplot as plt
import numpy as np

#create data
x= np.arange(5)
y1= [1599.9,1376.3,1376.3,1030.9,2752.6]
y2 = [777.0,777.0,898.1,1030.9,1030.9]
y3 = [256.99, 28.908, 25.987, 71.8668, 47.09767]
width= 0.2

#plot data in grouped manner of bar type
plt.bar(x-0.2, y1, width, color= 'violet')
plt.bar(x, y2, width, color= 'blue')
plt.bar(x+0.2, y3, width, color= 'Pink')
plt.xticks(x,['Miss', 'Mr', 'Mrs', 'Hon', 'Dr'])
plt.xlabel('item_id')
plt.ylabel('sku')
plt.legend(["APPHAI5A015E5320BB0", "APPHAI5A02071AB37EA","MATHUA5A0AD9A76E957","MATLEN5A000D63006BF","MATHTC59D77E7A70ABA"])
plt.show()


# In[24]:


dataframepi = pd.DataFrame({'Gender': dataframe.Gender, "age": dataframe.age})
dataframepi


# In[27]:


dataframepi.groupby(['Gender']).sum().plot(kind ="pie", y= 'age', autopct= '%1.0f%%')


# In[28]:


corr=dataframe.corr()
corr


# In[29]:


import seaborn as sns
#create a map of the correlations
sns.heatmap(corr, vmin= -0.5, vmax= 1.0)
plt.show()


# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[33]:


#create a box plot for each sku
sns.boxplot(x= "qty_ordered", y="Zip", data=dataframe)


# In[ ]:




