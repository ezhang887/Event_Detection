import cv2
import numpy as np
import json

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
        assert(video_file == self.video_filename)
        cap = cv2.VideoCapture(video_file)
        while cap.isOpened():
            rv, frame = cap.read()
            if not rv:
                raise Exception("Bad frame in video")
            cv2.rectangle(frame,(self.x,self.y),(self.x+self.w,self.y+self.h),(0,255,0),2)
            cv2.imshow("frame", frame)
            cv2.waitKey(20)
