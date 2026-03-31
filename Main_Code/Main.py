# --- Import Staments ----
#Fits Operations
from astropy.io import fits # Import from the astropy libairy to be able to open local and online fits files
from astropy.visualization import make_lupton_rgb # Lupton rgb allows for multiimage stacking for the user to generate colour images
#Data Operations and viuslisations
from matplotlib import pyplot as plt # Allows for the creation of the image and the rendering of frequancy spectra histograms
from numpy import array # Allows for the fast modification to the arrays due to the size of the arrays being between 500-20000 px wide
#Frontend
import tkinter as tk # Tkinter for the projects frontend for the user
from PIL import Image, ImageTk #Import pillow to resize images in Tkinter

# --- Main Code ----


    
class BackendMain(): #backend for FITS rendering code

    def __init__(self):
        pass

    def main(self):
        pass

    def Image_Spectra_Data_Formater(self):
        # Makes the Data Array 1D and sorts it in preperation for a MatPlotLib Histogram for the image spectra.
        self.data = array(self.data) 
        self.data = self.data.reshape(-1) 
        self.data = list(filter(lambda a: a!='nan',self.data))
        self.data.sort()
        
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
            plt.imshow(self.data,cmap=Cmap,vmin=Bounds[0],vmax=Bounds[1])
            plt.colorbar()
            self.render()
        except:
            return("Rendering Error")



class Main(BackendMain): #Main code used for all misc functions

    def __init__(self):
        #Inherting the backend
        super().__init__()

    def main(self):
        self.frontend = FrontendMain()
        self.frontend.Create_New_Instance()
        
    def quitprogram(self): # sub function to end the application when run in the menu bar
        quit()



class FrontendMain(Main): # All frontend rendering 
    def __init__(self):
        super().__init__() # Inherits Main and Backend main
        

        #Class global variables
        self.darkColour = "#888"
        self.lightColour = "#BBB"
        self.window = tk.Tk()
        self.darkmode = False
        self.colour = self.lightColour
        #Tkinter window setup
        self.window.geometry=("500x500")
        self.window.state('zoomed')
        self.window.iconbitmap("./MAIN_CODE/SmallLogo.ico")
        self.window.configure(background=self.colour)
        
        #Creating the window menu bar
        self.Menubar = tk.Menu()
        
        
        self.file_menu = tk.Menu(self.Menubar)
        self.edit_menu = tk.Menu(self.Menubar)
        self.option_menu = tk.Menu(self.Menubar)
        
        #Adding the dropdown menues; File, Edit, Options
        self.Menubar.add_cascade(menu=self.file_menu,label="File")
        self.Menubar.add_cascade(menu=self.edit_menu,label="Edit")
        self.Menubar.add_cascade(menu=self.option_menu,label="Options")
        
        #Adding the options to the file menu
        self.file_menu.add_command(label="New", command=lambda:self.createnewInstance())
        self.file_menu.add_command(label="Save File", command=None)
        self.file_menu.add_command(label="Open local File", command=None)
        self.file_menu.add_command(label="Open Web File", command=None)
        self.file_menu.add_command(label="Exit", command=lambda:self.quitprogram())
        
        self.edit_menu.add_command(label="Dark Mode",command=lambda:self.DarkmodeConfig())
        
        self.window.config(menu=self.Menubar)
        
        #creating the main window frame for the project
        
        self.frame1 = tk.Frame(self.window)
        self.orignalImage = Image.open("MAIN_CODE\LargeLogoGrey.png")
        self.height = self.window.winfo_height()
        self.height = int(self.height)
        self.imageRescale = self.orignalImage.resize((int(float(self.height)*0.90),int(float(self.height)*0.90)))
        self.img = ImageTk.PhotoImage(self.imageRescale)
        self.imageplace = tk.Label(self.frame1,image=self.img)
        self.imageplace.config(background=self.colour)
        self.imageplace.grid(column=0,row=0)
        
        self.frame1.grid(row=0)
        
        #creating the bottom bar for the application 
        self.frame2 = tk.Frame(self.window)
        
        
        self.frame2.grid(row=1)
        self.window.mainloop()
    
    def Create_New_Instance(self):
        pass
    
    def DarkmodeConfig(self):
        if self.darkmode == False:
            self.colour = self.darkColour
            self.darkmode= True
        else:
            self.darkmode = False
            self.colour = self.lightColour
        self.window.update()
    def main(self):
        pass

        
if __name__ == "__main__":
    main = Main()
    main.main()
    