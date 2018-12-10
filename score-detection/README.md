# Score Detection

This package contains scripts to detect goals scored in soccer. We accomplish this by using traditional color filtering, region detection, and optical character recognition.

### Here are the steps that we used:
  1. Go through the image pixel by pixel and filter out any pixels in the first frame that have too much green. This serves to instantly eliminate all the grass and much of the audience and players.
  
  2. Go through the video frame by frame and eliminate the pixels that change as the video progresses. At the end only pixels that have remained relatively the same will remain (i.e. the scoreboard).
  
    Now we have something that looks like this:
  
  3. Afterwards, we expand the scoreboard and use pytesseract to convert the image to a string.

### Libraries used:
  - OpenCV
  - Numpy
  - Pytesseract
