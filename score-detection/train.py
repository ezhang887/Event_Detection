import cv2
import numpy as np
import json

class Train:

    def __init__(self, filename):
        self.cap = cv2.VideoCapture(filename)
        _, self.initial_frame = self.cap.read()
        self.filename = filename

        self.height, self.width, self.channels = self.initial_frame.shape

        #parameters for filtering
        self.green_thresh = 80
        self.diff_thresh = 60
        self.perc = 0.075

    #returns the "distance" between two pixels
    def dist(self, dest, src):
        val = abs(dest[0]-src[0]) + abs(dest[1]-src[1]) + abs(dest[2]-src[2])
        return val

    #returns the max rgb values of a frame
    def max_rgb(self, frame):
        max_r, max_g, max_b = 0,0,0
        for x in range(self.width):
            for y in range(self.height):
                curr = frame[y,x]
                max_r = max(curr[0], max_r)
                max_g = max(curr[1], max_g)
                max_b = max(curr[2], max_b)
        return max_r, max_g, max_b

    #preprocessing step: filters out the grass on the soccer field and returns a filtered frame
    def preprocess(self, frame):
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

    #performs a morphology expansion on the image
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

    #find the rectangle given the processsed binary image
    def find_rect(self, frame):
        _, contours, _ = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contour = contours[0]
        max_area = 0
        for c in contours:
            if cv2.contourArea(c) > max_area:
                contour = c
                max_area = cv2.contourArea(c)

        rect = cv2.boundingRect(contour)
        return rect

    def num_white_pixels(self, frame):
        rv = 0
        for x in range(self.width):
            for y in range(self.height):
                if frame[y,x] == 255:
                    rv+=1
        return rv

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
            num_pix = self.num_white_pixels(filtered_frame)
            if num_pix < 1000:
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
        print(rect)
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

        while display_image:
            cv2.imshow("frame", frame)
            cv2.imshow("filtered", filtered_frame)
            cv2.waitKey(10)
