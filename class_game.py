from class_visual import Visual
from graphics import *
class Game():
    def __init__(self,win,height,width):
        self.win=win
        self.height=height
        self.width=width
        self.box_centers = []
        self.box_maker()
        self.o_centers=[]
        self.x_centers=[]
        self.starterplayer = "o"

        #self.o()
        self.text = None
        self.defeat=bool
        self.player_o = 0
        self.player_x = 0

        self.starter()
    def starter(self):
        surrounding_l = Rectangle(Point(20, 250), Point(180, 20))
        surrounding_r = Rectangle(Point(980, 250), Point(820, 20))
        if self.starterplayer == "o":
            self.starterplayer = "x"
            surrounding_l.setFill(color_rgb(70, 150, 30))
            surrounding_l.draw(self.win)
            surrounding_r.setFill(color_rgb(200, 60, 30))
            surrounding_r.draw(self.win)
            self.draw_text("Starter", 30, "white", 100, 50)
            self.draw_text("Player O", 35, "white", 100, 100)
            self.draw_text("Player X", 35, "white", 900, 100)
            self.draw_text(str(self.player_o), 30, "white", 100, 200)
            self.draw_text(str(self.player_x), 30, "white", 900, 200)
            self.o()
        else:
            self.starterplayer = "o"
            surrounding_l.setFill(color_rgb(200, 60, 30))
            surrounding_l.draw(self.win)
            surrounding_r.setFill(color_rgb(70, 150, 30))
            surrounding_r.draw(self.win)
            self.draw_text("Starter", 30, "white", 900, 50)
            self.draw_text("Player O", 35, "white", 100, 100)
            self.draw_text("Player X", 35, "white", 900, 100)
            self.draw_text(str(self.player_o), 30, "white", 100, 200)
            self.draw_text(str(self.player_x), 30, "white", 900, 200)
            self.x()
    def draw_text(self,text, size, color,x,y):
        t = Text(Point(x, y), text)
        t.setSize(size)
        t.setFill(color)
        t.draw(self.win)

    def box_maker(self):
        background=Visual(self.width/2,self.height/2).background
        background.draw(self.win)
        for i in range(3):
            y_i = (500) - i * 100
            x_i = 350
            for j in range(3):
                box = Visual(x_i+j*100, y_i).box
                box.setFill(color_rgb(70, 60, 30))
                box.setOutline('white')
                box.setWidth(7)
                self.box_centers.append(box.getCenter())
                box.draw(self.win)

    def x(self):
        drawn=False
        clickpoint = self.win.getMouse()
        for i in self.box_centers:
            if clickpoint.getY() < i.getY() + 50 and clickpoint.getX() < i.getX() + 50 and clickpoint.getY() > i.getY() - 50 and clickpoint.getX() > i.getX() - 50:
                    text = Visual(i.getX(), i.getY()).x_text
                    self.box_centers.remove(i)
                    self.x_centers.append(text.getAnchor())
                    text.setSize(35)
                    text.setFill('white')
                    text.draw(self.win)
                    self.checker()
                    drawn=True
        if drawn:
            self.o()
        else:
            self.x()
    def o(self):
        drawn=False
        clickpoint = self.win.getMouse()
        for i in self.box_centers:
            if clickpoint.getY() < i.getY() + 50 and clickpoint.getX() < i.getX() + 50 and clickpoint.getY() > i.getY() - 50 and clickpoint.getX() > i.getX() - 50:
                    text = Visual(i.getX(), i.getY()).o_text
                    self.box_centers.remove(i)
                    self.o_centers.append(text.getAnchor())
                    text.setSize(35)
                    text.setFill('white')
                    text.draw(self.win)
                    self.checker()
                    drawn = True
        if drawn:
            self.x()
        else:
            self.o()

    def checker(self):
        for i in self.x_centers:
            x_score_up, x_score_horizontal, x_score_diagonal_u, x_score_diagonal_d  = 0, 0, 0, 0
            for j in self.x_centers:
                if i.getX() == j.getX():
                    x_score_up += 1
                    if x_score_up==3:
                        line=Visual(i.getX(),500).vertical_line
                        line.setOutline('red')
                        line.setWidth(15)
                        line.draw(self.win)
                if i.getY() == j.getY():
                    x_score_horizontal += 1
                    if x_score_horizontal==3:
                        line=Visual(350,i.getY()).horizontal_line
                        line.setOutline('red')
                        line.setWidth(15)
                        line.draw(self.win)
                if i.getX() == j.getX() - 100 and i.getY() == j.getY() + 100 or i.getX() == j.getX() + 100 and i.getY() == j.getY() - 100:
                    x_score_diagonal_u += 1
                if i.getX() == j.getX() - 100 and i.getY() == j.getY() - 100 or i.getX() == j.getX() + 100 and i.getY() == j.getY() + 100:
                    x_score_diagonal_d += 1
                if x_score_diagonal_u == 2:
                    line=Visual(350,500).diagonal_line_u
                    line.setOutline('red')
                    line.setWidth(15)
                    line.draw(self.win)
                if x_score_diagonal_d == 2:
                    line = Visual(350, 200).diagonal_line_d
                    line.setOutline('red')
                    line.setWidth(15)
                    line.draw(self.win)
                if x_score_up == 3 or x_score_horizontal == 3 or x_score_diagonal_u == 2 or x_score_diagonal_d == 2:
                    self.text = Visual(self.width / 2, self.height / 10).x_won
                    self.text.setSize(35)
                    self.text.setFill('white')
                    self.text.setStyle("bold")
                    self.text.draw(self.win)
                    self.defeat = True
                    self.player_x += 1
                    self.restart()
        for i in self.o_centers:
            o_score_up, o_score_horizontal, o_score_diagonal_u, o_score_diagonal_d = 0, 0, 0, 0
            for j in self.o_centers:
                if i.getX() == j.getX():
                    o_score_up += 1
                    if o_score_up==3:
                        line=Visual(i.getX(),500).vertical_line
                        line.setOutline('red')
                        line.setWidth(15)
                        line.draw(self.win)
                if i.getY() == j.getY():
                    o_score_horizontal += 1
                    if o_score_horizontal==3:
                        line=Visual(350,i.getY()).horizontal_line
                        line.setOutline('red')
                        line.setWidth(15)
                        line.draw(self.win)
                if i.getX() == j.getX() - 100 and i.getY() == j.getY() + 100 or i.getX() == j.getX() + 100 and i.getY() == j.getY() - 100:
                    o_score_diagonal_u += 1
                if i.getX() == j.getX() - 100 and i.getY() == j.getY() - 100 or i.getX() == j.getX() + 100 and i.getY() == j.getY() + 100:
                    o_score_diagonal_d += 1
                if o_score_diagonal_u == 2:
                    line=Visual(350,500).diagonal_line_u
                    line.setOutline('red')
                    line.setWidth(15)
                    line.draw(self.win)
                if o_score_diagonal_d == 2:
                    line = Visual(350, 200).diagonal_line_d
                    line.setOutline('red')
                    line.setWidth(15)
                    line.draw(self.win)
                if o_score_up == 3 or o_score_horizontal == 3 or o_score_diagonal_u == 2 or o_score_diagonal_d == 2:
                    self.text = Visual(self.width / 2, self.height / 10).o_won
                    self.text.setSize(35)
                    self.text.setFill('white')
                    self.text.setStyle("bold")
                    self.text.draw(self.win)
                    self.defeat = True
                    self.player_o += 1
                    self.restart()
        if len(self.o_centers)+len(self.x_centers)==9:
            self.defeat = False
            self.restart()
    def restart(self):
        restart_button=Visual(450,650).box
        restart_button.setFill('red')
        restart_text=Visual(500,600).restart_text
        restart_text.setFill('white')
        restart_text.setSize(25)
        restart_button.draw(self.win)
        restart_text.draw(self.win)
        center=restart_button.getCenter()
        clickpoint = self.win.getMouse()
        if clickpoint.getY() < center.getY() + 50 and clickpoint.getX() < center.getX() + 50 and clickpoint.getY() > center.getY() - 50 and clickpoint.getX() > center.getX() - 50:
            if self.defeat==True:
                self.text.undraw()
            self.box_centers = []
            self.box_maker()
            self.o_centers = []
            self.x_centers = []
            self.starter()
            #self.o()
            self.text = None






