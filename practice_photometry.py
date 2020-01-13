# start with import statements as necessary

import numpy as np  # arithmetic
import photutils # photometry
from astropy.io import fits
from astropy.stats import mad_std
from photutils import DAOStarFinder  # finding stars on image
import matplotlib.pyplot as plt  # plotting tools
import glob  # gathering images

from photutils import find_peaks  # find bright sources in image
from photutils import centroid_com  # for center of mass centroids

def star_finder(images, fwhm):  # a function to perform photometry on one or more images
    image_list = glob.glob(images)  # gather images from folder
    # get the list in a stack
    stack = []

    # extract the data and header from the fits files
    for file in image_list:
        stack.append(fits.getdata(file).astype(np.int32))  # get the array data, put it in stack                                                 
        fits.getheader(file)  # preserve the header

    for file in stack:
        bkg_sigma = mad_std(file)
        daofind = DAOStarFinder(fwhm=fwhm, threshold=80.*bkg_sigma)
        sources = daofind(file)
        
        for col in sources.colnames:
            sources[col].info.format = '%.8g'
        print(sources)
        

def find_centroid(images):  # function to find the centroids of bright points in a fits image
    imlist = glob.glob(images)
    
    for image in imlist:
        unflipped_data = fits.getdata(image).astype(np.int32)  # get the array of pixel data
        data = np.flip(unflipped_data, axis=0)  # flip to get axis correct orientation
        bkg_sigma = mad_std(data)  # for the threshold calculation, next line
        sources = find_peaks(data=data, threshold=80.*bkg_sigma, box_size=30, centroid_func=centroid_com)  # find the bright sources in the image
        
        for col in sources.colnames:
            sources[col].info.format = '%.8g'
        print(sources)
        
        source_counts = sources['peak_value']  # take the flux/counts at each source
        
        print(image)
        print('Min', np.min(source_counts))  # print the minimum counts out of all the sources
        print('Max', np.max(source_counts))  # print the maximum counts out of all the sources
        print('Mean', np.mean(source_counts))  # print the mean counts out of all the sources
        print('Standard Deviation', np.std(source_counts))  # print the standard deviation
        print()
        
        # now, to plot the images
        fig, ax = plt.subplots(1,1, figsize=(4,4))
        plt.tight_layout()
        plt.imshow(data, cmap='viridis')
        plt.colorbar()
        ax.scatter(sources['x_centroid'], sources['y_centroid'], marker='o', color='Red')  # red shows the sources found from find_peaks
        ax.set_xlabel('x pix')
        ax.set_ylabel('y pix')
        ax.set_title('Peak Sources' + ", " + image)


def peak_histogram(images):
    imlist = glob.glob(images)
    
    for image in imlist:
        data = fits.getdata(image).astype(np.int32)
            
        bkg_sigma = mad_std(data)  # for the threshold calculation, next line
        sources = find_peaks(data=data, threshold=80.*bkg_sigma, box_size=30, centroid_func=centroid_com)  # find the bright sources in the image
        source_counts = sources['peak_value']  # take the flux/counts at each source
        
        hst = np.histogram(source_counts)
        print(hst, image)
        plt.hist(source_counts, bins=8)
        plt.xlabel('Peak Counts')
        plt.ylabel('Frequency')
        plt.show()
        

def histogram(images, fwhm, threshold, parameter, bins):  # create histograms for a given parameter
    imlist = glob.glob(images)  # gather images
    
    for image in imlist:
        data = fits.getdata(image).astype(np.int32)
            
        bkg_sigma = mad_std(data)  # for the threshold calculation, next line
        daofind = DAOStarFinder(fwhm=fwhm, threshold=threshold*bkg_sigma)
        sources = daofind(data)  # stars found
        
        desired_param = sources[parameter]  # desired parameter to evaluate
        
        hst = np.histogram(desired_param)  # generate a numerical histogram
        print(hst, image)
        plt.hist(desired_param, bins=bins)  # plot the histogram
        plt.xlabel(parameter)
        plt.ylabel('Frequency')
        plt.show()
