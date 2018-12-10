from train import Train
from detect import Detect

train = False

if train:
    trainer = Train("goal.mp4")
    trainer.train("goalOutput.txt", True)
else:
    detector = Detect("goalOutput.txt")
    detector.detect("goal.mp4")
