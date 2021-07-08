# inheritance 



class Vehicle:
    def general_vehical(self):
        print("general use: Transpotation")
        
class Car(Vehicle):
    def __init__(self):
        print("i am a car")
        self.wheel = 4
        self.has_roof = True
        
    def specific_usage(self):
        print("specific use : vacation with family")
        
class MotorCycle(Vehicle):
    def __init__(self):
        print("i am MotorCycle")
        self.wheel = 2
        self.has_roof = True
        
    def specific_usage(self):
        print("specific use : Raccing, road trip")
        
c = Car()
c.general_vehical()
c.specific_usage()


m = MotorCycle()
m.general_vehical()
m.specific_usage()
