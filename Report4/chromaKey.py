import cv2
import numpy as np
from dissolve import readImages

winChromaKey = 'ChromaKey'
trackbars = ('LowerBlue', 'UpperBlue', 'LowerGreen',
             'UpperGreen', 'LowerRed', 'UpperRed')
trackMax = 255


def onChange(val):
    global fore, back
    lower, upper = [], []
    for i in range(len(trackbars)):
        if i % 2 == 0:
            lower.append(cv2.getTrackbarPos(
                trackbars[i], winChromaKey) / trackMax)
        else:
            upper.append(cv2.getTrackbarPos(
                trackbars[i], winChromaKey) / trackMax)

    posMask = cv2.inRange(fore, np.array(lower), np.array(upper)) / trackMax
    posMask = cv2.merge((posMask, posMask, posMask))
    negMask = np.ones(posMask.shape, np.float64) - posMask

    result = fore * negMask + back * posMask
    cv2.imshow(winChromaKey, result)


def main():
    global fore, back
    fore, back = readImages()
    fore = fore.astype(np.float64) / trackMax
    cv2.imshow('Foreground', fore)
    back = back.astype(np.float64) / trackMax
    cv2.imshow('Background', back)
    cv2.namedWindow(winChromaKey)

    for i in range(len(trackbars)):
        cv2.createTrackbar(trackbars[i], winChromaKey, 0, trackMax, onChange)
        cv2.setTrackbarPos(trackbars[i], winChromaKey, (i % 2) * trackMax)

    onChange(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
