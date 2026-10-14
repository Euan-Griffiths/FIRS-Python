#Fits Operations
from astropy.io import fits # Import from the astropy libairy to be able to open local and online fits files
from astropy.visualization import make_lupton_rgb # Lupton rgb allows for multiimage stacking for the user to generate colour images

#Data Operations and visulisations
from matplotlib import pyplot as plt # Allows for the creation of the image and the rendering of frequancy spectra histograms
from numpy import array # Allows for the fast modification to the arrays due to the size of the arrays being between 500-20000 px wide

class BackendMain(): #backend for FITS rendering code

    def __init__(self):
        # backend global varibles
        self.minval = 0
        self.maxval = 100
        self.lowerBound = self.minval
        self.upperBound = self.maxval
        self.data = []
        self.header = ""

    def main(self):
        pass

    def Image_Spectra_Data_Formater(self):
        # Makes the Data Array 1D and sorts it in preperation for a MatPlotLib Histogram for the image spectra.
        self.data = array(self.data) 
        self.data = self.data.reshape(-1) 
        self.data = list(filter(lambda a: a!='nan',self.data))
        self.data.sort()
    
    def quitprogram():
        quit()


