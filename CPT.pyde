import random

gridx = 50
gridy = 50
pixelsize = 10
hud_height = (gridx * pixelsize) / 10
button_normal = 255
hover_clr = 200
time_limit = 180

def draw_button(x, y, w, h, words):
    noStroke()
    if mouse_in(x, y, w, h):
        fill(hover_clr)
    else:
        fill(button_normal)
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    rect(x, y, w, h, 100)
    fill(0)
    textSize(h / 2)
    text(words, x, y)

def mouse_in(x, y, w, h):
    return x - w/2 < mouseX < x + w/2 and y - h/2 < mouseY < y + h/2

def draw_title():
    fill(255)
    textSize(100)
    textAlign(CENTER)
    text("SNAKES", width/2, height/3)

class snake:
    def __init__(self, x, y, colour, dir, score):
        self.x = [(s - 1) * pixelsize for s in x]
        self.y = [(s - 1) * pixelsize + hud_height for s in y]
        self.colour = colour
        self.dir = dir
        self.score = score
    def draw_snake(self):
        fill(self.colour)
        stroke(0)
        rectMode(CORNER)
        for i in range(len(self.x)):
            rect(self.x[i], self.y[i], pixelsize, pixelsize)
    def move(self):
        if frameCount % 10 == 0:
            del self.x[0]
            del self.y[0]
            if self.dir == 'up':
                self.x.append(self.x[-1])
                if self.y[-1] - pixelsize < hud_height:
                    self.y.append(self.y[-1] - pixelsize + height - hud_height)
                else:
                    self.y.append(self.y[-1] - pixelsize)
            if self.dir == 'down':
                self.x.append(self.x[-1])
                if self.y[-1] + pixelsize >= height:
                    self.y.append(self.y[-1] + pixelsize - height + hud_height)
                else:
                    self.y.append(self.y[-1] + pixelsize)
            if self.dir == 'left':
                self.y.append(self.y[-1])
                if self.x[-1] - pixelsize < 0:
                    self.x.append(self.x[-1] - pixelsize + width)
                else:
                    self.x.append(self.x[-1] - pixelsize)
            if self.dir == 'right':
                self.y.append(self.y[-1])
                if self.x[-1] + pixelsize >= width:
                    self.x.append(self.x[-1] + pixelsize - width)
                else:
                    self.x.append(self.x[-1] + pixelsize)

def reset_snake1():
    return snake([2, 2, 2], [2, 3, 4], '#ff0000', 'down', 0)
def reset_snake2():
    return snake([gridx - 1, gridx - 1, gridx - 1], [gridy - 1, gridy - 2, gridy - 3], '#0000ff', 'up', 0)

class food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw_food(self):
        fill(255)
        rectMode(CORNER)
        rect(self.x, self.y, pixelsize, pixelsize)
    def make_food(self):
        self.x = random.randint(0, gridx) * pixelsize
        self.y = random.randint(0, gridy) * pixelsize + hud_height
food = food(random.randint(0, gridx) * pixelsize, random.randint(0, gridy) * pixelsize + hud_height)

def draw_hud():
    fill(255)
    rect(0, 0, width, hud_height)
    
    fill(0)
    textSize(hud_height)
    textAlign(LEFT, CENTER)
    text(snake1.score, 0, hud_height / 2)
    textAlign(RIGHT, CENTER)
    text(snake2.score, width, hud_height / 2)

def draw_timer():
    global time, screen
    if frameCount % 60 ==0:
        time -= 1
    
    fill(0)
    textSize(40)
    textAlign(CENTER, CENTER)
    #text(time, width / 2, hud_height / 2)
    text("{}:{}{}".format(time // 60, time % 60 // 10, time % 10), width/2, 20)
    if time <= 0:
        screen = 'end'

def setup():
    global snake1, snake2, screen
    size(gridx * pixelsize, gridy * pixelsize + hud_height)
    snake1 = reset_snake1()
    snake2 = reset_snake2()
    screen = 'title'

def draw():
    global screen
    if screen == 'title':
        background(0)
        draw_title()
        draw_button(width/2, height/2, 400, 100, 'TIMED')
        draw_button(width/2, height/2 + 120, 400, 100, 'ELIMINATION')
    elif screen == 'end':
        draw_button(width/2, height/2 + 100, 400, 100, 'NEW GAME')
        fill(255)
        textSize(40)
        text("{}, WIN".format("Nothing"), width/2, height/3)
    else:
        background(0)
        food.draw_food()
        snake1.draw_snake()
        snake2.draw_snake()
        snake1.move()
        snake2.move()
        draw_hud()
        if screen == 'timed':
            draw_timer()
        if screen == 'elimination':
            pass

def mouseClicked():
    global screen, time
    if screen == 'title':
        if mouse_in(width/2, height/2, 400, 100):
            screen = 'timed'
            time = time_limit
        if mouse_in(width/2, height/2 + 120, 400, 100):
            screen = 'elimination'
    elif screen == 'end':
        if mouse_in(width/2, height/2 + 100, 400, 100):
            screen = 'title'

def keyPressed():
    global snake1, snake2
    if key == 'w' or key == 'W':
        snake1.dir = 'up'
    if key == 's' or key == 'S':
        snake1.dir = 'down'
    if key == 'a' or key == 'A':
        snake1.dir = 'left'
    if key == 'd' or key == 'D':
        snake1.dir = 'right'
    if keyCode == UP:
        snake2.dir = 'up'
    if keyCode == DOWN:
        snake2.dir = 'down'
    if keyCode == LEFT:
        snake2.dir = 'left'
    if keyCode == RIGHT:
        snake2.dir = 'right'
