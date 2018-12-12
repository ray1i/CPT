class snake:
    def __init__(self, x, y, colour):
        self.x = [(s * 10) for s in x]
        self.y = [(s *10) + 50 for s in y]
        self.colour = colour
    def draw_snake(self):
        fill(self.colour)
        for x in self.x:
            for y in self.y:
                rect(x, y, pixelsize, pixelsize)

snake1 = snake([2, 2, 2], [2, 3, 4], '#ff0000')
snake2 = snake([48, 48, 48], [48, 47, 46], '#0000ff')

def setup():
    global pixelsize
    size(500, 550)
    pixelsize = width / 50

def draw():
    background(0)
    snake1.draw_snake()
    snake2.draw_snake()
