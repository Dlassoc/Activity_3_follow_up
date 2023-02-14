from Point_class import Point


class Rectangle:
    def __init__(self, point_1, point_2):
        self.point_1: Point = point_1
        self.point_2: Point = point_2

    def calculate_perimeter(self) -> float:
        base = abs(self.point_2.x - self.point_1.x)
        high = abs(self.point_2.y - self.point_1.y)
        return (base + high) * 2

    def is_square(self) -> bool:
        base = abs(self.point_2.x - self.point_1.x)
        high = abs(self.point_2.y - self.point_1.y)
        return base == high
