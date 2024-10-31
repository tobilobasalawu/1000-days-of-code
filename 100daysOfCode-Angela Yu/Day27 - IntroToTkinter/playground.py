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

calculate(2, add = 4, multiply = 1)