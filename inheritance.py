class vehicle:
    def general_usage(self):
        print('general use: transportation')
class Car(vehicle):
    def __init__(self):
        print("I am car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        self.general_usage()
        print("Specific use: commute to work, vacation with family")
class MotorCycle(vehicle):
    def __init__(self):
        print("I am a motorcycle")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip, racing")
c = Car()
c.specific_usage()

m = MotorCycle()
m.specific_usage()

print(isinstance(c, MotorCycle))
print(issubclass(Car, MotorCycle))
