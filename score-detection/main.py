from train import Train
from detect import Detect

train = False

if train:
    trainer = Train("TrimmedFiles/Champsgoal.mp4")
    trainer.train("TrimmedFiles/Champs.txt", True)
else:
    detector = Detect("TrimmedFiles/Champs.txt")
    detector.detect("TrimmedFiles/Champsgoal.mp4")
