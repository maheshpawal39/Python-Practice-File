import math

def circle_status(radius):
    area =  math.pi * radius ** 2
    Cercomference = 2 * math.pi * radius
    return area , Cercomference

a , c = circle_status(30)
print("Area :", a , "Cercomference" , c)