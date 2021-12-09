#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import itertools


# In[4]:


def find_closest_sum(numbers, targets):
    numbers = numbers[:]
    for t in targets:
        if not numbers:
            break
        combs = sum([list(itertools.combinations(numbers,r))
                    for r in range(1, len(numbers)+1)], [])
        sums = np.asarray(list(map(sum,combs)))
        bestcomb = combs[np.argmin(np.abs(np.asarray(sums) - t))]
        numbers = list(set(numbers).difference(bestcomb))
        print("Target: {}, combination: {}".format(t, bestcomb))

targets = [76, 71]
numbers = [40, 75, 59, 12, 82, 0, 200, 60000, 400, 62, 50958]
find_closest_sum(numbers, targets)                                    


# In[ ]:




