#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pymongo import MongoClient


# In[3]:


client=MongoClient('localhost:27017')
print("Connection done")


# In[10]:


db = client.iacsdedbda


# In[11]:


db.client.iacsdedbda


# In[17]:


emp=db.emp.find().limit(2)


# In[18]:


import pprint


# In[22]:


with MongoClient() as client:
        db = client.iacsdedbda
        for doc in db.emp.find():
            pprint.pprint(doc)


# In[ ]:




