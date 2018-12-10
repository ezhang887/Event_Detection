import cv2
import numpy as np
import json
import pytesseract
import PIL

class Detect:
    
    def __init__(self, data_file):
        self.data_file = data_file
        try:
            with open(data_file) as json_data:
                d = json.load(json_data)
                self.x = d["x"]
                self.y = d["y"]
                self.w = d["w"]
                self.h = d["h"]
                self.video_filename = d["video_filename"]
        except IOError:
            print("There was an error opening your data file!")
            return

    def detect(self, video_file):
        cap = cv2.VideoCapture(video_file)

        prev_cropped_frame = None
        while cap.isOpened():
            rv, frame = cap.read()
            if not rv:
                raise Exception("Bad frame in video")
            cropped_frame = frame[self.y:self.y+self.h, self.x:self.x+self.w]
            resized = cv2.resize(cropped_frame,(int(100/self.h*self.w),100))
            hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
            low = np.array([0,0,140])
            high = np.array([360,150,255])
            mask = cv2.inRange(hsv, low, high)
            cv2.imshow("hsv", hsv)
            cv2.imshow("mask", mask)
            delta = self.delta(cropped_frame, prev_cropped_frame)
            prev_cropped_frame = cropped_frame
            cv2.rectangle(frame,(self.x,self.y),(self.x+self.w,self.y+self.h),(0,255,0),1)
            cv2.imshow("frame", frame)
            print(pytesseract.image_to_string(PIL.Image.fromarray(mask)))
            cv2.waitKey(20)
