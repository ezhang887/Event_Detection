# Card Detection

This package contains scripts to detect yellow and red card occurrences in soccer. We accomplish this by using traditional color filtering and contour processing.

### Here are the steps that we used:
  1. Convert the RGB image to HSV. We do this because the HSV color space seperates the "color" of the image from its "brightness". 
  
      See this [link](http://infohost.nmt.edu/tcc/help/pubs/colortheory/web/hsv.html) for info about the HSV color space. Also [note](https://stackoverflow.com/a/10951189) that OpenCV may have different HSV scales than other libraries.
  2. 

### Libraries used:
  - OpenCV
  - Numpy
