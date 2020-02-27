#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import cv2
import numpy as np


# In[2]:


def readImage():
    """
    read an image file and return its data
    """
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = input('image file -> ')
    image = cv2.imread(fname)
    print(image.shape)
    if image is None:
        print('no image file:', fname)
        sys.exit(1)
    return image


# In[3]:


def main():
    img = readImage()
    print('original size =', img.size)
    print('(height, width, channels) =', img.shape)
    print('channel depth =', img.dtype)
    cv2.imwrite('image.jpg', img)
    wname = 'Original'
    #
    cv2.imshow(wname, img)

    real = img.astype(np.float64) / 255.0
    print('\nreal number size =', real.size)
    print('(height, width, channels) =', real.shape)
    print('channel depth =', real.dtype)
    cv2.imwrite('real.jpg', real)
    wname = 'Real'
    cv2.imshow(wname, real)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print('\ngrayscale size =', gray.size)
    print('(height, width, channels) =', gray.shape)
    print('channel depth = ', gray.dtype)
    cv2.imwrite('gray.jpg', gray)
    wname = 'Gray'
    cv2.imshow(wname, gray)

    rGray = gray.astype(np.float64) / 255.0
    print('\nreal number size =', rGray.size)
    print('(height, width, channels) =', rGray.shape)
    print('channel depth =', rGray.dtype)
    cv2.imwrite('realGray.jpg', rGray)
    wname = 'RealGray'
    cv2.imshow(wname, rGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# In[5]:


if __name__ == '__main__':
    main()
