import cv2
import numpy as np
from grayscale import readImage
from histogram import histImage
from histogramCV import getHistogram


def main():
    img = readImage()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray', gray)
    histSize = 256
    hist = histImage(getHistogram(gray, histSize))
    cv2.imshow('Gray Histogram', hist)
    # ここを変更する
    """
    ヒストグラムを均一化するルックアップテーブルを作成し、そのルックアップテーブルを用いてトーンマッピングする
    ヒストグラムが均一化されている場合には、累積相対頻度と明度が等しくなる。
    => ヒストグラムから累積ヒストグラムを作成し、それをトーンマッピングのルックアップテーブルとして用いればいい。
    """
    # histgramの取得
    histogram = getHistogram(gray, histSize)
    # 累積histgramを作成
    ruiseki = getRuiseki(histogram)
    print('ruiseki', ruiseki)
    hist = histImage(ruiseki)
    cv2.imshow('Ruiseki Histogram', hist)
    # 累積histogramをトーンマッピングのルックアップテーブルとして使う
    lookUpTable = getLookUp(ruiseki)
    equal = cv2.LUT(gray, lookUpTable)
    cv2.imshow('Result', equal)
    hist = histImage(getHistogram(equal, histSize))
    cv2.imshow('Result Histogram', hist)
    cv2.waitKey(0)
    cv2.imwrite('equalized.jpg', equal)
    cv2.destroyAllWindows()


def getRuiseki(histogram):
    ruiseki = np.zeros(histogram.shape, np.float64)
    sum = 0
    for i in range(len(histogram)):
        ruiseki[i, 0] = sum + histogram[i, 0]
        sum += histogram[i, 0]
    # 最大値
    max = ruiseki[len(histogram)-1, 0]
    ruiseki = (ruiseki * (255.0 / max)).astype(np.uint8)
    # 正規化
    return ruiseki


def getLookUp(ruiseki):
    lookUpTable = np.zeros(len(ruiseki), np.uint8)
    for i in range(len(ruiseki)):
        lookUpTable[i] = ruiseki[i, 0]
    return lookUpTable


if __name__ == '__main__':
    main()
