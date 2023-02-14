import math


class Point:
    def __init__(self, point_x: int, point_y: int):
        self.point_x: int = point_x
        self.point_y: int = point_y

    def show_coordinates(self) -> tuple:
        return self.point_x, self.point_y

    def move_coordinates(self, how_much_move_the_point_in_x, how_much_move_the_point_in_y):
        self.point_x = how_much_move_the_point_in_x + self.point_x
        self.point_y = how_much_move_the_point_in_y + self.point_y

    def calculate_distance(self, other_point) -> tuple:
        dist = math.sqrt((other_point.x - self.point_x) ** 2) + ((other_point.y - self.point_y) ** 2)
        return dist


