import cv2
from grayscale import readImage

def main():
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Source', gray)
    k = 3
    tmp = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=k)
    tmp = cv2.convertScaleAbs(tmp)
    cv2.imshow('SobleX', tmp)
    tmp = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=k)
    tmp = cv2.convertScaleAbs(tmp)
    cv2.imshow('SobleY', tmp)
    tmp = cv2.Laplacian(gray, cv2.CV_64F, ksize=k)
    tmp = cv2.convertScaleAbs(tmp)
    cv2.imshow('Laplacian', tmp)
    lower, upper = 180, 250
    tmp = cv2.Canny(gray, lower, upper)
    tmp = cv2.convertScaleAbs(tmp)
    cv2.imshow('canny', tmp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()