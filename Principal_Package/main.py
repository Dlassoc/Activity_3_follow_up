from Point_class import Point
if __name__ == "__main__":
    point_1_str: str = input("Ingrese el punto 1 (x,y)")
    coordinates_point_1 = point_1_str.split(",")
    point_1: Point = Point(int(coordinates_point_1[0]), int(coordinates_point_1[1]))
    Point.move_coordinates()