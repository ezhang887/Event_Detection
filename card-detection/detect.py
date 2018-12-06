import cv2
import numpy as np

class CardDetector:

    def __init__(self):
        self.red_low = np.array([0,150,150])
        self.red_high = np.array([10,255,255])

    def solidity(self, contour):
        x,y,w,h = cv2.boundingRect(contour)
        return cv2.contourArea(contour)/(w*h)

    def area(self, contour):
        area = cv2.contourArea(contour)
        totalArea = self.height*self.width
        return area/totalArea

    def detect(self, image):
        self.height, self.width, _ = image.shape
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.red_low, self.red_high)
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
        contours = [cnt for cnt in contours if self.area(cnt) >= 1/1000 and self.area(cnt) <= 1/100 and self.solidity(cnt) >= 0.5]
        cv2.drawContours(image, contours, -1, (0,255,0), 3)

        while True:
            cv2.imshow("image", image)
            cv2.imshow("hsv", hsv)
            cv2.imshow("mask", mask)
            cv2.waitKey(10)
