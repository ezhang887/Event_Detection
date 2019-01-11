# CS 196 - Event Detection (formerly Camera Mesh Network)
FA18 project for CS 196 focused on event detection/recognition. We decided to focus on sports events, specifically soccer.

**Note: This repository was imported from the original [CS196Illinois](https://github.com/CS196Illinois) organization after the semester ended and the original repository was made private.**

## YOLO Object Detection
  [YOLO](https://pjreddie.com/darknet/yolo/) is a real-time detection algorithm developed for object detection. We used [darknet](https://pjreddie.com/darknet/) (a neural network using YOLO) to detect yellow cards from soccer matches in an image/video. The pretrained models did not suppert this feature, so we ended up training a custom model for this. 
  
  Our trained weights are located [here](https://github.com/CS196Illinois/Event_Detection/tree/master/darknet/backup). This model can be used to identify yellow cards in still images or videos. 
  
Click [here](https://github.com/CS196Illinois/Event_Detection/blob/master/darknet) for more information.
 
## Color Filtering and Blob Detection
  This package analyzes each frame of a video and filteres the pixels for the desired color and shape. Traditional computer vision techniques are used here, such as HSV filtering and contour/blob processing. This is an alternative to YOLO for detecting events with yellow cards.
  
Click [here](https://github.com/CS196Illinois/Event_Detection/blob/master/card-detection) for more information.
 
 ## Optical Character Recognition of Overlays
   In sporting events there are almost always scoring overlays that are updated in real-time as the match goes on. Our solution to detect when goals were scored in soccer uses this fact. We used color filtering to detect where the overlay was in a video, and then used optical character recognition to figure out what the scores are and when they change.
   
Click [here](https://github.com/CS196Illinois/Event_Detection/blob/master/score-detection) for more information.

#### Team members:
  - Akhil Isanaka
  - Himanshu Minocha
  - Eric Zhang
  
#### Special thanks to:
  - Omar Khan
  - Sathwik Pochampally
  
