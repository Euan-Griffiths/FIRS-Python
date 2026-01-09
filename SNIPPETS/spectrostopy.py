
class spectrostcopy():
    def __init__(self):
        self.arrays = [[5,0,3,3,7,9,3,'nan',2,4,7,6],
                       [8,8,1,6,7,7,8,1,5,9,8,9],
                       [4,3,0,'nan','nan',0,2,'nan',8,1,3,'nan'],
                       ['nan',7,0,1,9,'nan',0,4,7,3,'nan',7],
                       [2,0,0,4,'nan','nan',6,8,4,'nan',4,'nan'],
                       [8,1,1,7,9,9,3,6,7,2,0,3],
                       [5,9,4,4,'nan',4,4,3,4,4,8,4],
                       [3,7,5,5,0,1,5,9,'nan','nan',5,0],
                       [1,2,4,2,0,3,2,0,7,5,9,0],
                       ['nan',7,2,9,2,3,3,'nan',3,4,1,2],
                       [9,1,4,6,8,2,3,0,0,6,0,6],
                       [3,3,8,8,8,2,3,2,0,8,8,3]]

        self.total_data = 0
        self.data = []

    def main(self):
        for array in self.arrays:
            
            values = list(filter(lambda a: a!= "nan", array)) # Removes all nan values from the data
            
            self.total_data += len(values) # gets total amount of data to caculate a precentage, for the amount of wavelength emmisions at that value
            
            while len(values) != 0:
                initlen = len(values) # gets current length of the array of values
                target = values[0] # gets current first value of the array to check the rest of the array
                
                values = list(filter(lambda a:a!= target,values)) # Removes all instances of the target from the array
                
                endlen = len(values) 
                sublen = initlen-endlen # finds how much data has been removed from the array, giving the frequancy of the removed value
                
                targetfound = False
                for pos,dat in enumerate(self.data): #Checks if the value being added to the data array is already in the array
                    if dat[0] == target:
                        targetfound = True
                        break
                    
                if targetfound == False:
                    self.data.append([target,sublen]) # adds the target and frequany into the data  array
                    
                if targetfound == True: # increase the sum of the frequancy of the target when it alreadys exists in the array
                    sublen += self.data[pos][1]
                    self.data.pop(pos)
                    self.data.append([target,sublen])
        self.percentages()
        print(self.data) 
        self.sortdata()
    
    def percentages(self): # turns the data in to percentages for the graph
        print(self.total_data)
        for i,dat in enumerate(self.data):
            self.data[i][1] = round(dat[1]/self.total_data*100)
          
    def sortdata(self):
        self.data.sort(key=lambda a:a[0]) # sorts the data array based on the target value
        print(self.data)
            
            
if __name__ =="__main__":
    spec = spectrostcopy()
    spec.main()