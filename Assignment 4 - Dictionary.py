#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
unique_values = set(my_dict.values())
print(unique_values)


# In[2]:


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
combined_dict = {**dict1, **dict2}
for key, value in dict1.items():
    if key in dict2:
        combined_dict[key] = value + dict2[key]
print(combined_dict)


# In[3]:


my_dict = {}
if not my_dict:
    print("The dictionary is empty")
else:
    print("The dictionary is not empty")


# In[4]:


my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
unique_dict = {}
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print(unique_dict)


# In[5]:


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person("John", 30, "New York")
person_dict = vars(person)
print(person_dict)


# In[6]:


my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 3}
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print("Maximum value:", max_value)
print("Minimum value:", min_value)


# In[7]:


my_dict = {'a': 5, 'b': 2, 'c': 8, 'd': 3}
sorted_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print("Ascending order:", sorted_asc)
print("Descending order:", sorted_desc)


# In[9]:


my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
print(my_dict)


# In[ ]:




