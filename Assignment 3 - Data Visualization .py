#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt 
import os
import numpy as np


# In[77]:


df = pd.read_csv(r'C:\Users\sarah\OneDrive\Documents\DSG\Airbnb Dataset 19.csv', encoding='latin-1')
print(df)


# In[78]:


df.head(11)


# In[8]:


len(df)


# In[9]:


df.dtypes


# In[10]:


df.isnull().sum()


# In[11]:


df.neighbourhood_group.unique()


# In[12]:


df.room_type.unique()


# In[26]:


df.neighbourhood_group = df.neighbourhood_group.astype('category')
df.neighbourhood_group.cat.categories


# In[27]:


pd.crosstab(df.neighbourhood_group, df.room_type)


# In[ ]:





# # room type and price

# sns.catplot(x="room_type", y="price", data=df);

# In[30]:


sns.catplot(x="neighbourhood_group", y="price", kind="bar",
            data=df);


# roomtype and neighbourhood type

# In[38]:


plt.figure(figsize=(10,10))
df1 = sns.countplot(x=df['room_type'],hue=df['neighbourhood_group'], palette='plasma')


# neighbourhood_group and room availability

# In[40]:


plt.figure(figsize=(10,10))
df1 = sns.lineplot(data=df, x=''neighbourhood_group'',y='availability_365',palette='plasma')


# Scatter Plot: Latitude vs. Longitude

# In[97]:


plt.scatter(df['longitude'], df['latitude'])
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Scatter Plot: Latitude vs. Longitude')
plt.show()


# Bar Plot: Neighbourhood Group Counts

# In[98]:


neighbourhood_group_counts = df['neighbourhood_group'].value_counts()
plt.bar(neighbourhood_group_counts.index, neighbourhood_group_counts.values)
plt.xlabel('Neighbourhood Group')
plt.ylabel('Count')
plt.title('Bar Plot: Neighbourhood Group Counts')
plt.show()


# Histogram: Price Distribution

# In[99]:


plt.hist(df['price'], bins=20)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Histogram: Price Distribution')
plt.show()


# Pie Chart: Room Type Distribution

# In[100]:


room_type_counts = df['room_type'].value_counts()
plt.pie(room_type_counts.values, labels=room_type_counts.index, autopct='%1.1f%%')
plt.title('Pie Chart: Room Type Distribution')
plt.show()


# Line Plot: Reviews per Month Over Time

# In[101]:


df['last_review'] = pd.to_datetime(df['last_review'])
df_sorted = df.sort_values('last_review')

plt.plot(df_sorted['last_review'], df_sorted['reviews_per_month'])
plt.xlabel('Date')
plt.ylabel('Reviews per Month')
plt.title('Line Plot: Reviews per Month Over Time')
plt.show()


# Heatmap: Correlation Matrix

# In[102]:


correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap: Correlation Matrix')
plt.show()


# Bar Plot: Top 10 Neighbourhoods by Listing Count

# In[103]:


top_10_neighbourhoods = df['neighbourhood'].value_counts().head(10)
plt.bar(top_10_neighbourhoods.index, top_10_neighbourhoods.values)
plt.xlabel('Neighbourhood')
plt.ylabel('Count')
plt.title('Bar Plot: Top 10 Neighbourhoods by Listing Count')
plt.xticks(rotation=45)
plt.show()


# Scatter Plot: Price vs. Reviews per Month

# In[104]:


plt.scatter(df['reviews_per_month'], df['price'])
plt.xlabel('Reviews per Month')
plt.ylabel('Price')
plt.title('Scatter Plot: Price vs. Reviews per Month')
plt.show()


# In[ ]:




