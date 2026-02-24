# --- Import Staments ----

from astropy.io import fits # Import from the astropy libairy to be able to open local and online fits files
from matplotlib import pyplot as plt # Allows for the creation of the image and the rendering of frequancy spectra histograms
import numpy as np # Allows for the fast modification to the arrays due to the size of the arrays being between 500-20000 px wide
import tkinter as tk # Tkinter for the projects frontend for the user
from astropy.visualization import make_lupton_rgb # Lupton rgb allows for multiimage stacking for the user to generate colour images

# --- Main Code ----


    
class BackendMain():
    def __init__(self):
        pass

    def main(self):
        pass

    def Image_Spectra_Data_Formater(self):
        # Makes the Data Array 1D and sorts it in preperation for a MatPlotLib Histogram for the image spectra.
        self.data = np.array(self.data) 
        self.data = self.data.reshape(-1) 
        self.data = list(filter(lambda a: a!='nan',self.data))
        self.data.sort()
        
    def CreateImageNonLupin(self,Path,Cmap,Bounds):
        try:
            with fits.open(self.imageLink) as self.hdul: # Opens the image and gets the image Data for rendering and the Header for credits 
                self.data = self.hdul[self.location].data
                self.header = self.hdul[self.location].header
                
        except FileNotFoundError: #File Erroring handeling
            return ("Incorrect File Path")
        except:
            return("Unkown Error")
        
        try: # Image rendering and error detection
            plt.imshow(self.data,cmap=Cmap,vmin=Bounds[0],vmax=Bounds[1])
            plt.colorbar()
            self.render()
        except:
            return("Rendering Error")


class Main(BackendMain):
    def __init__(self):
        #Initalising the backend and frontend
        super().__init__()

    def main(self):
        self.frontend = FrontendMain()

class FrontendMain(Main):
    def __init__(self):
        super().__init__()
        self.colour = "#888"
        self.window = tk.Tk()
        self.window.geometry=("500x500")
        self.window.state('zoomed')
        self.window.iconbitmap("./MAIN_CODE/SmallLogo.ico")
        self.window.configure(background=self.colour)
        
        
        self.Menubar = tk.Menu()
        self.window.config(menu=self.Menubar)
        self.file_menu = tk.Menu(self.Menubar)
        self.edit_menu = tk.Menu(self.Menubar)
        self.option_menu = tk.Menu(self.Menubar)
        
        self.Menubar.add_cascade(menu=self.file_menu,label="File")
        self.Menubar.add_cascade(menu=self.edit_menu,label="Edit")
        self.Menubar.add_cascade(menu=self.option_menu,label="Options")
        
        self.file_menu.add_command(label="New", command=None)
        self.file_menu.add_command(label="Save File", command=None)
        self.file_menu.add_command(label="Open File", command=None)
        self.file_menu.add_command(label="Open Web File", command=None)
        self.file_menu.add_command(label="Exit", command=self.quitprogram())
        
        
        self.frame1 = tk.Frame(self.window)
        
        
        self.frame1.grid(row=1)
        
        self.frame2 = tk.Frame(self.window)
        
        
        self.frame2.grid(row=1)
        
        self.window.mainloop()
    
    
        
    def main(self):
        pass
    
    def quitprogram(self):
        quit()
if __name__ == "__main__":

    main = Main()
    main.main()
    