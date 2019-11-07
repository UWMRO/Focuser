## The UW MRO automated focusing system

These pages will describe the automated focusing system being developed by students in UW Astronomy Undergrad Engineering Group (AUEG).




Camera/telescope communication:
* Determine how to command the focusing mechanism via python.
  * Write python code to move the focuser.
* Determine how to command exposures from the camera via python.
  * Write python code to command an exposure.
* Determine how much of a focus move is necessary to significantly change the FWHM of an image.

Focus math:
* Collect test data of previously-acquired focus images.
* Write python class to determine the average FWHM of an image (photutils?).
* Write python class to fit a parabola to a set of points with uncertainties (scipy.optimize?).

Putting it all together:
* Write a script to take exposures while moving the focuser, fit PSFs to the images, and compute the optimum focus.
* Generate plots to monitor the output of the above.


My suggestion of a place to start would be to find a dozen or so images from a focus sequence at MRO, some above, some near, and some below focus. This will give us some test data to play with. We would also want the logbooks that go with those images, so that we can compare with the focus values measured by the observers.

I would next try to use the astropy affiliate photutils package to detect and measure point sources on each image and compute the mean full-width at half maximum (FWHM) for that image. One thing I don't know is how well photutils does on images that are fairly far from correct focus, such that the stars look more like donuts than points. This would be something to explore.



First, we can write the code to do the focusing. We can use this before we do the automating part (that communicates with the telescope).

We need our program to return a number that gives correct focus.

Pick a bright star in image, measure its FWHM,

Width of Gaussian is not the same as FWHM

Inside, outside (above, below) focus

Use 3-6 + exposures points to fit a parabola, the minimum of the parabola is the optimum focus point! Plot FWHM in pixels vs focus steps in mm.

Two ways: Measure FWHM and take the smallest value; look for the image the star is the brightest (small radius)

Note: the FWHM method does not work for “donuts” -- extremely out of focus stars.
