from detect import *
import cv2
import os
import glob

def main():
    while True:
        detector = YellowCardDetector()
        os.chdir("./yellow")
        for f in glob.glob("*.jpg"):
            detector.detect(cv2.imread(f), 3)
        for f in glob.glob("*.png"):
            detector.detect(cv2.imread(f), 3)
        detector = RedCardDetector()
        os.chdir("../red")
        for f in glob.glob("*.jpg"):
            detector.detect(cv2.imread(f), 3)
        for f in glob.glob("*.png"):
            detector.detect(cv2.imread(f), 3)
        os.chdir("../")


def test():
    detector = YellowCardDetector()
    detector.detect(cv2.imread("yellow/3.jpg"), 10000, True)


if __name__ == "__main__":
    test()
