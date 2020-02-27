import cv2
import numpy as np
from grayscale import readImage


def gammaLUT(trackHalf, trackMax):
    base, ratio = 2.0, 32.0
    histSize = 256
    lookUpTable = np.zeros((trackMax+1, histSize), np.uint8)
    for trackVal in range(trackMax+1):
        gamma = base**((trackHalf-trackVal) / ratio)
        for val in range(histSize):
            lookUpTable[trackVal, val] = \
                round((val/(histSize-1))**gamma * (histSize-1))
    return lookUpTable


winRes = 'Result'
track = 'Gamma'


def changeGamma(val):
    global gray, lookUpTable
    val = cv2.getTrackbarPos(track, winRes)
    result = cv2.LUT(gray, lookUpTable[val])
    cv2.imshow(winRes, result)


def main():
    global gray, lookUpTable
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', gray)

    trackHalf = 128
    trackMax = trackHalf * 2
    lookUpTable = gammaLUT(trackHalf, trackMax)

    cv2.namedWindow(winRes)
    cv2.createTrackbar(track, winRes, 0, trackMax, changeGamma)

    cv2.setTrackbarPos(track, winRes, trackHalf)
    changeGamma(trackHalf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


# In[ ]:
