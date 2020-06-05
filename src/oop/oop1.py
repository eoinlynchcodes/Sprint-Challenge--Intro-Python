Oop1 

# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# This is the base class
class Vechicle:
    def __init__(self, carries_people):
        self.carries_people = carries_people


class GroundVehicle(Vechicle):
    def __init__(self, carries_people, number_of_wheels):
        super.__init__(carries_people, number_of_wheels)

class Car(GroundVehicle):
    def __init__(self, carries_people, number_of_wheels):
        super.__init__(carries_people, number_of_wheels)

class Motorcycle(GroundVehicle):
    def __init__(self, carries_people, number_of_wheels, eoin_would_drive):
        super.__init__(carries_people, number_of_wheels)
        self.eoin_would_drive = eoin_would_drive


class FlightVehicle(Vechicle):
    def __init__(self, carries_people, has_wings):
        super.__init__(carries_people)
        self.has_wings = has_wings

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass
