import matplotlib.pyplot as plt
import numpy
class spectrostcopy():
    def __init__(self):
        self.data = [[5,0,3,3,7,9,3,'nan',2,4,7,6],
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
    def render(self):
        self.data = numpy.array(self.data)
        self.data = self.data.reshape(-1)
        self.data = list(filter(lambda a: a!='nan',self.data))
        self.data.sort()
        plt.hist(self.data,bins=6,color='skyblue',edgecolor='black')
        plt.xlabel('Values')
        plt.ylabel('Frequency')
        plt.title('Basic Histogram')
        plt.show()

spec = spectrostcopy()
spec.render()