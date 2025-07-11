class Car:
    def __init__(self,windows,tyres,engine):## constructor init is nothing but constructor
        self.windows=windows## self is used for koi bhi attribute class ke under hota hai usko directly call kar skte hai
        self.tyres=tyres
        self.engine=engine
        
        
    def self_driving(self,engine):## method or a function
        print("the car type is {} engine ".format(engine))
car1=Car(4,4,"petrol")
print("The no of tyres in a car1 is {} ".format(car1.tyres))
print("The no of windows in a car1 is {} ".format(car1.windows))
#car1.self_driving()
car1.self_driving("elecrtic")