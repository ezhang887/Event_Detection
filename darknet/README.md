
# Event Detection with Darknet

We used a custom dataset of Yellow Cards to create a model. The following are the results.


### Results after 10,000 Iterations 

MODEL: https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/backup/yolov3-tiny_10000.weights


#### Demo (70% confidence): 
 <p align="center">
    1)
    <img src="https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/testIMG4.jpg" width="350" alt="accessibility text">
    2)
  <img src="https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/IMG4Prediction.jpg" width="350" alt="accessibility text">
</p>


#### Demo (57% confidence): 
 <p align="center">
    1)
    <img src="https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/IMG155.jpg" width="350" alt="accessibility text">
    2)
  <img src="https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/predictions.jpg" width="350" alt="accessibility text">
</p>




### Data 


#### Number of Objects Detected
 <p align="center">
    <img src="https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/NumberOfObjects.png" alt="accessibility text">
</p>

#### Average Confidence Per Weights File
 <p align="center">
    <img src="https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/Average%20Confidence.png" alt="accessibility text">
</p>

#### Change in Confidence Per Image Per Weight File
 <p align="center">
    <img src="https://github.com/CS196Illinois/Event_Detection/blob/master/darknet/Change%20In%20Confidence.png" alt="accessibility text">
</p>





## Issues
<p>
Problem: Training was really, really slow on our computers
 
Solution: We use the ACM GPU cluster to get a faster CPU as well as use a CUDA based GPU
___
Problem: We kept running out of ram when we were training on the GPU Cluster. 

Solution: We reduced the data size
___
Problem: The results of the training were suboptimal. 

Solution: We switched from normal darknet and moved to darknet-tiny which worked better given the computing hardware at our disposal. 
___

Problem: Weights file needs a GPU to run

Solution: A CUDA gpu would be needed in order to use the weights in realtime. 
</p>







  
