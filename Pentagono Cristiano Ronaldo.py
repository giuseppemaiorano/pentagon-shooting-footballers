#!/usr/bin/env python
# coding: utf-8

# In[26]:


import matplotlib.pyplot as plt
import pandas as pd
from math import pi
 
df = pd.DataFrame({
'group': ['A','B','C','D'],
'Pot. tiro': [95, 1.5, 30, 4],
'Finalizzaz': [94, 10, 9, 34],
'Tiri dist.': [93, 39, 23, 24],
'Tiri al volo': [87, 31, 33, 14],
'effetto': [81, 15, 32, 14]
})


# In[36]:


categories=list(df)[1:]
N = len(categories)
 

values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
values
 
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]


# In[35]:


ax = plt.subplot(111, polar=True)
 
plt.xticks(angles[:-1], categories, color='red', size=10)
ax.set_xlabel("Cristiano Ronaldo", color='black')
 
ax.set_rlabel_position(0)
plt.yticks([50,70,90], ["50","70","90"], color="grey", size=8)
plt.ylim(0,100)
 
ax.plot(angles, values, linewidth=1, linestyle='solid')
 
ax.fill(angles, values, 'b', alpha=0.1)


# In[ ]:




