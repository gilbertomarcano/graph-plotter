import tkinter

from gui import GUI
from plotter import Plotter, Point2D, Line2D

def start():
    root = tkinter.Tk()
    root.geometry("640x550")
    app = GUI(root)
    root.mainloop()
    


