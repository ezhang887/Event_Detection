from train import Train
from detect import Detect

'''
trainer = Train("video.mp4")
trainer.train(200, 300, "output.txt", False)
'''

detector = Detect("output.txt")
detector.detect("video.mp4")
