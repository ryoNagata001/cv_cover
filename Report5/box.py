import cv2
import numpy as numpy
import time
from grayscale import readImage

def myboxFilter(img, size):
    rows, cols = img.shape[:2]
    krows, kcols = size
    ahgt = krows //2
    awth = kcols //2
    org = cv2.copyMakeBorder(img, ahgt, ahgt, awth, awth, cv2.BORDER_DEFAULT)
    intimg = cv2.integral(org, cv2.CV_64F)
    res = intimg[0:rows, 0:cols] -
          intimg[krows:krows+rows, 0:cols] -
          intimg[0:rows, kcols:kcols+cols] +
          intimg[krows:krows+rows, kcols:kcols+cols]
    return np.uint8(res / (krows * kcols))


def main():
    img = readImage()
    cv2.imshow('Source', img)
    kmin, kmax = 3, 41
    for ksize in range (kmin, kmax+1, 2):
        print('kernel size =', ksize, 'x', ksize)
        kernel = np.ones((ksize, ksize), np.float64) / (ksize*ksize)
    s = time.time()
    res = cv2.filter2D(img, cv2.CV_8UC3, kernel)
    print('filter2D:{:6.2f}'.format((time.time()-s)*1000), end='mst')
    kernel = np.ones(ksize, np.float64) / ksize
    s = time.time()
    res = cv2.filter2D(img, cv2.CV_8UC3, kernel, kernel)
    print('sepFilter:{:6.2f}'.format((time.time()-s)*1000), end='mst')
    s = time.time()
    res = cv2.boxFilter(img, cv2.CV_8UC3, (ksize, ksize))
    print( 'boxFilter:{:6.2f}'.format((time.time()-s)*1000), end='mst')
    s = time.time()
    res = myboxFilter(img, (ksize, ksize))
    print('myBoxFilter:{:6.2f}'.format((time.time()-s)*1000), end='mst')
    print('')
    cv2.imshow('Result', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()