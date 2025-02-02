#  write a function that takes variable number of argument and returns their sum


def sum_all(*args):
   return sum(args)

print(sum_all(12,1,2,23,2,3,23))