

class Car :
    total_car = 0


    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1
    def full_name(self):
        return f"{self.__brand}, {self.__model}"    
    def get_brand(self):
        return self.__brand + "!"
    def fuel_type(self):
        return "Petrol or Diesel "
    @staticmethod
    def general_des():
        return "Cars are means of transport "
    @property
    def model(self):
        return self.__model
    




my_car = Car("toyota","corolla")
my_new_car = Car("Lamborghini", "Urus")
print(my_new_car.full_name())
# print(my_car.brand , my_car.model)



class ElectricCar(Car):
    def __init__(self, brand, __model, battery_size):
        super().__init__(brand, __model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electric Charge"

my_tesla = ElectricCar("Tesla","Model S" , "45kwh" )
print(my_tesla.full_name())



print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))

cybertruck = ElectricCar("Tesla", "CyberTruck", "45kwh")
print(cybertruck.fuel_type())
print(Car.total_car)



class Battery:
    def battery_info(self):
        return "this car contains battery"

class Engine:
    def Engine_info(self):
        return "this car contains engine"

class ElectricCarTwo(Battery,Engine, Car):
    pass


me_new_tesla = ElectricCarTwo("Tesla" , "Model S")
print(me_new_tesla.Engine_info())
print(me_new_tesla.battery_info())