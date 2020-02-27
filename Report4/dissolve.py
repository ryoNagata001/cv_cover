import sys
import cv2
import numpy as np

winResult = 'Result'
trackbar = 'Alpha'
trackHalf = 128
trackMax = trackHalf * 2


def readImages():
    if len(sys.argv) > 2:
        foreFile = sys.argv[1]
        backFile = sys.argv[2]
    else:
        foreFile = input('foreground image -> ')
        backFile = input('background image-> ')
    fore = cv2.imread(foreFile)
    if fore is None:
        print('no image file:', foreFile)
        sys.exit(1)

    back = cv2.imread(backFile)
    if back is None:
        print('no image file:', backFile)
        sys.exit(1)

    if fore.shape[:2] != back.shape[:2]:
        print('different image sizes: ', foreFile, backFile)
        sys.exit(1)

    return (fore, back)


def onChange(val):
    global fore, back
    alpha = val / trackMax
    result = (fore.astype(np.float64) / 255) * (1-alpha) + \
        (back.astype(np.float64) / 255) * alpha

    cv2.imshow(winResult, result)


def main():
    global fore, back
    fore, back = readImages()
    cv2.namedWindow(winResult)
    cv2.createTrackbar(trackbar, winResult, 0, trackMax, onChange)
    cv2.setTrackbarPos(trackbar, winResult, trackHalf)
    onChange(trackHalf)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
