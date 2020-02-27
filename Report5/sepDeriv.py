import cv2
from grayscale import readImage


def main():
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ksize = 3
    krow, kcol = cv2.getDerivKernels(1, 0, ksize)
    tmp = cv2.sepFilter2D(gray, cv2.CV_64F, krow, kcol)
    gray = cv2.convertScaleAbs(tmp)
    print('row kernel matrix:n', krow)
    print('column kernel matrix:n', kcol)
    cv2.imshow('Source', img)
    cv2.imshow('Result', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
