import tkinter

from gui import GUI
from plotter import Plotter, Point2D, Line2D

# Main class of the program
def main():
    root = tkinter.Tk()
    root.geometry("640x550")
    app = GUI(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()



