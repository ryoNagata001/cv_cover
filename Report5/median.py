import cv2
from grayscale import readImage

def main():
    img = readImage()
    cv2.imshow('Source', img)
    kmin, kmax = 9, 17
    for ksize in range (kmin, kmax+1, 2):
       res = cv2.GaussianBlur(img, (ksize, ksize), -1)
       cv2.imshow('Gaussian', res)
       res = cv2.boxFilter(img, cv2.CV_8UC3, (ksize. ksize))
       cv2.imshow('Box', res)
       res = cv2.medianBlur(img.ksize)
       cv2.imshow('Median', res)
       cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()