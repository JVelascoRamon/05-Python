import math #librería para utilizar el número pi

class Circle: #Si hay dudas, ver los comentarios del 01.py , que es igual
    def __init__(self, radius): 
        self.radius = radius
        
    def area (self):
        area = math.pi * math.pow(self.radius , 2) #Otra forma de hacer una potencia de exponente 2
        return area
    
circulo = Circle(2)
area = circulo.area()
print (math.pi)
print (area)