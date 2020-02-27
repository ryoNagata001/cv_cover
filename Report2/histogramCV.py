#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
from grayscale import readImage
from histogram import createLUT, histImage, winRes, trackB, trackC, trackHalf


# In[5]:


def getHistogram(img, histSize):
    '''
    img         -given image
    histSize    -size of histogram (number of bins)
    create and return a histogram with OpenCV
    '''
    histogram = cv2.calcHist([img], [0], None, [histSize], [0, histSize])

    return histogram
# In[6]:

def onChange(val):
    '''
    val        -changed trackbar value (not used directly)
    '''
    global gray, result
    histSize    = 256
    lookUpTable = createLUT(winRes, trackB, trackC, trackHalf, histSize)

    result = cv2.LUT(gray, lookUpTable)
    cv2.imshow(winRes, result)
    hist = histImage(getHistogram(result, histSize))
    cv2.imshow('Histogram', hist)

# In[7]:


def main():
    global gray, result
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', gray)
    trackMax = trackHalf * 2
    cv2.namedWindow(winRes)
    cv2.createTrackbar(trackB, winRes, 0, trackMax, onChange)

    cv2.setTrackbarPos(trackB, winRes, trackHalf)
    cv2.createTrackbar(trackC, winRes, 0, trackMax, onChange)

    cv2.setTrackbarPos(trackC, winRes, trackHalf)
    onChange(trackHalf)
    cv2.waitKey(0)
    cv2.imwrite('mapped.jpg', result)
    cv2.destroyAllWindows()





# In[8]:

if __name__ == '__main__':
    main()


# In[ ]:
