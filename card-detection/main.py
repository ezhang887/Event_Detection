from detect import *
import cv2

'''
#image = cv2.imread("more.png")
#image = cv2.imread("other.jpg")
#image = cv2.imread("image.jpg")
rc = RedCardDetector()
rc.detect(image)
'''

image = cv2.imread("yellow_two.jpg")

yc = YellowCardDetector()
yc.detect(image)

