from tkinter import * 
from tkinter import ttk  # Importing Tkinter to creater the UI
from astropy.io import fits # Importing Astropy to be able to open FITS files in python
from matplotlib import pyplot as plt # Importing MatPlotLib to render the images from the data recived from the FITS files
import numpy #Used to resive the data from the files to create the images, by reducing the size of the arrays as they can be 3D or 4D as FITS can Include Time/Maximum Amplitude or can create 3D images due to the seperate positions of the telescopes in the Array

class Main():
    def __init__(self,root):
        root.title("Fits File Converter (FFC)")
        mainframe = ttk.Frame(root,padding=(3,3,12,12))
        mainframe.grid(column=0,row=0,sticky=(N,E,S,W))
        ttk.Label(mainframe,text="A Fits Image Visuliser In Python.",padding=(10,10,10,10)).grid(column=0,row=1,sticky=(W,E,N))
        
    
    def getDimension(self):
        pass
    
root =Tk()
Main(root)
root.mainloop()