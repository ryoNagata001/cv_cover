#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2
import numpy as np
from grayscale import readImage


# In[5]:


def createLUT(win, trackB, trackC, trackHalf, histSize):
    trackMax = trackHalf * 2
    bright = cv2.getTrackbarPos(trackB, win) / trackMax
    delta = (cv2.getTrackbarPos(trackC, win) - trackHalf) / trackHalf

    if delta >= 0:
        a = 1.0 / (1.0 - delta)
        b = bright - 0.5 * a
    else:
        a = 1.0 + delta
        b = bright - 0.5*a
    lookUpTable = np.zeros(histSize, np.uint8)
    for i in range(histSize):
        newVal = round((a * i / (histSize - 1) + b) * (histSize - 1))

        if newVal < 0:
            newVal = 0
        if newVal > (histSize - 1):
            newVal = histSize - 1
        lookUpTable[i] = newVal
    return lookUpTable


# In[6]:


def getHistogram(img, histSize):
    histogram = np.zeros(histSize, np.float64)
    for row in range(len(img)):
        for col in range(len(img[row])):
            histogram[img[row, col]] += 1
    return histogram


# In[7]:


def histImage(histogram):
    histSize = histogram.shape[0]
    barWidth = 2
    histHeight = histSize
    histWidth = histSize * barWidth
    histogram = histogram * (histHeight / max(histogram))
    histImg = np.ones((histHeight, histWidth), np.uint8) * 255

    for val in range(histSize):
        cv2.rectangle(histImg, (val * barWidth, histHeight),
                      ((val+1)*barWidth-1, histHeight-int(histogram[val])), 0)

    return histImg


# In[8]:


winRes = 'Result'
trackB = 'Bright'
trackC = 'Contrast'
trackHalf = 128


# In[9]:


def onChange(val):
    global gray
    histSize = 256
    lookUpTable = createLUT(winRes, trackB, trackC, trackHalf, histSize)

    result = np.zeros(gray.shape[:2], np.uint8)

    for row in range(len(result)):
        for col in range(len(result[row])):
            result[row, col] = lookUpTable[gray[row, col]]
    cv2.imshow(winRes, result)
    hist = histImage(getHistogram(result, histSize))
    cv2.imshow('Histogram', hist)


# In[10]:


def main():
    global gray
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
    cv2.destroyAllWindows()


# In[11]:


if __name__ == '__main__':
    main()


# In[ ]:
