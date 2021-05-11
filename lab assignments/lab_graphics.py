from graphics import GraphWin, Polygon, Text, Point, Rectangle
import math
def main():
	win = GraphWin("Draw a simple house")
	win.setCoords(0.0, 0.0, 10.0, 10.0)
	message = Text(Point(5, 0.5),"Click on two points")
	message.draw(win)
	p1 = win.getMouse()
	p2 = win.getMouse()
	rectangle = Rectangle(p1, p2)
	rectangle.draw(win)
	win.getMouse()
	p1_x = p.getX()
	p1_y = p.getY()
	p2_x = p.getX()
	width = p2_x - p1_x
	message = Text(Point(5, 0.5),"Click on one points")
	message.draw(win)
	p3 = win.getMouse()
	p3_x = p.getX()
	door_left = Point(p3_x-width*(1/5),p1_y)
	door_right = Point(p3_x+width*(1/5),p1_y)
	rectangle_door = Rectangle(door_left,door_right)
	rectangle_door.draw(win)
