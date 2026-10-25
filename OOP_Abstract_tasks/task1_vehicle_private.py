class Vehicle():
    count=0
    def __init__(self, name, max_speed, mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
        Vehicle.count+=1
        self.__car_id=Vehicle.count

    @property
    def car_id(self):
        return self.__car_id

    @car_id.setter
    def car_id(self, car_id):
        if car_id is int:
            self.__car_id=car_id
        else:
             raise ValueError("The car ID must be a number.")

    def vehicle_capacity(self, capacity):
         return f"The vehicle's capacity is {capacity}."

    def __repr__(self):
        return f"Class Vehicle: name={self.name}, max_speed={self.max_speed}, mileage={self.mileage}."

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        self.vehicle_type="Bus"
    def __repr__(self):
            return f"Class Bus: name={self.name}, max_speed={self.max_speed}, mileage={self.mileage}."
    

class Train(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        self.vehicle_type="Train"
    def __repr__(self):
            return f"Class Train: name={self.name}, max_speed={self.max_speed}, mileage={self.mileage}."
