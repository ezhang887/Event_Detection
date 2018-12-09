import cv2
import numpy as np
import json

class Train:

    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)
        _, self.initial_frame = self.cap.read()
        self.filename = filename

        self.height, self.width, self.channels = self.initial_frame.shape

        self.green_thresh = 80
        self.diff_thresh = 60
        self.perc = 0.075

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
        for i in range(-1, 2):
            for j in range(-1, 2):
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

    def train(self, output_filename, display_image = True):
        print("Preprocessing...")
        filtered_frame = self.preprocess(self.initial_frame)
        if display_image:
            cv2.imshow("frame", self.initial_frame)
            cv2.imshow("filtered", filtered_frame)
        print("Done reprocessing...")

        print("Running main filter...")
        #main processing
        prev_frame = None
        rv = True
        while rv:
            rv, frame = self.cap.read()
            if not rv:
                break
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
            if display_image:
                cv2.imshow("frame", frame)
                cv2.imshow("filtered", filtered_frame)
                cv2.waitKey(10)
            prev_frame = frame
        print("Done running main filer...")

        print("Postprocessing...")
        pre_morph_frame = filtered_frame.copy()
        for i in range(self.width):
            for j in range(self.height):
                filtered_frame = self.morphology_expansion(j, i, filtered_frame, pre_morph_frame)
        print("Done postprocessing")

        print("Finding box")
        rect = self.find_rect(filtered_frame)
        x,y,w,h = rect
        y += 1
        h -= 2
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        print("Done finding box")

        data = {}
        data["video_filename"] = self.filename
        data["x"] = x
        data["y"] = y
        data["w"] = w
        data["h"] = h

        self.trained_data = data

        with open(output_filename, "w") as outfile:
            json.dump(data, outfile)
            outfile.write("\n")
        outfile.close()
        print("Saved data to file")
