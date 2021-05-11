"""CSC 161 Lab: Simlation & Design

Ningyuan Xiong
Lab Section TR 12:30-1:45pm
Spring 2019
"""


def main():
    print("Simulation of two dimensional random walk")
    walks = eval(input("How many walks should I do?"))
    steps = eval(input("How many steps should I take on each?"))
    distances = distance(steps,walks)
    print("Average distance from start:{0:0.2f}".format(distances))

def distance(steps,walks):
    import math
    x = 1
    x_direction = 0
    y_direction = 0
    from graphics import GraphWin, Point, Line
    Win = GraphWin()
    m = 100
    n = 100
    origin_point = Point(m, n)
    origin_point.draw(Win)
    while x <= walks:
        direction = random_walk_2d()
        x = x + 1
        if direction == 1:
            x_direction = x_direction + steps
            line = Line(Point(m,n),Point(m+steps,n))
            m = m + steps
        elif direction == 3:
            x_direction = x_direction - steps
            line = Line(Point(m,n),Point(m-steps,n))
            m = m - steps
        elif direction == 2:
            y_direction = y_direction + steps
            line = Line(Point(m,n),Point(m,n+steps))
            n = n + steps
        else:
            y_direction = y_direction - steps
            line = Line(Point(m,n),Point(m,n-steps))
            n = n - steps
        line.draw(Win)
    distance = math.sqrt((x_direction)**2+(y_direction)**2)
    return distance


def random_walk_2d():
    import random
    directions = random.randrange(1,5)
    return directions

main()

