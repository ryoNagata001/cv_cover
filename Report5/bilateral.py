import cv2
from grayscale import readImage

ksize = 15
winResult = 'Bilateral'
trackColor = 'ColorSigma'
trackSpace = 'SpaceSigma'


def onChange(val):
    global img
    color = cv2.getTrackbarPos(trackColor, winResult)
    sigmaColor = 2**(color/12)
    space = cv2.getTrackbarPos(trackSpace, winResult)
    sigmaSpace = space*space/512
    result = cv2.bilateralFilter(img, ksize, sigmaColor, sigmaSpace)
    cv2.imshow(winResult, result)


def main():
    global img
    img = readImage()
    cv2.imshow('Source', img)
    res = cv2.GaussianBlur(img, (ksize, ksize), -1)
    cv2.imshow('Gaussian', res)
    trackMax = 128
    cv2.namedWindow(winResult)
    cv2.createTrackbar(trackColor, winResult, 0, trackMax, onChange)
    cv2.setTrackbarPos(trackColor, winResult, trackMax)
    cv2.createTrackbar(trackSpace, winResult, 0, trackMax, onChange)
    cv2.setTrackbarPos(trackSpace, winResult, trackMax)
    onChange(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
