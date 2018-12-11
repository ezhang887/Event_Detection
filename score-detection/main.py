from train import Train
from detect import Detect

train = False

if train:
    trainer = Train("TrimmedFiles/OrigGoal.mp4")
    trainer.train("TrimmedFiles/Orig.txt", True)
else:
    detector = Detect("TrimmedFiles/Orig.txt")
    detector.detect("TrimmedFiles/OrigGoal.mp4")
