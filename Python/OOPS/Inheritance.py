## Inhertiance
## car class blueprint
class Car:
    def __init__(self,windows,doors,enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
    def driving(self):
        print("car is used for driving")
## audi car is inherting from class car
class Audi(Car):
       def __init__(self, windows, doors, enginetype,horsepower):
            super().__init__(windows, doors, enginetype)
            self.horsepower=horsepower 
       def selfdriving(self):
            print("it is a self driving car")
audiq7=Audi(4,5,"Diesel",200) 
print(audiq7.horsepower)
print(audiq7.windows) 
audiq7.driving()         
audiq7.selfdriving()


car1=Car(4,5,"Diesel")  
print(car1)
print(audiq7)  

print(dir(audiq7)) 
print(dir(car1))     