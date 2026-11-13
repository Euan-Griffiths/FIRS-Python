#Fits Operations
from astropy.io import fits # Import from the astropy libairy to be able to open local and online fits files
from astropy.visualization import make_lupton_rgb # Lupton rgb allows for multiimage stacking for the user to generate colour images

#Data Operations and visulisations
from matplotlib import pyplot as plt # Allows for the creation of the image and the rendering of frequancy spectra histograms
from numpy import array # Allows for the fast modification to the arrays due to the size of the arrays being between 500-20000 px wide


class mainBackend: # All backend operations for the project
    def __init__(self):
        pass


    def quitprogram(self): # Quits the program
        import sys
        sys.exit()

    def openfits(self, file_path): # Opens the fits file and returns the data and header
        with fits.open(file_path) as hdul:
            data = hdul[0].data
            header = hdul[0].header
        return data, header