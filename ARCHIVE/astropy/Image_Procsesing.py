from astropy.io import fits
from matplotlib import pyplot as plt
import numpy as np


class Main():
    def __init__(self):
        #General Information
        self.imageLink = r"FITS_IMAGES\ESA\502nmos.fits" 
        self.location = 0
        
        #List for image rendering
        self.cmap = "CMRmap"
        self.lowerbound = 0
        self.upperbound = 70
        
        #Lists for credit
        Orginisations = [["NRAO",'ALMA','EVLA','GBT','GMVA','VLA','VLBA','Arecibo'],
                         ['NASA/ESA','HUBBLE'],['NASA/ESA/CSA','JWST']]
        
    
    def main(self):
        
        try:
            with fits.open(self.imageLink) as self.hdul: # Opens the image and gets the image Data for rendering and the Header for credits 
                self.data = self.hdul[self.location].data
                self.header = self.hdul[self.location].header
                
        except FileNotFoundError: #File Erroring handeling
            return ("Incorrect File Path")
        except:
            return("Unkown Error")
        
        try: # Image rendering and error detection
            plt.imshow(self.data,cmap=self.cmap,vmin=self.lowerbound,vmax=self.upperbound)
            plt.colorbar()
            self.render()
        except:
            return("Rendering Error")
        
            
    def render(self):
        plt.show()
    
    def credit_generator(self):
        pass
    
if __name__ == "__main__":
    main = Main()
    main.main()