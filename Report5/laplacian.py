import cv2
import numpy as np
from grayscale import readImage


def main():
    img = readImage()
    k = 3
    tmp = cv2.Laplacian(img, cv2.CV_64F, ksize=k)
    temp = getSharpImage(img, tmp, 0.2)
    cv2.imshow('Original', img)
    cv2.imshow('Sharp', temp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def getSharpImage(image, laplacian, alpha):
    print(laplacian)
    temp = (image - alpha * laplacian) / 255.0
    return temp


if __name__ == '__main__':
    main()
