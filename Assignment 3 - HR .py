#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np 
import pandas as pd 
import os 
import matplotlib.pyplot as plt


# In[17]:


df = pd.read_csv(r"C:\Users\sarah\OneDrive\Desktop\HRDataset_v14.csv")


# In[18]:


df.shape


# In[19]:


df.dtypes


# In[20]:


df.head(5)


# In[21]:


df.describe()


# In[22]:


categorical = df.dtypes[df.dtypes == "object"].index
print(categorical)


# In[23]:


df[categorical].describe()


# In[25]:


department_counts = df['Department'].value_counts()

plt.figure(figsize=(10, 6))
plt.bar(department_counts.index, department_counts.values)
plt.xlabel('Department')
plt.ylabel('Count of Employees')
plt.title('Employee Count by Department')
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show()


# In[31]:


marital_counts = df['MaritalDesc'].value_counts()

plt.figure(figsize=(5, 5))
plt.pie(marital_counts.values, labels=marital_counts.index, autopct='%1.1f%%')
plt.title('Marital Status Distribution')
plt.axis('equal')  
plt.show()


# In[34]:


plt.figure(figsize=(10, 6))
plt.hist(df['Salary'], bins=10, edgecolor='black')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Employee Salaries')
plt.show()


# In[37]:


plt.figure(figsize=(10, 6))
df.boxplot(column='Salary', by='Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.title('Salary Ranges by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[38]:


plt.figure(figsize=(10, 6))
plt.scatter(df['EngagementSurvey'], df['EmpSatisfaction'])
plt.xlabel('Engagement Survey Score')
plt.ylabel('Employee Satisfaction')
plt.title('Engagement Survey Score vs. Employee Satisfaction')
plt.show()


# In[39]:


df['LastPerformanceReview_Date'] = pd.to_datetime(df['LastPerformanceReview_Date'])

plt.figure(figsize=(10, 6))
plt.plot(df['LastPerformanceReview_Date'], df['Absences'])
plt.xlabel('Date of Last Performance Review')
plt.ylabel('Absences')
plt.title('Absences Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[40]:


gender_performance = df.groupby(['PerformanceScore', 'GenderID']).size().unstack()

plt.figure(figsize=(10, 6))
gender_performance.plot(kind='bar', stacked=True)
plt.xlabel('Performance Score')
plt.ylabel('Count')
plt.title('Performance Score by Gender')
plt.legend(title='Gender', loc='upper right')
plt.show()


# In[41]:


import seaborn as sns


# In[42]:


correlation_matrix = df[['EmpSatisfaction', 'SpecialProjectsCount']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation between Employee Satisfaction and Special Projects Count')
plt.show()


# In[43]:


average_salary_by_department = df.groupby('Department')['Salary'].mean()

plt.figure(figsize=(10, 6))
average_salary_by_department.plot(kind='bar')
plt.xlabel('Department')
plt.ylabel('Average Salary')
plt.title('Average Salary by Department')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[44]:


df['LastPerformanceReview_Date'] = pd.to_datetime(df['LastPerformanceReview_Date'])

plt.figure(figsize=(10, 6))
plt.stackplot(df['LastPerformanceReview_Date'], df['Absences'], labels=['Absences'])
plt.xlabel('Date of Last Performance Review')
plt.ylabel('Absences')
plt.title('Changes in Employee Absences over Time')
plt.legend(loc='upper left')
plt.show()


# In[ ]:




