import cv2
import numpy as np
from grayscale import readImage


def main():
    img = readImage()
    cv2.imshow('Source', img)
    default_h = 22
    default_s = 150
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    planes = cv2.split(imgHSV)
    planes[0] = np.ones(planes[0].shape[:2], np.uint8) * default_h
    planes[1] = np.ones(planes[1].shape[:2], np.uint8) * default_s
    imgHSV = cv2.merge(planes)
    cv2.imshow('Sepia', cv2.cvtColor(imgHSV, cv2.COLOR_HSV2BGR))

    cv2.waitKey(0)
    cv2.destroyAllWIndows()


if __name__ == '__main__':
    main()
