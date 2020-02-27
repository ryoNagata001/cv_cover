import cv2
import numpy as np
from grayscale import readImage


def main():
    img = readImage()
    cv2.imshow('Original', img)
    rows, cols = img.shape[:2]
    size = (cols, rows)
    original = np.float32(((0, 0), (cols, 0), (0, rows)))
    translate = np.float32(((100, 150), (500, 50), (50, 550)))
    mat = cv2.getAffineTransform(original, translate)
    result = cv2.warpAffine(img, mat, size, flags=cv2.INTER_CUBIC)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
