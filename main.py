import matplotlib.pyplot as plt

# Main class of the program
def main():
    canvas = Canvas(filename='graph')
    p0 = Point2D(0, 2)
    p1 = Point2D(5, 9)
    l0 = Line2D(p0, p1)
    canvas.plot_line(l0)

    canvas.plot_line(Line2D(Point2D(6, 9), Point2D(13, 0)))
    canvas.delete_last()

    canvas.plot_line(Line2D(Point2D(20, 10), Point2D(30, 80)))
    canvas.plot_line(Line2D(Point2D(-50, -34), Point2D(-30, 4)))

    canvas.delete_last()
    canvas.delete_last()

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

# Canvas class
class Canvas:
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
        self.update()
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        self.axes = plt.gca()

        # Set the file properties
        self.filename = filename
        self.extension = extension

        self.dbg_count = 0
    
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
        plt.savefig(self.filename + str(self.dbg_count) + '.' + self.extension)
        # Debug purposes
        print(f'saved {self.dbg_count}')
        self.dbg_count += 1
    
if __name__ == '__main__':
    main()



