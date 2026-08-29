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


class imagerenders(BackendMain):
    def __init__(self):
        super().__init__()
        
    def Create_Image_Non_Lupin_RGB(self,Path,Cmap,Bounds):
        
        try:
            with fits.open(self.imageLink) as self.hdul: # Opens the image and gets the image Data for rendering and the Header for credits 
                self.data = self.hdul[self.location].data
                self.header = self.hdul[self.location].header
                
        except FileNotFoundError: #File Erroring handeling
            return ("Incorrect File Path")
        
        except:
            return("Unkown Error")
        
        try: # Image rendering and error detection
            plt.imshow(self.data,cmap=Cmap,vmin=Bounds[self.lowerBound/100],vmax=Bounds[self.upperBound]/100)
            plt.colorbar()
            self.render()
            
        except:
            return("Rendering Error")