
class spectrostcopy():
    def __init__(self):
        self.array = [["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"],
                      ["nan",1,2,3,4,5,6,7,8,9,"nan"]]
        self.total_data = 0
        self.data = []

    def main(self):
        for a2ndlarray in self.array:
            values = list(filter(lambda a: a!= "nan", a2ndlarray))
            print(values)
            self.total_data += len(values)
            while len(values) != 0:
                initlen = len(values)
                target = values[0]
                values = list(filter(lambda a:a!= target,values))
                endlen = len(values)
                sublen = initlen-endlen
                targetfound = False
                for pos,dat in enumerate(self.data):
                    if dat[0] == target:
                        targetfound = True

                self.data.append([target,sublen])
                    
        
            
            
if __name__ =="__main__":
    spec = spectrostcopy()
    spec.main()