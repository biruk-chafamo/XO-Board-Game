from graphics import *
class Visual():
    def __init__(self,x_i,y_i):
        self.x_i_i=x_i
        self.y_i = y_i
        self.box=Rectangle(Point(x_i,y_i),Point(x_i+100,y_i-100))
        self.background=Image(Point(x_i,y_i),"wood.gif")
        self.x_text=Text(Point(x_i,y_i),"X")
        self.o_text = Text(Point(x_i, y_i), "O")
        self.restart_text=Text(Point(x_i, y_i), "Restart")
        self.horizontal_line=Line(Point(x_i, y_i),Point(x_i+300, y_i))
        self.vertical_line = Line(Point(x_i, y_i), Point(x_i, y_i-300))
        self.diagonal_line_u = Line(Point(x_i, y_i), Point(x_i+300, y_i-300))
        self.diagonal_line_d = Line(Point(x_i, y_i), Point(x_i + 300, y_i + 300))
        self.o_won = Text(Point(x_i, y_i), "You win O")
        self.x_won = Text(Point(x_i, y_i), "You win x")

