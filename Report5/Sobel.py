import cv2
import time
from grayscale import readImage

def main():
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    s = time.time()
    tmp = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
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