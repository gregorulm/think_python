from swampy.TurtleWorld import *
from polygon import *
    
def czech_flag(canvas):
    canvas.rectangle([[-80, 50], [80, 0]],outline = None, fill='white')
    canvas.rectangle([[-80, -50], [80, 0]],outline = None, fill='red3')
    points = [[-80,-50], [-80, 50], [0, 0]]
    canvas.polygon(points, fill='blue4')

world = World()
canvas = world.ca(width=500, height=500, background='black')
czech_flag(canvas)

world.mainloop()

