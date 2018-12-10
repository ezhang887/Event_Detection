from train import Train
from detect import Detect

train = False

if train:
    trainer = Train("train.mp4")
    trainer.train("output.txt", True)
else:
    detector = Detect("output.txt")
    detector.detect("video.mp4")
