import data
import math
from data import Point


# Write your functions for each part in the space below.

# Part 1
def first_element(input:list[list[int]]) -> list[int]:
    result = [item[0] for item in input]
    return result

# Part 2
def x_coordinates(points:list[Point]) -> list[float]:
    result = [point.x for point in points]
    return result

# Part 3
def area_in_positive_quadrant(points:list[Point]) -> list[tuple[float, float]]:
    result =[(point.x, point.y) for point in points if point.x > 0 and point.y > 0]
    return result

# Part 4
def distance(point1:[Point], point2:[Point]) -> float:
    result = [round(math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2))]
    return result

# Part 5
def manhattan_distance(point1:[Point], point2:[Point]) -> list:
    result = [abs(point1.x - point2.x) + abs(point1.y - point2.y)]
    return result

# Part 6
def distance_all(points:list[Point]) -> list[int]:
    result = [round(math.sqrt(point.x**2 + point.y**2)) for point in points]
    return result


