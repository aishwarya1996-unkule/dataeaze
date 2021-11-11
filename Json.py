#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import json

try:
    req = requests.get("https://jsonplaceholder.typicode.com/todos/")
except requests.exceptions.ConnectionError:
    print("connection refused")


var = json.loads(req.text)

print(var)
print(len(var))

i=0
for v in var:
    if(v['completed']==True):
        i += 1
        # print(i)
    else:
        pass

print(i)

i = {}


# In[6]:


import pandas as pd 
import numpy as np
import json
import matplotlib as plt
#filepath="F:/datasets"


def load_rows(filepath, nrows = None):
    with open(filepath,encoding="utf8") as json_file:
        count = 0
        objs = []
        line = json_file.readline()
        while (nrows is None or count < nrows) and line:
            count += 1
            obj = json.loads(line)
            objs.append(obj)
            line = json_file.readline()
        return pd.DataFrame(objs)


# In[8]:


data = load_rows('E:\\DBDA\Project\\yelp_academic_dataset_review\\yelp_academic_dataset_review.json',nrows=1000)
print('user objects loaded. Count = {}'.format(data.shape[0]))
data


# In[ ]:




