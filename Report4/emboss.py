import cv2
import numpy as np
from grayscale import readImage


def main():
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    emboss = getEmboss(gray, 0.1, 128)
    cv2.imshow('Original', gray)
    cv2.imshow('Emboss', emboss)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getEmboss(image, alpha, staticColor):
    """
    imageは二次元配列
    """
    res = np.zeros(image.shape, np.uint8)
    res[len(image)-1, len(image[0])-1] = staticColor
    for row in range(len(image)-1):
        for col in range(len(image[row])-1):
            temp = alpha * (image[row, col] -
                            image[row + 1, col + 1]) + staticColor
            if temp <= 0:
                res[row, col] = 0
            elif 255 <= temp:
                res[row, col] = 255
            else:
                res[row, col] = int(temp)
    return res


if __name__ == '__main__':
    main()
