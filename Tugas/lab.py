"""
Nama    : Imanuel M.T. Manullang
NIM     : 221402036
Matkul  : Pemrograman Integrative

Soal 2:
Write a class that calculates and stores the height and weight of a person in metric. The file should be named lab.py.  BMI is calculated using this formula:
Weight/Height^2 - weight is in kilograms and height is in meters.
The class should have two properties named:
Weight
Height
The class should have two methods:
BMI_Value – This takes no arguments and returns a decimal value of the BMI
Equals – This should override the equals method from the object class to compare the weight and height of two BMI objects.  To override the equal method you should implement this method: __eq__(self, other) and return a boolean
"""

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def BMI_Value(self):
        return self.weight / (self.height ** 2)
    
    def __eq__(self, other):
        return self.weight == other.weight and self.height == other.height

# Example usage:
person1 = BMI(70, 1.75)  # Weight in kilograms, Height in meters
person2 = BMI(65, 1.70)

bmi1 = person1.BMI_Value()
bmi2 = person2.BMI_Value()

print("BMI of person1:", bmi1)
print("BMI of person2:", bmi2)

if person1 == person2:
    print("Person 1 and Person 2 have the same weight and height.")
else:
    print("Person 1 and Person 2 have different weight or height.")
