#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def circle_area(self):
        area = 3.1416 * self.radius ** 2
        return area

    def circle_perimeter(self):
        perimeter = 2 * 3.1416 * self.radius
        return perimeter

    def is_in_circle_or_not(self, x, y):
        is_or_no = (x + y)**2
        if is_or_no == self.radius:
            return "Pertenece al circulo"
        else:
            return "No pertenece al circulo"
