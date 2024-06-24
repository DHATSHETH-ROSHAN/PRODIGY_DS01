#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


import pandas as pd
import csv
import matplotlib.pyplot as plt


# In[3]:


try:
    data = pd.read_csv("population.csv")
    print(data)
except pd.errors.ParserError as e:
    print(f"ParserError: {e}")
except Exception as e:
    print(f"Error: {e}")


# In[4]:


data.head()


# In[5]:


data.describe


# In[6]:


countries_to_plot = ['United States', 'Canada', 'Japan', 'Germany', 'France']
filtered_data = data[data['Country Name'].isin(countries_to_plot)]
print(filtered_data)

plt.bar(filtered_data['Country Name'], filtered_data['2022'])
plt.xlabel('Country Name')
plt.ylabel('Population in 2022')
plt.title('Population of Selected Countries')
plt.show()


# In[ ]:




