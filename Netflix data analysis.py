#!/usr/bin/env python
# coding: utf-8

# In[81]:


# importing lib.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[82]:


df = pd.read_csv('mymoviedb.csv', lineterminator='\n')
df.head()


# In[83]:


# viewing dataset info
df.info()


# In[84]:


# exploring genres column
df['Genre'].head()


# In[85]:


# check for duplicated rows
df.duplicated().sum()


# In[86]:


# exploring summary statistics
df.describe()


# In[87]:


df.head()


# In[88]:


# casting column a
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
# confirming changes
print(df['Release_Date'].dtypes)


# In[89]:


df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes


# In[90]:


df.info()


# In[91]:


df.head()


# In[92]:


# making list of column to be dropped
cols = ['Overview', 'Original_Language', 'Poster_Url']
# dropping columns and confirming changes
df.drop(cols, axis = 1, inplace = True)
df.columns


# In[93]:


df.head()


# In[94]:


def catigorize_col (df, col, labels):
     edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
     df[col] = pd.cut(df[col], edges, labels = labels, duplicates='drop')
     return df


# In[95]:


# define labels for edges
labels = ['not_popular', 'below_avg', 'average', 'popular']
# categorize column based on labels and edges
catigorize_col(df, 'Vote_Average', labels)
# confirming changes
df['Vote_Average'].unique()


# In[96]:


df.head()


# In[97]:


# exploring column
df['Vote_Average'].value_counts()


# In[98]:


# dropping NaNs
df.dropna(inplace = True)
# confirming
df.isna().sum()


# In[99]:


# split the strings into lists
df['Genre'] = df['Genre'].str.split(', ')
# explode the lists
df = df.explode('Genre').reset_index(drop=True)
df.head()


# In[100]:


# casting column into category
df['Genre'] = df['Genre'].astype('category')
# confirming changes
df['Genre'].dtypes


# In[101]:


df.info()


# In[102]:


df.nunique()


# # Data visualization

# In[103]:


sns.set_style('whitegrid')


# # Q1: What is the most frequent genre in the dataset?

# In[104]:


df['Genre'].describe()


# In[105]:


sns.catplot(y = 'Genre' , data = df , kind = 'count' ,
           order = df['Genre'].value_counts().index ,
           color = '#4287f5')
plt.title('Genre column distribution')
plt.show()


# # Q2: What genres has highest votes ?

# In[106]:


df.head()


# In[107]:


sns.catplot(y = 'Vote_Average' , data = df , kind = 'count' , 
           order = df['Vote_Average'].value_counts().index ,
           color = 'red')
plt.title('Vote_Average distributation')
plt.show()


# # Q3: What movie got the highest popularity ? what's its genre ?

# In[108]:


df.head()


# In[109]:


df[df['Popularity'] == df['Popularity'].max()]


# # Q4: What movie got the lowest popularity? what's its genre?

# In[110]:


df[df['Popularity'] == df['Popularity'].min()]


# #  Q5: Which year has the most filmmed movies?

# In[111]:


df['Release_Date'].hist() 
plt.title('Release_Date column distribution')
plt.show() 


# In[ ]:


Colclusion :
 get_ipython().run_line_magic('pinfo', 'dataset')
 Drama genre is the most frequent genre in our dataset and has appeared more than 14% of the times among 19 other genres.
     
 Q2: What genres has highest votes ?
 we have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the highest popularity among fans by being having more than 18.5% of movies
 popularities.
 Q3: What movie got the highest popularity ? what's its Action , genre ?
 Spider-Man: No Way Home has the highest popularity rate in our dataset and it has genres of Adventure and Sience Fiction .

 Q3: What movie got the lowest popularity ? what's its genre ?
 The united states, thread' has the highest lowest rate in our dataset and it has genres of music , drama , 'war', 'sci-fi' and history`.

 Q4: Which year has the most filmmed movies?
 year 2020 has the highest filmming rate in our dataset.

