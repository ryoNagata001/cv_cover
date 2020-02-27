import cv2
import time
from grayscale import readImage

def main():
    img = readImage()
    ksize, sigma = 15, 2.5
    kernel = cv2.getGaussianKernel(ksize, sigma, cv2.CV_64F)
    blur = cv2.sepFilter2D(img, cv2.CV_8UC3, kernel, kernel)
    print('kernel matrix:n', kernel)
    cv2.imshow('Source', img)
    cv2.imshow('Result', blur)
    cv2.imshow('Edge', edge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()