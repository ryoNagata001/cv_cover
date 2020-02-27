#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
from grayscale import readImage


# In[4]:


wname = 'Binary'
trackbar = 'Threshold'


# In[5]:


def onChange(val):
    """
    val - changed trackbar value
    binalize the image (gray) with the threshold value
    """
    global gray
    white = 255
    ret, binary = cv2.threshold(gray, val, white, cv2.THRESH_BINARY)

    cv2.imshow(wname, binary)


# In[6]:


def main():
    global gray
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original', gray)
    trackHalf = 127
    trackMax = trackHalf * 2
    cv2.namedWindow(wname)
    cv2.createTrackbar(trackbar, wname, 0, trackMax, onChange)

    cv2.setTrackbarPos(trackbar, wname, trackHalf)
    onChange(trackHalf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# In[7]:


if __name__ == '__main__':
    main()


# In[ ]:
