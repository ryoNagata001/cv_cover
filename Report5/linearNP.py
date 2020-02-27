import cv2
import numpy as np
import time
from grayscale import readImage

def myFilter2D(src, kernel):
    drows, dcols = src.shape[:2]
    dst = np.zeros((drows, dcols), np.float64)
    krows, kcols = kernel.shape[:2]
    ahgt = krows //2
    awth = kcols //2
    org  = cv2.copyMakeBorder(src, ahgt, ahgt, awth, awth, cv2.BORDER_DEFAULT)
    org = np.float64(org)
    for krow in range(0, krows):
        for kcol in range(0, kcols):
            dst += org[krow:krow+drows, kcol:kcol+dcols] * kernel[krow, kcol]
    return dst

def main():
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    m = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    kernel = np.array(m)
    s = time.time()
    
    tmp = myFilter2D(gray, kernel)

    print('time:', time.time()-s, 'sec')
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(tmp)
    gray = (tmp - minVal) / (maxVal - minVal)
    edge = cv2.convertScaleAbs(tmp)
    cv2.imshow('Source', img)
    cv2.imshow('Result', gray)
    cv2.imshow('Edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()