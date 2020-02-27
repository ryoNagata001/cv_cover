import sys
import cv2
import numpy as np


def main():
    if len(sys.argv) > 3:
        foreFile = sys.argv[1]
        backFile = sys.argv[2]
        alphaFile = sys.argv[3]
    else:
        foreFile = input('foreground image -> ')
        backFile = input('background image -> ')
        alphaFile = input('alphamatte -> ')

    fore = cv2.imread(foreFile)
    if fore is None:
        print('no image file:', foreFile)
        sys.exit(1)

    back = cv2.imread(backFile)
    if back is None:
        print('no image file:', backFile)
        sys.exit(1)

    alpha = cv2.imread(alphaFile)
    if alpha is None:
        print('no image file:', alphaFile)
        sys.exit(1)

    if fore.shape[:2] != back.shape[:2]:
        print('diferent image sizes:', foreFile, backFile)
        sys.exit()

    if fore.shape[:2] != alpha.shape[:2]:
        print('diferent image sizes:', foreFile, alphaFile)
        sys.exit()

    fore = fore.astype(np.float64) / 255.0
    cv2.imshow('Foreground', fore)
    back = back.astype(np.float64) / 255.0
    cv2.imshow('Background', back)
    alpha = alpha.astype(np.float64) / 255.0
    cv2.imshow('Alphamatte', alpha)
    result = fore * alpha + back * (1.0 - alpha)

    cv2.imshow("Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
