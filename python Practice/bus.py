from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self,vehicleType,doors,wheels,capacity):
        super().__init__(vehicleType)
        self.doors = doors
        self.wheels = wheels
        self.capacity = capacity
    def toString(self):
        print('VehicleType:',self.vehicleType,'Doors:',self.doors,'Wheels:', self.wheels, 'MaxCapacity:',self.capacity)
