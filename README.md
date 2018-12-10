# CS 196 - Event Detection (formerly Camera Mesh Network)
FA18 project for CS 196 focused on event detection/recognition.

The goal of this project is to detect events from a video recording of an event. We have implented 3 approaches to solve this problem. 

1) YOLO v3 Object Detection
2) Color Filtering 
3) Optical Character Recognition of Overlays

## YOLO v3 Object Detection
  YOLO v3 is a neural net which seeks to identify objects in an image if they exist. In this project we decided to see if Yellow Cards existed in an image/video. A model for this did not exist so we used darknet to train our own model. The output of this training is https://github.com/CS196Illinois/Event_Detection/tree/master/darknet/backup. This model can be used to identify yellow cards in still images or videos. 
  
For more information go to https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/README.md

  
  
  
## Color Filtering
  Color filtering analyzes each frame of a video and filters for just the color yellow. Because jerseys of soccer players can be yellow as well there is another layer of filtering. This layer is to see the general shape and infil of the yellow area. If the area is too large, or has a lot of noise it will not be identified as a yellow card. 
  
 For more information go to https://github.com/CS196Illinois/Event_Detection/blob/master/card-detection/README.md
 
 
 ## Optical Character Recognition of Overlays
   For sporting events there are often overlays that are updated in realtime as a game is played. In soccer there is a graphical overlay that show the number of goals scored by each team. By writing a software that reads that graphic we can determine if a team scores a goal, and which team scores a goal. 
   
 
 
  
  
