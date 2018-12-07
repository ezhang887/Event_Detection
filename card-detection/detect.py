import cv2
import numpy as np
import time

#abstract class
class CardDetector:

    def __init__(self):
        #type: 3-element numpy array
        #hsv minimum and maximum thresholds for converting the image to binary
        #everything between the threshold will be converted to white, everything outside will be black
        self.hsv_low = None
        self.hsv_test = None

    #takes in a contour, returns the "solidity" of the contour
    #the solidity of a contour is the ratio of the area of the contour to the area of the bounding rectangle around the contour
    def solidity(self, contour):
        w,h = cv2.minAreaRect(contour)[1]
        area = w*h
        contourArea = cv2.contourArea(contour)
        return contourArea/area

    #relative area of the contour:
    #this is the ratio of the area of the contour to the total area of the image
    def relative_area(self, contour, total_area):
        area = cv2.contourArea(contour)
        return area/total_area

    #draw the rotated rectangle around a contour: taken from opencv website
    def draw_rotated_rect(self, image, contour):
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], -1, (255,0,0), 3)
        return rect

    #code to detect a card
    #takes in an image (2-d numpy array where each element is [R,G,B])
    #and two optional parameters for the debugging/displaying images
    def detect(self, image, display_time = 5, debug = False):
        #do some initial calculations
        height, width, _ = image.shape
        total_area = height*width
        #convert the image to HSV from RGB
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        #threshold the image to be in the set hsv boundaries
        #mask is a binary image (2-d numpy array where each element is a single number)
        mask = cv2.inRange(hsv, self.hsv_low, self.hsv_high)
        #find all the contours on the binary image
        _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #filter through the contours
        for i in range(len(contours)):
            #if the contour is inside another contour, this is most likely not a card
            if hierarchy[0,i,3] != -1:
                continue
            cnt = contours[i]
            #use the convex hull of the contour from now on, as it gives a better estimate
            cnt = cv2.convexHull(cnt)
            #calculate the aspect ratio of the contour
            rect = cv2.boundingRect(cnt)
            x,y,w,h = rect
            aspect_ratio = h/w
            #filters:
            #the area of the card should be between 1/1000 and 1/100 of the total image area
            #the card should be a convex shape and not a concave shape
            #the aspect ratio of the card should be between 1/3 and 3
            #the solidity of the contour should be above 0.6
            if self.relative_area(cnt, total_area) >= 1/1000 and self.relative_area(cnt, total_area) <= 1/100 and cv2.isContourConvex(cnt) and aspect_ratio < 3 and aspect_ratio > 1/3 and self.solidity(cnt) > 0.6:
                #draw the rectangle on the image
                self.draw_rotated_rect(image, cnt)
        #display the image for the given time
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

