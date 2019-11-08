# The UW MRO automated focusing system

These pages will describe the automated focusing system being developed by students in UW Astronomy Undergrad Engineering Group (AUEG). We are writing in python. There are two ways to achieve focusing:  
a) measure FWHM and take the smallest value  
b) look for the brightest pixels in the image to calculate radius of star and go from there

## Here is a list of steps to take, in order:

### Focus math
* Collect test data of previously-acquired focus images
* Write python class to determine the average FWHM of an image (use photutils?)
* Write python class to fit a parabola to a set of points with uncertainties (use scipy.optimize?)

### Camera/telescope communication
* Determine how to command the focusing mechanism
  * Write python code to move the focuser
* Determine how to command exposures from the camera
  * Write python code to command an exposure
* Determine how much of a focus move is necessary to significantly change the FWHM of an image.

### Putting it all together
* Write a script to take exposures while moving the focuser
* Fit PSFs to the images
* Compute the optimum focus
* Generate plots to monitor the output of the above

## Detailed explanation

### Focus math
* Find a dozen or so images from a focus sequence at MRO (with logbooks), with some above, some near, and some below focus. This will give us some test data to play with. Logbooks are necessary to compare with the focus values measured by the observers.

* Use the astropy affiliate photutils package to detect and measure point sources on each image, compute the mean full-width at half maximum (FWHM) for that image.

* Write the code to do the focusing. This will be done before the automating part (that communicates with the telescope).

Our program needs to: 
  * Pick a bright star in image, measure its FWHM (keep in mind that width of Gaussian is not the same as FWHM)
  * Inside, outside (above, below) focus
  * Use 3-6 + exposures points to fit a parabola, the minimum of the parabola is the optimum focus point
  * Plot FWHM in pixels vs focus steps in mm
  * Return a number that gives correct focus

Note: the FWHM method does not work for “donuts” -- extremely out of focus stars.
