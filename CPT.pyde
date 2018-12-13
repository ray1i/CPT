gridx = 50
gridy = 50
hover_clr='#ff0000'
button_normal=255

# Button timed
def draw_button_timed(x, y, w, h):
    if mouse_in_button(x, y, w, h):
        noStroke()
        fill(hover_clr)
        rect(x, y, w, h, 100)
    else: 
        noStroke()
        fill(button_normal)
        rect(x, y, w, h, 100)
    fill(0)
    textSize(15)
    text("timed mode", width/2, height/2 + 20)

# Button elimination
def draw_button_elimination(x, y, w, h):
    if mouse_in_button(x, y, w, h):
        noStroke()
        fill(hover_clr)
        rect(x, y, w, h, 100)
    else:
        noStroke()
        fill(button_normal)
        rect(x, y, w, h, 100)
    fill(0)
    textSize(15)
    text("elimination mode", width/2, height/2 + 140)

def mouse_in_button(x, y, w, h):
    return mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h

# Title
def draw_title():
    fill("#ff0000")
    textSize(100)
    textAlign(CENTER)
    text("SNAKES", width/2, height/3)

class snake:
    def __init__(self, x, y, colour):
        self.x = [(s - 1) * 10 for s in x]
        self.y = [(s - 1) * 10 + 50 for s in y]
        self.colour = colour
    def draw_snake(self):
        fill(self.colour)
        stroke(0)
        for x in self.x:
            for y in self.y:
                rect(x, y, pixelsize, pixelsize)

def reset_snake1():
    return snake([2, 2, 2], [2, 3, 4], '#ff0000')
def reset_snake2():
    return snake([gridx - 1, gridx - 1, gridx - 1], [gridy - 1, gridy - 2, gridy - 3], '#0000ff')

def setup():
    global pixelsize, snake1, snake2, gridx, gridy, screen
    size(gridx * 10, gridy * 10 + 50)
    pixelsize = width / gridx
    snake1 = reset_snake1()
    snake2 = reset_snake2()
    screen = 'title'

def draw():
    global screen
    if screen == 'title':
        background(0)
        draw_title()
        draw_button_timed(width/2 - 50, height/2, 100, 40)
        draw_button_elimination(width/2 - 70, height/2 + 120, 140, 40)
    else:
        background(0)
        snake1.draw_snake()
        snake2.draw_snake()
        if screen == 'timed':
            pass
        if screen == 'slimination':
            pass

def mouseClicked():
    global screen
    if screen == 'title':
        if mouse_in_button(width/2 - 50, height/2, 100, 40):
            screen = 'timed'
        if mouse_in_button(width/2 - 70, height/2 + 120, 140, 40):
            screen = 'elimination'

