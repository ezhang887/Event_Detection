from train import Train
from detect import Detect

train = True

if train:
    trainer = Train("Basketball.mp4")
    trainer.train("output.txt", False)
else:
    detector = Detect("output.txt")
    detector.detect("Basketball.mp4")
