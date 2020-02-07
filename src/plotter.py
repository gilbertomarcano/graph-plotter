import matplotlib.pyplot as plt

from random import randint

class Point2D:
    ''' Class that represents an Euclidean point in a two-dimensional space
    '''
    def __init__(self, x=0, y=0):
        self.ordered_pair = (x, y)

    def get_x(self):
        return self.ordered_pair[0]

    def get_y(self):
        return self.ordered_pair[1]

class Line2D:
    ''' Class that represents a line segment that is bounded by two distinct endpoints
    '''
    def __init__(self, first_endpoint=Point2D, second_endpoint=Point2D):
        self.endpoints = (first_endpoint, second_endpoint)
    
    def get_endpoints(self):
        return self.endpoints

# Plotter class
class Plotter:
    ''' Class that represents the canvas where the line segments will be plotted
    '''

    def __init__(self, xmin=0, ymin=0, xmax=10, ymax=10, filename='out', extension='png'):
        # Set the initial x's and y's and the limits of the canvas
        self.x_list = [xmin, xmax]
        self.y_list = [ymin, ymax]
        self.lines = []


        self.xlimit = xmax
        self.ylimit = ymax

        # Set the initial minimum and maximum points in the axes
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        self.axes = plt.gca()

        # Set the file properties
        self.filename = filename
        self.extension = extension

        self.update()
        self.auto_rescale()

        self.dbg_count = 0

    def get_file(self):
        return f'{self.filename}.{self.extension}';
    
    # Set and return the lowest values in the list which contains the points
    def get_min(self):
        self.xmin = min(self.x_list)
        self.ymin = min(self.y_list)
        return (self.xmin, self.ymin)
    
    # Set and return the highest values in the list which contains the points
    def get_max(self):
        self.xmax = max(self.x_list)
        self.ymax = max(self.y_list)
        return (self.xmax, self.ymax)
    
    # Plot a line in the canvas
    def plot_line(self, line=Line2D):
        points = line.get_endpoints()
        x1 = points[0].get_x()
        x2 = points[1].get_x()

        y1 = points[0].get_y()
        y2 = points[1].get_y()

        self.x_list.append(x1)
        self.x_list.append(x2)

        self.y_list.append(y1)
        self.y_list.append(y2)
        
        new_line, = plt.plot((x1, x2), (y1, y2), 'k-')
        self.lines.append(new_line) 

    
        self.update()
        self.auto_rescale()

    # Delete the last line added
    def delete_last(self):
        if self.lines:
            line = self.lines.pop()
            self.axes.lines.remove(line)

            self.x_list.pop()
            self.x_list.pop()

            self.y_list.pop()
            self.y_list.pop()

            self.update()
            self.auto_rescale() 
           

    # Update the minimum and maximum point values     
    def update(self):
        self.xmin, self.ymin = self.get_min()
        self.xmax, self.ymax = self.get_max()

    # Check for the limits and rescale the canvas
    def auto_rescale(self):
        xmin = self.xmin if self.xmin < 0 else 0
        xmax = self.xmax if self.xmax > self.xlimit else self.xlimit

        ymin = self.ymin if self.ymin < 0 else 0
        ymax = self.ymax if self.ymax > self.ylimit else self.ylimit

        self.rescale(xmin, ymin, xmax, ymax)

    # Rescale the canvas with certain points
    def rescale(self, xmin, ymin, xmax, ymax):
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)

        self.save()
    
    # Generate an updated file
    def save(self):
        plt.savefig(f'./{self.get_file()}')
        # Debug purposes
        # print(f'saved {self.dbg_count}')
        # self.dbg_count += 1

def randpoint():
    return Point2D(randint(-50, 50), randint(-50, 50))

def randline():
    return Line2D(randpoint(), randpoint())