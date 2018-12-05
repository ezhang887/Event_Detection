import cv2
import numpy as np
import os

class Train:

    def __init__(self, filename):
        cap = cv2.VideoCapture(filename)

        self.frames = []
        i = 0
        while i < 1000:
            rv, frame = cap.read()
            if not rv:
                break
            #cv2.imshow("frame", frame)
            cv2.waitKey(10)
            self.frames.append(frame)

        self.height, self.width, self.channels = self.frames[0].shape

        self.green_thresh = 80
        self.diff_thresh = 50
        self.perc = 0.1

    def dist(self, dest, src):
        val = abs(dest[0]-src[0]) + abs(dest[1]-src[1]) + abs(dest[2]-src[2])
        #val = abs(dest-src)
        return val

    def max_rgb(self, frame):
        max_r, max_g, max_b = 0,0,0
        for x in range(self.width):
            for y in range(self.height):
                curr = frame[y,x]
                max_r = max(curr[0], max_r)
                max_g = max(curr[1], max_g)
                max_b = max(curr[2], max_b)
        return max_r, max_g, max_b

    def preprocess(self, frame):
        #pre-processing: filter the grass
        filtered_frame = frame.copy()
        max_r, max_g, max_b = self.max_rgb(frame)
        for x in range(self.width):
            for y in range(self.height):
                curr = frame[y,x]
                if curr[1] > self.green_thresh and curr[0]>max_r*self.perc and curr[1]>max_g*self.perc and curr[2]>max_b*self.perc:
                    filtered_frame[y,x] = [0,0,0]
                else:
                    filtered_frame[y,x] = [255,255,255]
        filtered_frame = cv2.cvtColor(filtered_frame, cv2.COLOR_BGR2GRAY)
        return filtered_frame

    def morphology_expansion(self, y, x, filtered_frame, pre_morph):
        if pre_morph[y,x] != 255:
            return filtered_frame
        for i in range(-2, 3):
            for j in range(-2, 3):
                in_height = y+i>0 and y+i <= self.height-1
                in_width = x+j>=0 and x+j <= self.width-1
                if in_height and in_width:
                    filtered_frame[y+i][x+j] = 255 
                if in_height and not in_width:
                    filtered_frame[y+i][x] = 255
                if in_width and not in_height:
                    filtered_frame[y][x+j] = 255
        return filtered_frame

    def find_rect(self, frame):
        _, thresh = cv2.threshold(frame, 254, 255, 0)
        _, contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

        contour = contours[0]
        max_area = 0
        for c in contours:
            if cv2.contourArea(c) > max_area:
                contour = c
                max_area = cv2.contourArea(c)

        rect = cv2.boundingRect(c)
        return rect

    def train(self, start_frame, end_frame):
        #create training frames
        training_frames = self.frames[start_frame:end_frame]

        filtered_frame = self.preprocess(training_frames[0])
        cv2.imshow("frame", training_frames[0])
        cv2.imshow("filtered", filtered_frame)

        #main processing
        prev_frame = None
        for i in range(1,len(training_frames)):
            frame = training_frames[i]
            if prev_frame is None:
                prev_frame = frame
                continue
            for x in range(self.width):
                for y in range(self.height):
                    curr = frame[y,x]
                    
                    if self.dist(curr.tolist(), prev_frame[y,x].tolist()) < self.diff_thresh and filtered_frame[y,x] == 255:
                        filtered_frame[y,x] = 255
                    else:
                        filtered_frame[y,x] = 0
            cv2.imshow("frame", frame)
            cv2.imshow("filtered", filtered_frame)
            cv2.waitKey(10)
            prev_frame = frame

        pre_morph_frame = filtered_frame.copy()
        for i in range(self.width):
            for j in range(self.height):
                filtered_frame = self.morphology_expansion(j, i, filtered_frame, pre_morph_frame)
        rect = self.find_rect(filtered_frame)
        x,y,w,h = rect
        cv2.rectangle(filtered_frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        while True:
            cv2.imshow("frame", frame)
            cv2.imshow("pre_morph", pre_morph_frame)
            cv2.imshow("filtered", filtered_frame)
            cv2.waitKey(10)
        cv2.destroyAllWindows()
