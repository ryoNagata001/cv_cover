import cv2
import numpy as np
import time
from grayscale import readImage

def main():
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    m = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    kernel = np.array(m)
    s = time.time()
    
    tmp = myFilter2D(gray, cv2.CV_64F, kernel)

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