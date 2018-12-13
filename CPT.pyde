gridx = 50
gridy = 50
pixelsize = 10
hover_clr='#ff0000'
button_normal=255

def draw_button(x, y, w, h, words):
    noStroke()
    if mouse_in_button(x, y, w, h):
        fill(hover_clr)
    else:
        fill(button_normal)
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    rect(x, y, w, h, 100)
    fill(0)
    textSize(15)
    text(words, x, y)

def mouse_in_button(x, y, w, h):
    return x - w/2 < mouseX < x + w/2 and y - h/2 < mouseY < y + h/2

def draw_title():
    fill("#ff0000")
    textSize(100)
    textAlign(CENTER)
    text("SNAKES", width/2, height/3)

class snake:
    def __init__(self, x, y, colour, dir):
        self.x = [(s - 1) * pixelsize for s in x]
        self.y = [(s - 1) * pixelsize + 50 for s in y]
        self.colour = colour
        self.dir = dir
    def draw_snake(self):
        fill(self.colour)
        stroke(0)
        rectMode(CORNER)
        for x in self.x:
            for y in self.y:
                rect(x, y, pixelsize, pixelsize)
    def move(self):
        if frameCount % 60 == 0:
            if self.dir == 'up':
                self.x.append(self.x[-1])
                self.y.append(self.y[-1] - pixelsize)
            if self.dir == 'down':
                self.x.append(self.x[-1])
                self.y.append(self.y[-1] + pixelsize)
            if self.dir == 'left':
                self.x.append(self.x[-1] - pixelsize)
                self.y.append(self.y[-1])
            if self.dir == 'right':
                self.x.append(self.x[-1] + pixelsize)
                self.y.append(self.y[-1])
            del self.x[0]
            del self.y[0]

def reset_snake1():
    return snake([2, 2, 2], [2, 3, 4], '#ff0000', 'down')
def reset_snake2():
    return snake([gridx - 1, gridx - 1, gridx - 1], [gridy - 1, gridy - 2, gridy - 3], '#0000ff', 'up')

def setup():
    global pixelsize, snake1, snake2, gridx, gridy, screen
    size(gridx * pixelsize, gridy * pixelsize + 50)
    snake1 = reset_snake1()
    snake2 = reset_snake2()
    screen = 'title'

def draw():
    global screen
    if screen == 'title':
        background(0)
        draw_title()
        draw_button(width/2, height/2, 100, 40, 'timed')
        draw_button(width/2, height/2 + 120, 140, 40, 'elimination')
    else:
        background(0)
        snake1.move()
        snake2.move()
        snake1.draw_snake()
        snake2.draw_snake()
        if screen == 'timed':
            pass
        if screen == 'elimination':
            pass

def mouseClicked():
    global screen
    if screen == 'title':
        if mouse_in_button(width/2, height/2, 100, 40):
            screen = 'timed'
        if mouse_in_button(width/2, height/2 + 120, 140, 40):
            screen = 'elimination'
