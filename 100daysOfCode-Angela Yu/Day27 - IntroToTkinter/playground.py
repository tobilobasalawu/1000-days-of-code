def addNumbers(*args):
  print(f"Second NUmber is : {args[1]}")
  total = 0
  for i in args:
    total += i
  print(total)

#addNumbers(856, 6986)

def calculate(n, **kwargs):
#  for key,value in kwargs.items():
 #   print(value)
  n += kwargs['add']
  n *= kwargs['multiply']
  print(n)

#calculate(2, add = 4, multiply = 1)


#using class

class Car():
  def __init__(self, **kwargs):
    self.make = kwargs['make']
    self.model = kwargs['model']
    self.year = kwargs['year']
    self.color = kwargs['color']

myCar = Car(make = "BMW", model = 'i7', year = '2023', color = 'black')
print(f"Make = {myCar.make}\nModel = {myCar.model}\nYear = {myCar.year}\nColor = {myCar.color}")