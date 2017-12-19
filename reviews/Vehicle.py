# Review about object and class, getter and setter
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank,seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    @property
    def number_of_wheels(self):
        return self.number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.number_of_wheels = number

    def make_noise(self):
        print('VRUMMMMMMM')


tesla = Vehicle(4, 'Electric', 5, 250)
print(tesla.number_of_wheels)
tesla.number_of_wheels = 2
print(tesla.number_of_wheels)
tesla.make_noise()