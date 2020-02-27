import cv2
from grayscale import readImage
from histogram import createLUT, histImage, winRes, trackB, trackC, trackHalf


def getHistogram(img, histSize):
    histogram = cv2.calcHist([img], [0], None, [histSize], [0, histSize])
    return histogram


def onChange(val):
    global gray, result
    histSize = 256
    lookUpTable = createLUT(winRes, trackB, trackC, trackHalf, histSize)

    result = cv2.LUT(gray, lookUpTable)
    cv2.imshow(winRes, result)
    hist = histImage(getHistogram(result, histSize))
    cv2.imshow('Histogram', hist)


def main():
    global gray, result
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
