from tkinter import Canvas, PhotoImage, Button, NW
from plotter import Plotter, Point2D, Line2D, randline

class GUI:
    ''' GUI Class of the app
    '''

    def __init__(self, root):
        # Init a plotter and a canvas
        self.plotter = Plotter()
        self.canvas = Canvas(root, width = 680, height = 580)

        # Set the img with the file of the plotter
        self.img = PhotoImage(file=self.plotter.get_file())
        self.imgArea = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.pack()

        # Add buttons
        self.but1 = Button(root, text='random line', command=lambda: self.addline())
        self.but2 = Button(root, text='go back', command=lambda: self.delete())
        self.but1.place(x=10, y=500)
        self.but2.place(x=90, y=500)

    # Add a line to the canvas
    def addline(self):
        self.plotter.plot_line(randline())
        self.updateimg()

    # Remove the last added line
    def delete(self):
        self.plotter.delete_last()
        self.updateimg()

    # Update the image of the canvas
    def updateimg(self):
        self.img = PhotoImage(file=self.plotter.get_file())
        self.canvas.itemconfig(self.imgArea, image=self.img)
