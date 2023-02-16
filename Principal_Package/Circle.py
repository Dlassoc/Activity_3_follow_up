#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
import math
from Point_class import Point


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def circle_area(self) -> float:
        area = 3.1416 * self.radius ** 2
        return area

    def circle_perimeter(self) -> float:
        perimeter = 2 * 3.1416 * self.radius
        return perimeter

    def is_a_point_in_circle_or_not(self, x: Point, y: Point):
        is_or_no: float = math.sqrt(((x - self.center.x) ** 2 ( y - self.center.y))**2)
        return is_or_no >= self.radius
