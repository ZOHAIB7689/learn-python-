# create a function that returns both the area and circumstances of  a circle given its radius
import math
def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference = 2 *math.pi * radius
    return area , circumference
radius = int(input("enter your circle area : "))

a,c = circle_stats(radius)
print("area: ", round(a,2), "circumference: ", round(c,2))