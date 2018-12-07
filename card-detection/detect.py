import cv2
import numpy as np

#abstract class
class CardDetector:

    def __init__(self):
        self.hsv_low = None
        self.hsv_test = None

    def solidity(self, contour):
        x,y,w,h = cv2.boundingRect(contour)
        return cv2.contourArea(contour)/(w*h)

    def area(self, contour, total_area):
        area = cv2.contourArea(contour)
        return area/total_area

    def detect(self, image):
        height, width, _ = image.shape
        total_area = height*width
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.hsv_low, self.hsv_high)
        _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        good = []
        for i in range(len(contours)):
            if hierarchy[0,i,3] != -1:
                continue
            cnt = contours[i]
            cnt = cv2.convexHull(cnt)
            rect = cv2.boundingRect(cnt)
            if self.area(cnt, total_area) >= 1/1000 and self.area(cnt, total_area) <= 1/100 and cv2.isContourConvex(cnt):
                good.append(cnt)
        cv2.drawContours(image, good, -1, (255,0,0), 3)
        while True:
            cv2.imshow("image", image)
            cv2.imshow("hsv", hsv)
            cv2.imshow("mask", mask)
            cv2.waitKey(10)

#red card detector class
class RedCardDetector(CardDetector):

    def __init__(self):
        self.hsv_low = np.array([0,150,150])
        self.hsv_high = np.array([10,255,255])

#yellow card detector class
class YellowCardDetector(CardDetector):

    def __init__(self):
        self.hsv_low = np.array([20,120,180])
        self.hsv_high = np.array([40,255,255])

