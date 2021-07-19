#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis - Retail
# 
# Submitted by:-Sarang D.Jare

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[7]:


#import dataset
data=pd.read_csv(r"C:\Users\Sarang\Desktop\Data\SampleSuperstore.csv")

data.head(10)


# In[8]:


#Checking the dataset dimension

data.shape


# In[9]:


data.info()


# In[10]:


data.describe()


# In[11]:


data['Ship Mode'].unique()


# In[12]:


data['Segment'].unique()


# In[13]:


data['Segment'].value_counts().reset_index()


# In[14]:


seg=(data['Segment'].value_counts()/len(data['Segment'])*100).reset_index().sort_values('Segment',ascending=False)
seg


# In[15]:


plt.figure(figsize=(5,5))
labels=('Consumer','Corporate','Home Office')
explode=(0.01,0.01,0.01)
plt.pie(seg['Segment'],explode=explode,labels=labels,autopct='%1.1f%%')
plt.show()


# In[16]:


data['Ship Mode'].value_counts()


# In[17]:


sm=(data['Ship Mode'].value_counts()/len(data['Ship Mode'])*100).reset_index().sort_values('Ship Mode',ascending=False)
sm


# In[18]:


plt.figure(figsize=(5,5))
labels=sm['index']
explode=(0.01,0.01,0.01,0.01)
plt.pie(sm['Ship Mode'],explode=explode,labels=labels,autopct='%1.1f%%')
plt.show()


# In[19]:


cg=(data['Category'].value_counts()/len(data['Category'])*100).reset_index().sort_values('Category',ascending=False)
cg


# In[21]:


plt.figure(figsize=(5,5))
labels=cg['index']
explode=(0.01,0.01,0.01)
plt.pie(cg['Category'],explode=explode,labels=labels,autopct='%1.1f%%')
plt.show()


# In[22]:


((data['Sub-Category'].value_counts())/len(data['Sub-Category'])*100).plot(kind='bar') 


# In[23]:


fig,ax=plt.subplots()
colors={'Consumer':'red','Corporate':'blue','Home Office':'green'}
ax.scatter(data['Sales'],data['Profit'],c=data['Segment'].apply(lambda x: colors[x]))
plt.show()


# In[24]:


dat=data.drop(['Postal Code','Country'],axis=1)


# In[25]:


dat.head()


# In[26]:


cor=dat.corr()
cor


# In[27]:


sns.heatmap(cor,annot=True)


# Above the heat map from we conclude that , Sales vs Discount and Profit Vs Discount be negatively corelative ,
# that's means their are no relation if we made a good relation between then that's help's business profit.
# Now we focusing on Discount variable

# In[28]:


data.pivot_table(values='Sales',index='Segment',columns='Discount',aggfunc='median')


# In[29]:


data.pivot_table(values='Profit',index='Segment',columns='Discount',aggfunc='median')


# In[32]:


temp_dat1=data.loc[(data['Segment']=='Consumer')&(data['Discount']==0.10)]
temp_dat1['Profit'].plot.hist(bins=50)


# In[33]:


temp_dat2=data.loc[(data['Segment']=='Consumer')&(data['Discount']==0.2)]
temp_dat2['Profit'].plot.hist(bins=50)


# In[34]:


temp_dat3=data.loc[(data['Segment']=='Consumer')&(data['Discount']==0.80)]
temp_dat3['Profit'].plot.hist(bins=50)


# From the above Histogram plots we say , Discount between 10%and 20% 0n consumer segment that's helps increasing business profit

# In[35]:


temp_dat4=data.loc[(data['Segment']=='Corporate')&(data['Discount']==0.10)]
temp_dat4['Profit'].plot.hist(bins=50)


# In[36]:


temp_dat5=data.loc[(data['Segment']=='Corporate')&(data['Discount']==0.20)]
temp_dat5['Profit'].plot.hist(bins=50)


# In[37]:


temp_dat6=data.loc[(data['Segment']=='Corporate')&(data['Discount']==0.80)]
temp_dat6['Profit'].plot.hist(bins=50)


# 
# From the above Histogram plots we say , Discount between 10%and 20% 0n Corporate segment that's helps increasing business profit.

# In[38]:


temp_dat7=data.loc[(data['Segment']=='Home Office')&(data['Discount']==0.10)]
temp_dat7['Profit'].plot.hist(bins=50)


# In[39]:



temp_dat8=data.loc[(data['Segment']=='Home Office')&(data['Discount']==0.20)]
temp_dat8['Profit'].plot.hist(bins=50)


# In[40]:


temp_dat9=data.loc[(data['Segment']=='Home Office')&(data['Discount']==0.80)]
temp_dat9['Profit'].plot.hist(bins=50)


# 
# From the above Histogram plots we say , Discount between 10%and 20% 0n all segment that's helps increasing business profit

# In[41]:


temp_dc1=data.loc[(data['Category']=='Furniture')&(data['Discount']>=0.10)&(data['Discount']<=0.20)]
temp_dc1['Profit'].plot.hist(bins=50)


# In[42]:


temp_dc2=data.loc[(data['Category']=='Technology')&(data['Discount']>=0.10)&(data['Discount']<=0.20)]
temp_dc2['Profit'].plot.hist(bins=50)


# In[43]:


temp_dc3=data.loc[(data['Category']=='Office Supplies')&(data['Discount']>=0.10)&(data['Discount']<=0.20)]
temp_dc3['Profit'].plot.hist(bins=50)


# From the above Histogram plots we say , Discount between 10% and 20% 0n all Category that's helps increasing business profit.

# ## Thank you
