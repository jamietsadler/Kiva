#!/usr/bin/env python
# coding: utf-8

# # Visualizing Loans Awarded by Kiva
# 
# Visualisation project based on the data from <a href = "https://www.kaggle.com/fkosmowski/kivadhsv1" target = "_blank">Kaggle</a>. The dataset contains information about loans awarded by the non-profit <a href = "https://www.kiva.org/" target = "_blank">Kiva</a>. 
# 

# In[2]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# ## Step 1: Load Data
# Load **kiva_data.csv** into a DataFrame called `df`

# In[4]:


df = pd.read_csv("kiva_data.csv")
df.head()


# ## Step 2: Examine The Data
# 
# 

# In[5]:


df.head(25)


# ## Step 3: Bar Charts

# 

# In[19]:


f, ax = plt.subplots(figsize=(15, 10))
sns.barplot(data=df, x="country", y="loan_amount")


# In[20]:



f, ax = plt.subplots(figsize=(15, 10))

sns.barplot(data=df, x="country", y = "loan_amount")


import matplotlib.ticker as mtick
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)


# In[21]:



f, ax = plt.subplots(figsize=(15, 10))

sns.barplot(data=df, x="country", y="loan_amount", hue="gender")

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)


# ## Step 4: Styling
# 
# 

# In[22]:


sns.set_palette("Dark2")

sns.set_style("darkgrid")

plt.figure(figsize=(25, 15))

ax.set_title("Loan Amounts")

sns.barplot(data=df, x="country", y="loan_amount", hue="gender")


# ## Step 5: Box Plots 

# In[23]:


plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x="country", y="loan_amount")


# In[24]:


plt.figure(figsize=(16, 10))
sns.boxplot(data=df, x="activity", y="loan_amount")


# ## Step 6: Violin Plots

# In[25]:


plt.figure(figsize=(16, 10))

sns.violinplot(data=df, x="activity", y="loan_amount")


# In[26]:


plt.figure(figsize=(16, 10))
sns.violinplot(data=df, x="country", y="loan_amount")


# In[27]:


# Some styling (feel free to modify)
sns.set_palette("Spectral")
plt.figure(figsize=(18, 12))
sns.violinplot(data=df, x="country", y="loan_amount", hue="gender", split=True)


# In[ ]:




