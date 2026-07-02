class Car():
    total_car=0
    def __init__(self,brand,model):
        self.brand= brand
        self.__model= model
        Car.total_car+=1

    def get_model(self):
        return self.__model

    def horn(self,target):
        return f"{self.brand} is honking towards {target.brand}."

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size= battery_size

    def fuel_type(self):
        return "Electric Charge"

car1= Car("BMW","X1")
car2=Car("Toyota","Corolla")
car3=Car("TATA","Safari")
car4= Car("Maruti-Suzuki","800")

print(car1.horn(car2))

electric_car1= ElectricCar("Tesla","Model-S","83KWh")

print(electric_car1.get_model())

print(electric_car1.horn(car4))

print(car1.fuel_type())
print(electric_car1.fuel_type())

print(car1.total_car)

print(Car.total_car)