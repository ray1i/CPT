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
    snake1 = snake([2, 2, 2], [2, 3, 4], '#ff0000')
def reset_snake2():
    snake2 = snake([49, 49, 49], [49, 48, 47], '#0000ff')

def setup():
    global pixelsize, snake1, snake2
    size(20 * 10, 20 * 10 + 50)
    pixelsize = width / 20
    snake1 = []
    snake2 = []

def draw():
    background(0)
    reset_snake1()
    reset_snake2()
    snake1.draw_snake()
    snake2.draw_snake()
