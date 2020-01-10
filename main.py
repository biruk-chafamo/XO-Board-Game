from class_game import Game
from graphics import *
def main():
    height=700
    width=1000
    win=GraphWin("xo Game",width,height)
    Game(win,height,width)
    win.getKey()
main()