# todo変更

import cv2
from grayscale import readImage


def main():
    img = readImage()
    cv2.imshow('Original', img)
    scaleX = 16
    scaleY = 9
    rows, cols = img.shape[:2]
    size = (cols * scaleX, rows * scaleY)

    result = cv2.resize(img, size, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('NEAREST', result)
    result = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)
    cv2.imshow('LINEAR', result)
    result = cv2.resize(img, size, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('CUBIC', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
