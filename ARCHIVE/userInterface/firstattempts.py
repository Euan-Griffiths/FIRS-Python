from tkinter import *
from tkinter import ttk
#imports tkinter and the submodule ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(0.3408 * value)
    except ValueError:
        pass
    
root = Tk()
root.title("Feet to Meters")
# sets up main window where everything is operated from

mainframe = ttk.Frame(root,padding=(3,3,12,12))
# creates the main window where everything is means bg is preseverd ext 
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))

feet = StringVar()#has to belong to this class for dynamic updates 

feet_entry = ttk.Entry(mainframe,width=7,textvariable=feet)
feet_entry.grid(column=2,row=1,stick=(W,E)) # places at the correct location and connects it to the edges of that section of grid with the fixed width

#creates the var feet and sets type also creates entry widget where the user inputs values


meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W) # calls calculate function on press 

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

root.columnconfigure(0, weight=1) # states to fill all availble space 
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): #adds a gap between each element
    child.grid_configure(padx=5, pady=5)
    
feet_entry.focus()
root.bind("<Return>", calculate) # states that on press of enter key to run calculate func

root.mainloop()