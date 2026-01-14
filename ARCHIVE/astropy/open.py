from astropy.io import fits
from matplotlib import pyplot as plt
import numpy
from tqdm import tqdm

hdul = fits.open(r"502nmos.fits")
info = hdul[0].header
data = hdul[0].data

print(data.shape)

#data = numpy.reshape(data,(1600, 1600))
print(f"Data Shape (NAXIS,NAXIS1): {data.shape}")

plt.imshow(data, cmap="CMRmap",vmin=0,vmax=70)
plt.colorbar()
plt.show()
input()
hdul.close()

# --------------------


class spectrostcopy():
    def __init__(self):
        hdul = fits.open(r"502nmos.fits")
        self.arrays = hdul[0].data
        hdul.close()
        self.total_data = 0
        self.data = []
    def render(self):
        self.arrays = numpy.array(self.arrays)
        self.arrays = self.arrays.reshape(-1)
        self.arrays = list(filter(lambda a: a!='nan',self.arrays))
        self.arrays.sort()
        plt.hist(self.arrays,bins=1000,color='skyblue',edgecolor='black')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Basic Histogram')
        plt.show()
    #def main(self):
    #    for array in tqdm(self.arrays):
    #        
    #        values = list(filter(lambda a: a!= "nan", array)) # Removes all nan values from the data
    #        
    #        self.total_data += len(values) # gets total amount of data to caculate a precentage, for the amount of wavelength emmisions at #that value
    #        
    #        while len(values) != 0:
    #            initlen = len(values) # gets current length of the array of values
    #            target = values[0] # gets current first value of the array to check the rest of the array
    #            
    #            values = list(filter(lambda a:a!= target,values)) # Removes all instances of the target from the array
    #            
    #            endlen = len(values) 
    #            sublen = initlen-endlen # finds how much data has been removed from the array, giving the frequancy of the removed value
    #            
    #            targetfound = False
    #            for pos,dat in enumerate(tqdm(self.data)): #Checks if the value being added to the data array is already in the array
    #                if dat[0] == target:
    #                    targetfound = True
    #                    break
    #                
    #            if targetfound == False:
    #                self.data.append([target,sublen]) # adds the target and frequany into the data  array
    #                
    #            if targetfound == True: # increase the sum of the frequancy of the target when it alreadys exists in the array
    #                sublen += self.data[pos][1]
    #                self.data.pop(pos)
    #                self.data.append([target,sublen])
    #    self.percentages()
    #    print(self.data) 
    #    self.sortdata()
    #
    #def percentages(self): # turns the data in to percentages for the graph
    #    print(self.total_data)
    #    for i,dat in enumerate(self.data):
    #        self.data[i][1] = round(dat[1]/self.total_data*100)
    #      
    #def sortdata(self):
    #    self.data.sort(key=lambda a:a[0]) # sorts the data array based on the target value
    #    print(self.data)
    #        
            
if __name__ =="__main__":
    spec = spectrostcopy()
    spec.render()