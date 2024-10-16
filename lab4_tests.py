import data
import lab4
import unittest
from lab4 import x_coordinates

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class TestCases(unittest.TestCase):
    # Write your test cases for each part below.

    # Part 1
    def test_first_element_1(self):
        input1 = [[1,2], [3,4]]
        result = lab4.first_element(input1)
        expected = [1, 3]
        self.assertEqual(expected, result)


    def test_first_element_2(self):
        input2 = [[-2,4,5],[4,6],[-7,23],[32,1,10]]
        result = lab4.first_element(input2)
        expected = [-2, 4, -7, 32]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        p1 = Point(1,2)
        p2 = Point(3,4)
        p3 = Point(5,6)
        points = [p1, p2, p3]
        result = lab4.x_coordinates(points)
        expected = [1, 3, 5]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        p1 = Point(-89, 553)
        p2 = Point(434, 34534)
        p3 = Point(-543, 54)
        points = [p1, p2, p3]
        result = lab4.x_coordinates(points)
        expected = [-89, 434, -543]
        self.assertEqual(expected, result)

    # Part 3
    def test_area_in_positive_quadrant(self):
        p1=Point(-98,47)
        p2=Point(24,98)
        p3=Point(23, 2323)
        points = [p1,p2,p3]
        result = lab4.area_in_positive_quadrant(points)
        expected =[(24, 98), (23, 2323)]
        self.assertEqual(expected, result)

    def test_area_in_positive_quadrant_2(self):
        p1=Point(98,47)
        p2=Point(2423424,982342)
        p3=Point(-23, -2323)
        points = [p1,p2,p3]
        result = lab4.area_in_positive_quadrant(points)
        expected =[(98,47), (2423424,982342)]
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        p1=Point(28, 52)
        p2=Point(26,29)
        result = lab4.distance(p1,p2)
        expected = [23.0]
        self.assertEqual(expected, result)

    def test_distance_2(self):
        p1 = Point(50, 50)
        p2 = Point(25, 25)
        result = lab4.distance(p1, p2)
        expected = [35.0]
        self.assertEqual(expected, result)

    # Part 5
    def test_manhattan_distance_1(self):
        p1=Point(20,52)
        p2=Point(-50, 70)
        result = lab4.manhattan_distance(p1, p2)
        expected =[88.0]
        self.assertEqual(expected, result)

    def test_manhattan_distance_2(self):
        p1=Point(40, -1)
        p2=Point(-1, 50)
        result = lab4.manhattan_distance(p1, p2)
        expected =[92.0]
        self.assertEqual(expected, result)

    # Part 6
    def test_distance_all_1(self):
        p1=Point(2,4)
        p2=Point(5,7)
        p3=Point (9,1)
        points = [p1,p2,p3]
        result = lab4.distance_all(points)
        expected=[4, 9, 9]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        p1=Point(-5,5)
        p2=Point(-9,7)
        p3=Point (0,1)
        points = [p1,p2,p3]
        result = lab4.distance_all(points)
        expected=[7, 11, 1]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
