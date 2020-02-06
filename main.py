
# GRAPH 
import matplotlib.pyplot as plt

# Point class
class Point2D:
    def __init__(self, x=0, y=0):
        self.pair = (x, y)

    def get_x(self):
        return self.pair[0]

    def get_y(self):
        return self.pair[1]

# Line class
class Line2D:
    def __init__(self, init_point=Point2D, final_point=Point2D):
        self.line = (init_point, final_point)
    
    def get_line(self):
        return self.line

# Canvas class
class Canvas:
    def __init__(self, xmin=0, ymin=0, xmax=10, ymax=10, filename='out', extension='png'):
        self.x_list = [xmin, xmax]
        self.y_list = [ymin, ymax]

        self.xlimit = xmax
        self.ylimit = ymax

        self.update()
        
        self.filename = filename
        self.extension = extension
        self.axes = plt.gca()
        self.lines = []

        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        self.dbg_count = 0
        self.rescale(xmin, ymin, xmax, ymax)

        
    
    def save(self):
        plt.savefig(self.filename + str(self.dbg_count) + '.' + self.extension)
        print(f'saved {self.dbg_count}')
        self.dbg_count += 1
    
    def get_min(self):
        self.xmin = min(self.x_list)
        self.ymin = min(self.y_list)
        return (self.xmin, self.ymin)
    
    def get_max(self):
        self.xmax = max(self.x_list)
        self.ymax = max(self.y_list)
        return (self.xmax, self.ymax)
    
    def plot_line(self, line=Line2D):
        line_tpl = line.get_line()
        x1 = line_tpl[0].get_x()
        x2 = line_tpl[1].get_x()

        y1 = line_tpl[0].get_y()
        y2 = line_tpl[1].get_y()

        self.x_list.append(x1)
        self.x_list.append(x2)

        self.y_list.append(y1)
        self.y_list.append(y2)
        
        new_line, = plt.plot((x1, x2), (y1, y2), 'k-')
        self.lines.append(new_line) 

        

        self.update()
        self.auto_rescale()

        print('line added')
        print(self.lines)

    def delete_last(self):
        line = self.lines.pop()
        self.axes.lines.remove(line)

        self.x_list.pop()
        self.x_list.pop()

        self.y_list.pop()
        self.y_list.pop()

        self.update()
        self.auto_rescale()    

        print('line deleted')
        print(self.lines)
    
    def update(self):
        self.xmin, self.ymin = self.get_min()
        self.xmax, self.ymax = self.get_max()

    def auto_rescale(self):
        xmin = self.xmin if self.xmin < 0 else 0
        xmax = self.xmax if self.xmax > self.xlimit else self.xlimit

        ymin = self.ymin if self.ymin < 0 else 0
        ymax = self.ymax if self.ymax > self.ylimit else self.ylimit

        self.rescale(xmin, ymin, xmax, ymax)

    

    def rescale(self, xmin, ymin, xmax, ymax):
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
        self.save()
    


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


