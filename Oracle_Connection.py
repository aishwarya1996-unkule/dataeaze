#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cx_Oracle
import pandas as pd


# In[2]:


con=cx_Oracle.connect('system/1234@127.0.0.1/XE')
if con!=None:
    print(con.version)
    print("Connection Done")
else:
    print("Connection False")


# In[3]:


cur=con.cursor()
query='''select * from emp'''
cur.execute(query)


# In[4]:


table_rows=cur.fetchall()
df=pd.read_sql('select * from emp',con=con)
print(df)


# In[5]:


df1=pd.read_sql('select * from emp where sal between 1600 and 3000',con=con)
print(df1)


# In[9]:


create_table2='''create table DataEaze2(id number primary key,name varchar(20),mobile char(10),addr varchar(50))'''
cur.execute(create_table2)


# In[10]:


insert='''insert into DataEaze2 values(101,'Aishwarya','9767466947','Shahupuri Satara')'''
cur.execute(insert)


# In[11]:


insert1='''insert into DataEaze2 values(102,'Shubham','9876543210','Katraj Pune')'''
cur.execute(insert1)


# In[12]:


df2=pd.read_sql('select * from DataEaze2',con=con)
print(df2)


# In[ ]:




