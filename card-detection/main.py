from detect import CardDetector
import cv2

#image = cv2.imread("more.png")
#image = cv2.imread("other.jpg")
image = cv2.imread("image.jpg")

c = CardDetector()
c.detect_red(image)
