#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


X=[2,4,6,8]
Y=[2,4,6,8]
plt.plot(X,Y)
plt.show()


# In[3]:


X=[2,4,6,8]
Y=[2,4,6,8]
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Line Plot')
plt.plot(X,Y)
plt.show()


# In[4]:


X=[2,4,6,8]
Y=[2,4,6,8]
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Dashed Line Plot')
plt.plot(X,Y,'b',linestyle='dashed')
plt.show()


# In[5]:


X=[2,4,6,8]
Y=[2,4,6,8]
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Line Plot With Marker')
plt.plot(X,Y,marker='+',markersize=10,markeredgecolor='red')
plt.show()


# In[6]:


Overs=['1-10','11-20','21-30','31-40','41-50']
Runs = [50,60,45,55,70]
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title("India VS Eng")
plt.bar(Overs,Runs,width=0.7)
plt.show()


# In[7]:


Overs=['1-10','11-20','21-30','31-40','41-50']
Runs = [50,60,45,55,70]
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title("India VS Eng")
plt.barh(Overs,Runs,color='grey')
plt.show()


# In[8]:


#multiple bar graph 
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(1, 51, 5)
a = [50, 60, 70, 80, 90]
b = [55, 65, 60, 75, 96]

plt.bar(X, a, width=3, color='r', label='Australia')
plt.bar(X + 3, b, width=3, color='b', label='India')
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('India Vs Australia')
plt.legend()
plt.show()


# In[9]:


#1st piechart
import matplotlib.pyplot as plt
import numpy as np
x = np.array([35,15,20,15,5])
mylabel = ['Apple', 'Orange', 'Banana', 'Guava', 'Mango']
plt.pie(x, labels= mylabel)
plt.title('Pie Chart')
plt.show()


# In[10]:


#piechart
import matplotlib.pyplot as plt

slices = [50, 20, 15, 10, 5]
departments = ['Sales', 'HR', 'Finance', 'Production', 'Account']
colors = ['magenta', 'cyan', 'green', 'red', 'blue']
explode = [0, 0.2, 0.3, 0, 0]

plt.pie(slices, labels=departments, colors=colors, startangle=90, explode=explode, shadow=True, autopct='%.1f%%')
plt.title('Pie Chart')
plt.show()


# In[11]:


#histogram plot 
import matplotlib.pyplot as plt

age = [22, 32, 35, 45, 55, 14, 26, 19, 56, 44, 48, 33, 38, 28]
bins = [0, 10, 20, 30, 40, 50, 60]

plt.hist(age, bins=bins, color='magenta', histtype='bar', rwidth=0.8)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram Plot')
plt.show()


# In[ ]:




