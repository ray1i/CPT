import random

gridx = 50
gridy = 50
pixelsize = 10
hud_height = (gridx * pixelsize) / 10
button_normal = 255
hover_clr = 200
time_limit = 180
game_over = False

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
    def __init__(self, x, y, colour, dir):
        self.x = [(s - 1) * pixelsize for s in x]
        self.y = [(s - 1) * pixelsize + hud_height for s in y]
        self.colour = colour
        self.dir = dir
        self.changedir = 0
        self.score = 0
    def draw_snake(self):
        fill(self.colour)
        stroke(0)
        rectMode(CORNER)
        for i in range(len(self.x)):
            rect(self.x[i], self.y[i], pixelsize, pixelsize)
    def del_end(self):
        del self.x[0]
        del self.y[0]
    def grow(self):
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
    def food_collide(self, x, y):
        return self.x[-1] == x and self.y[-1] == y
    def snake_collide(self, other_x, other_y):
        for x in range(len(other_x) - 1):
            for y in range(len(other_y) - 1):
                if self.x[-1] == other_x[x] and self.y[-1] == other_y[y]:
                    return True
    def control(self, snake):
        if snake == 1:
            if key == 'w' or key == 'W':
                if self.dir == 'down':
                    pass
                else:
                    self.changedir = 'up'
            if key == 's' or key == 'S':
                if self.dir == 'up':
                    pass
                else:
                    self.changedir = 'down'
            if key == 'a' or key == 'A':
                if self.dir == 'right':
                    pass
                else:
                    self.changedir = 'left'
            if key == 'd' or key == 'D':
                if self.dir == 'left':
                    pass
                else:
                    self.changedir = 'right'
        if snake == 2:
            if keyCode == UP:
                if snake2.dir == 'down':
                    return snake2.dir
                else:
                    return 'up'
            if keyCode == DOWN:
                if snake2.dir == 'up':
                    return snake2.dir
                else:
                    return 'down'
            if keyCode == LEFT:
                if snake2.dir == 'right':
                    return snake2.dir
                else:
                    return 'left'
            if keyCode == RIGHT:
                if snake2.dir == 'left':
                    return snake2.dir
                else:
                    return 'right'

def reset_snake1():
    return snake([2, 2, 2], [2, 3, 4], '#ff0000', 'down')
def reset_snake2():
    return snake([gridx - 1, gridx - 1, gridx - 1], [gridy - 1, gridy - 2, gridy - 3], '#0000ff', 'up')

class food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw_food(self):
        fill(255)
        rectMode(CORNER)
        rect(self.x, self.y, pixelsize, pixelsize)
    def make_food(self):
        self.x = random.randint(1, gridx - 1) * pixelsize
        self.y = random.randint(1, gridy - 1) * pixelsize + hud_height
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
    global time, screen, game_over
    if frameCount % 60 ==0:
        time -= 1
    
    fill(0)
    textSize(40)
    textAlign(CENTER, CENTER)
    #text(time, width / 2, hud_height / 2)
    text("{}:{}{}".format(time // 60, time % 60 // 10, time % 10), width/2, 20)
    if time <= 0:
        game_over = True

def winner():
    if screen == 'timed':
        if snake1.score < snake2.score:
            return 'BLUE'
        elif snake1.score == snake2.score:
            return 'NO ONE'
        else:
            return 'RED'
    if screen == 'elimination':
        if snake1.snake_collide(snake2.x, snake2.y) and snake2.snake_collide(snake1.x, snake1.y):
            return 'NO ONE'
        elif snake1.snake_collide(snake2.x, snake2.y) or snake1.snake_collide(snake1.x, snake1.y):
            return 'BLUE'
        elif snake2.snake_collide(snake1.x, snake1.y) or snake2.snake_collide(snake2.x, snake2.y):
            return 'RED'
            
def setup():
    global snake1, snake2, screen
    size(gridx * pixelsize, gridy * pixelsize + hud_height)
    snake1 = reset_snake1()
    snake2 = reset_snake2()
    snake1.score = 0
    snake2.score = 0
    screen = 'title'

def draw():
    global snake1, snake2, screen, game_over
    if screen == 'title':
        background(0)
        draw_title()
        draw_button(width/2, height/2, 400, 100, 'TIMED')
        draw_button(width/2, height/2 + 120, 400, 100, 'ELIMINATION')
    elif game_over:
        draw_button(width/2, height/2 + 100, 400, 100, 'NEW GAME')
        fill(255)
        textSize(40)
        text("{} WINS".format(winner()), width/2, height/3)
    else:
        background(0)
        food.draw_food()
        snake1.draw_snake()
        snake2.draw_snake()
        draw_hud()
        
        if keyPressed:
            snake1.changedir = control(1)
            snake2.changedir = control(2)
        
        if frameCount % 10 == 0:
            
            
            if not snake1.food_collide(food.x, food.y):
                snake1.del_end()
            else:
                food.make_food()
                snake1.score += 1
            if not snake2.food_collide(food.x, food.y):
                snake2.del_end()
            else:
                food.make_food()
                snake2.score += 1
            snake1.grow()
            snake2.grow()
            
            #snake1.dir = snake1.changedir
            #snake2.dir = snake2.changedir
        
        if screen == 'timed':
            draw_timer()
            if snake1.snake_collide(snake2.x, snake2.y) or snake1.snake_collide(snake1.x, snake1.y):
                snake1 = reset_snake1()
            if snake2.snake_collide(snake1.x, snake1.y) or snake2.snake_collide(snake2.x, snake2.y):
                snake2 = reset_snake2()
        if screen == 'elimination':
            if snake1.snake_collide(snake2.x, snake2.y) and snake2.snake_collide(snake1.x, snake1.y):
                game_over = True
            elif snake1.snake_collide(snake2.x, snake2.y) or snake1.snake_collide(snake1.x, snake1.y):
                game_over = True
            elif snake2.snake_collide(snake1.x, snake1.y) or snake2.snake_collide(snake2.x, snake2.y):
                game_over = True

def mouseClicked():
    global screen, time, snake1, snake2, game_over
    if screen == 'title':
        if mouse_in(width/2, height/2, 400, 100):
            screen = 'timed'
            time = time_limit
        if mouse_in(width/2, height/2 + 120, 400, 100):
            screen = 'elimination'
    elif game_over:
        if mouse_in(width/2, height/2 + 100, 400, 100):
            screen = 'title'
            game_over = False
            snake1 = reset_snake1()
            snake2 = reset_snake2()
            snake1.score = 0
            snake2.score = 0
