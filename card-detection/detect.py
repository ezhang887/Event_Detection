import cv2
import numpy as np
import time

#abstract class
class CardDetector:

    def __init__(self):
        self.hsv_low = None
        self.hsv_test = None

    def solidity(self, contour):
        w,h = cv2.minAreaRect(contour)[1]
        area = w*h
        contourArea = cv2.contourArea(contour)
        print(contourArea/area)
        return contourArea/area

    def area(self, contour, total_area):
        area = cv2.contourArea(contour)
        return area/total_area

    def draw_rotated_rect(self, image, contour):
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (255,0,0), 3)
        return rect

    def detect(self, image, display_time = 5, debug = False):
        height, width, _ = image.shape
        total_area = height*width
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.hsv_low, self.hsv_high)
        _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(contours)):
            if hierarchy[0,i,3] != -1:
                continue
            cnt = contours[i]
            cnt = cv2.convexHull(cnt)
            rect = cv2.boundingRect(cnt)
            x,y,w,h = rect
            aspect_ratio = h/w
            if self.area(cnt, total_area) >= 1/1000 and self.area(cnt, total_area) <= 1/100 and cv2.isContourConvex(cnt) and aspect_ratio < 3 and aspect_ratio > 1/3 and self.solidity(cnt) > 0.6:
                self.draw_rotated_rect(image, cnt)
        start_time = time.time()
        while time.time() < start_time + display_time:
            cv2.imshow("image", image)
            if debug:
                cv2.imshow("hsv", hsv)
                cv2.imshow("mask", mask)
            cv2.waitKey(10)

#red card detector class
class RedCardDetector(CardDetector):

    def __init__(self):
        self.hsv_low = np.array([0,150,200])
        self.hsv_high = np.array([10,255,255])

#yellow card detector class
class YellowCardDetector(CardDetector):

    def __init__(self):
        self.hsv_low = np.array([20,120,150])
        self.hsv_high = np.array([40,255,255])

