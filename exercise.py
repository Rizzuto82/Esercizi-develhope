class Animal:
    def __init__(self, animal, count_leg):
        self.animal = animal
        self.count_leg = count_leg
        print("animal object was created")

    def runs(self):
        print("Running started")    

animal1 = Animal("dog", 4)       
animal1.runs() 


       




    

