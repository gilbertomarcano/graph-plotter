from tkinter import Canvas, PhotoImage, Button, NW, Label, Entry, LEFT, RIGHT
from plotter import Plotter, Point2D, Line2D, randline

class GUI:
    ''' GUI Class of the app
    '''

    def __init__(self, root):
        # Init a plotter and a canvas
        self.root = root
        self.plotter = Plotter()
        self.canvas = Canvas(self.root, width = 680, height = 580)

        # Set the img with the file of the plotter
        self.img = PhotoImage(file=self.plotter.get_file())
        self.imgArea = self.canvas.create_image(0, 0, anchor=NW, image=self.img)
        self.canvas.pack()

        # Add buttons
        self.but_randline = Button(self.root, text='Generar una linea aleatoria', command=lambda: self.addrandline())
        self.but_removeline = Button(self.root, text='Deshacer ultima linea', command=lambda: self.delete())
        self.but_newline = Button(self.root, text='Agregar una linea', command=lambda: self.addline())
        self.but_randline.place(x=50, y=515)
        self.but_removeline.place(x=500, y=500)
        self.but_newline.place(x=80, y=485)

        self.label_x1 = Label(self.root, text='x1')
        self.label_x1.place(x=230, y=480)
        self.entry_x1 = Entry(self.root, bd=5, width='8')
        self.entry_x1.place(x=250, y=480)

        self.label_y1 = Label(self.root, text='y1')
        self.label_y1.place(x=230, y=520)
        self.entry_y1 = Entry(self.root, bd=5, width='8')
        self.entry_y1.place(x=250, y=520)

        self.label_x2 = Label(self.root, text='x2')
        self.label_x2.place(x=340, y=480)
        self.entry_x2 = Entry(self.root, bd=5, width='8')
        self.entry_x2.place(x=360, y=480)

        self.label_y2 = Label(self.root, text='y2')
        self.label_y2.place(x=340, y=520)
        self.entry_y2 = Entry(self.root, bd=5, width='8')
        self.entry_y2.place(x=360, y=520)



    # Add manually a line to the canvas
    def addline(self):
        try:
            x1 = int(self.entry_x1.get())
            x2 = int(self.entry_x2.get())
            y1 = int(self.entry_y1.get())
            y2 = int(self.entry_y2.get())
            self.plotter.plot_line(Line2D(Point2D(x1, y1), Point2D(x2, y2)))
            self.updateimg()
        except:
            pass
        finally:
            self.clear_entry()

    # Clear the entries
    def clear_entry(self):
        self.entry_x1.delete(0, 'end')
        self.entry_x2.delete(0, 'end')
        self.entry_y1.delete(0, 'end')
        self.entry_y2.delete(0, 'end')

    # Add a line to the canvas
    def addrandline(self):
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
