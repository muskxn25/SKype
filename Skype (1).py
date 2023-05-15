#!/usr/bin/env python
# coding: utf-8

# In[1]:


# sending message to a group chat
from skpy import Skype

# create a Skype object and login with your credentials
sk = Skype("muskansahetai.stepin@gmail.com", "stepin@123")

# find the group chat you want to send a message to
group = sk.chats["19:9ac60db17fa448d0947cf36bfe145607@thread.skype"]

# send a message to the group chat
group.sendMsg("Sending message Testing")


# In[ ]:




