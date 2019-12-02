from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,vehicleType,doors,wheels,carType,maker):
        super().__init__(vehicleType)
        self.doors = doors
        self.wheels = wheels
        self.carType = carType
        self.maker = maker
    def toString(self):
        print('VehicleType:',self.vehicleType,'Doors:',self.doors,'Wheels:', self.wheels, 'CarType:', self.carType, 'Maker:',self.maker)
