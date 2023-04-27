
class Rectangle:
    def __init__(self, width , height): #Le doy los dos parámetros
        self.width = width #Creo las variables de instancia 'self.aaaa' para poder utilizarlas después en los métodos
        self.height = height
        
    def area (self): #No hace falta que le pase parámetros porqwue ya los tengo de los self.aaaa
        area = self.width * self.height
        return area #Devuelvo el valor del área para que se guarde en la variable 'area' del main, con la que llamo al método .area .
    
rectangulo = Rectangle(4, 5) #Declaro la variable rectángulo como un objeto de clase Rectangle con altura 4 y longitud 5
area = rectangulo.area() #Creo la variable 'area' y llamo al método .area con mi objeto rectángulo
print (area)