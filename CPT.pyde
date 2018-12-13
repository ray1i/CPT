gridx = 20
gridy = 20

class snake:
    def __init__(self, x, y, colour):
        self.x = [(s - 1) * 10 for s in x]
        self.y = [(s - 1) * 10 + 50 for s in y]
        self.colour = colour
    def draw_snake(self):
        fill(self.colour)
        for x in self.x:
            for y in self.y:
                rect(x, y, pixelsize, pixelsize)

def reset_snake1():
    return snake([2, 2, 2], [2, 3, 4], '#ff0000')
def reset_snake2():
    return snake([gridx - 1, gridx - 1, gridx - 1], [gridy - 1, gridy - 2, gridy - 3], '#0000ff')

def setup():
    global pixelsize, snake1, snake2, gridx, gridy
    size(gridx * 10, gridy * 10 + 50)
    pixelsize = width / 20
    snake1 = reset_snake1()
    snake2 = reset_snake2()

def draw():
    background(0)
    snake1.draw_snake()
    snake2.draw_snake()
