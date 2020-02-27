import cv2
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
    print(hist[150][200])
    equal = cv2.equalizeHist(gray)
    cv2.imshow('Result', equal)
    hist = histImage(getHistogram(equal, histSize))
    cv2.imshow('Result Histogram', hist)
    cv2.waitKey(0)
    cv2.imwrite('equalized.jpg', equal)
    cv2.destroyAllWindows()


# def getAccumulationHistogram(hist):
#     for row in range(len(hist)):
#         for col in range(len(hist[row])):


if __name__ == '__main__':
    main()
