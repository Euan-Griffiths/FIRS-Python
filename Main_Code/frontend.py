#Frontend libiaries
import tkinter as tk # Tkinter for the projects frontend for the user
from PIL import Image, ImageTk #Import pillow to resize images in Tkinter
from backend import BackendMain as bk

class FrontendMain: # All frontend rendering 
    def __init__(self):
        
        #frontend global variables
        self.darkColour = "#444"
        self.lightColour = "#DDD"
        self.darkmode = False
        self.colour = self.lightColour
        
        self.window = tk.Tk()
        
        
        
        #Tkinter window setup
        self.window.geometry=("500x500")
        self.window.state('zoomed')
        self.window.iconbitmap(r"./MAIN_CODE/SmallLogo.ico")
        self.window.configure(background=self.colour)
        
        #Creating the window menu bar
        self.Menubar = tk.Menu()
        
        # Adding the menu bar tab varibales
        self.file_menu = tk.Menu(self.Menubar)
        self.edit_menu = tk.Menu(self.Menubar)
        self.option_menu = tk.Menu(self.Menubar)
        
        #Adding the dropdown menues; File, Edit, Options
        self.Menubar.add_cascade(menu=self.file_menu,label="File")
        self.Menubar.add_cascade(menu=self.edit_menu,label="Edit")
        self.Menubar.add_cascade(menu=self.option_menu,label="Options")
        
        #Adding the options to the file menu
        self.file_menu.add_command(label="New", command=lambda:bk.createnewInstance())
        self.file_menu.add_command(label="Save File", command=None)
        self.file_menu.add_command(label="Open local File", command=None)
        self.file_menu.add_command(label="Open Web File", command=None)
        self.file_menu.add_command(label="Exit", command=lambda:bk.quitprogram())
        
        # Adding options to the Edit menu
        self.edit_menu.add_command(label="Dark Mode",command=lambda:self.DarkmodeConfig())
        
        # Placing the menu into the frame
        self.window.config(menu=self.Menubar)
        
        #creating the main window frame for the project
        
        self.frame1 = tk.Frame(self.window)
        
        self.height = self.window.winfo_height()
        self.height = int(self.height)
        
        # adding the onload image to the window
        
        self.Image = Image.open(r"MAIN_CODE\LargeLogoGrey.png").convert('RGBA')
        
        self.scaledImage = self.Image.resize((int(float(self.height)*0.90),int(float(self.height)*0.90)))
        self.img = ImageTk.PhotoImage(self.scaledImage)
        
        self.imageplace = tk.Label(self.frame1,image=self.img)
        self.imageplace.config(background=self.colour)
        self.imageplace.grid(column=0,row=0)
        
        # adding bound sliders for image rendering
        
        self.maxbound = tk.Scale(self.frame1,from_=self.minval, to=self.maxval, orient="horizontal")
        self.maxbound.grid(row=1,column=0)
        self.maxbound.config(background=self.colour)
        
        #Config for frame 1
        
        self.frame1.config(background=self.colour)
        self.frame1.grid(row=0)
        
        #creating the bottom bar for the application 
        self.frame2 = tk.Frame(self.window)
        
        self.frame2.grid(row=1)
        self.window.mainloop()
    
    def Create_New_Instance(self):
        pass
    
    def DarkmodeConfig(self): # Sets the screen to dark mode
        
        if self.darkmode == False:
            self.darkmode= True
            self.colour = self.darkColour
        else:
            self.darkmode = False
            self.colour = self.lightColour
            
        self.window.config(background=self.colour)
        self.imageplace.config(background=self.colour)
        self.maxbound.config(background=self.colour)
        self.frame1.config(background=self.colour)
       
    def main(self):
        pass