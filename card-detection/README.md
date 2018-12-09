# Card Detection

This package contains scripts to detect yellow and red card occurrences in soccer. We accomplish this by using traditional color filtering and contour processing.

### Here are the steps that we used:
  1. Convert the RGB image to HSV. We do this because the HSV color space seperates the "color" of the image from its "brightness". 
  
      See this [link](http://infohost.nmt.edu/tcc/help/pubs/colortheory/web/hsv.html) for info about the HSV color space. Also [note](https://stackoverflow.com/a/10951189) that OpenCV may have different HSV scales than other libraries.
  2. Convert the HSV image to a single channel binary image. We do this by specifying a lower and upper HSV bound for the color we want to detect. Anything outside of this bound is 0, while everything inside the bound is 255. This way, we filter out everything that is not the correct color for the object we are looking for.

    ![Original](readme_images/image.jpg)
    ![Mask](readme_images/mask.jpg)

### Libraries used:
  - OpenCV
  - Numpy
