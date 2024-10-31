def addNumbers(*args):
  print(f"Second NUmber is : {args[1]}")
  total = 0
  for i in args:
    total += i
  print(total)

addNumbers(856, 6986)