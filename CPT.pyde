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
    textSize(h/2)
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
        self.changedir = dir
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
        for i in range(len(other_x)):
            if self.x[-1] == other_x[i] and self.y[-1] == other_y[i]:
                return True
        return False

    def self_collide(self):
        for i in range(len(self.x) - 1):
            if self.x[-1] == self.x[i] and self.y[-1] == self.y[i]:
                return True
        return False

    def control(self, snake):
        if snake == 1:
            up = 87
            down = 83
            left = 65
            right = 68
        elif snake == 2:
            up = 38
            down = 40
            left = 37
            right = 39
        if keyCode == up:
            if self.dir == 'down':
                return self.dir
            else:
                return 'up'
        if keyCode == down:
            if self.dir == 'up':
                return self.dir
            else:
                return 'down'
        if keyCode == left:
            if self.dir == 'right':
                return self.dir
            else:
                return 'left'
        if keyCode == right:
            if self.dir == 'left':
                return self.dir
            else:
                return 'right'
        return self.changedir


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
    text(snake1.score, 0, hud_height/2)
    textAlign(RIGHT, CENTER)
    text(snake2.score, width, hud_height/2)


def draw_timer():
    global time, game_over
    if frameCount % 60 == 0:
        time -= 1

    fill(0)
    textSize(hud_height)
    textAlign(CENTER, CENTER)

    text("{}:{}{}".format(time//60, time % 60//10, time % 10), width/2, hud_height/2)
    if time <= 0:
        game_over = True


def winner():
    if screen == 'timed':
        if snake1.score < snake2.score:
            return 'BLUE'
        elif snake1.score > snake2.score:
            return 'RED'
        else:
            return 'NO ONE'
    if screen == 'elimination':
        if snake1.snake_collide(snake2.x, snake2.y) and snake2.snake_collide(snake1.x, snake1.y):
            return 'NO ONE'
        elif snake1.snake_collide(snake2.x, snake2.y) or snake1.self_collide():
            return 'BLUE'
        elif snake2.snake_collide(snake1.x, snake1.y) or snake2.self_collide():
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
        draw_button(width/2, height/2, 400, pixelsize*8, 'TIMED')
        draw_button(width/2, height/2 + height/6, 400, pixelsize*8, 'ELIMINATION')
        draw_button(width/2, height/2 + height/3, 400, pixelsize*8, 'HOW TO PLAY')
    elif screen == 'htp':
        background(0)
        draw_button(width/2, height - pixelsize*3, 400, pixelsize*6, 'BACK')

        textSize(pixelsize*3)
        fill(255)
        textAlign(LEFT, TOP)
    
        text('HOW TO PLAY:', 0, 0)
        text('TIMED MODE: ', 0, gridy/6*pixelsize)
        text('ELIMINATION MODE: ', 0, gridy/6*pixelsize*2)
        text('CONTROLS: ', 0, gridy/6*pixelsize*3)
    
        rectMode(CORNERS)
        textSize(pixelsize*2)
        textLeading(20)
        text('Eat dots to grow. Avoid colliding with the other snake. Don\'t collide with yourself.', 0, pixelsize*3, width, height)
        text('When the timer runs out, the longest snake wins. Collision will reset your score.', 0, gridy/6*pixelsize+pixelsize*3, width, height)
        text('One life.  Get the other snake to collide with you. Avoid colliding with the other snake.', 0, gridy/6*pixelsize*2+pixelsize*3, width, height)
    
        textSize(50)
        fill('#ff0000')
        text('''RED:
    W
  A S D''', 0, gridy/6*pixelsize*3+pixelsize*3)
        fill('#0000ff')
        text('''BLUE:
     ^
  < v >''', width/2, gridy/6*pixelsize*3+pixelsize*3)

    elif game_over:
        draw_button(width/2, height/2 + 100, 400, pixelsize*10, 'NEW GAME')
        fill(255)
        textSize(40)
        text("{} WINS".format(winner()), width/2, height/3)
    else:
        background(0)
        food.draw_food()
        snake1.draw_snake()
        snake2.draw_snake()
        draw_hud()

        if frameCount % 10 == 0:
            snake1.dir = snake1.changedir
            snake2.dir = snake2.changedir

            snake1.grow()
            snake2.grow()

            if snake1.food_collide(food.x, food.y):
                food.make_food()
                snake1.score += 1
            else:
                snake1.del_end()

            if snake2.food_collide(food.x, food.y):
                food.make_food()
                snake2.score += 1
            else:
                snake2.del_end()

        if screen == 'timed':
            draw_timer()
            if snake1.snake_collide(snake2.x, snake2.y) or snake1.self_collide():
                snake1 = reset_snake1()
            if snake2.snake_collide(snake1.x, snake1.y) or snake2.self_collide():
                snake2 = reset_snake2()

        if screen == 'elimination':
            if snake1.snake_collide(snake2.x, snake2.y) and snake2.snake_collide(snake1.x, snake1.y):
                game_over = True
            elif snake1.snake_collide(snake2.x, snake2.y) or snake1.self_collide():
                game_over = True
            elif snake2.snake_collide(snake1.x, snake1.y) or snake2.self_collide():
                game_over = True


def mouseClicked():
    global screen, time, snake1, snake2, game_over
    if screen == 'title':
        if mouse_in(width/2, height/2, 400, pixelsize*8):
            screen = 'timed'
            time = time_limit
        if mouse_in(width/2, height/2 + height/6, 400, pixelsize*8):
            screen = 'elimination'
        if mouse_in(width/2, height/2 + height/3, 400, pixelsize*8):
            screen = 'htp'
    elif screen == 'htp':
        if mouse_in(width/2, height - pixelsize*3, 400, pixelsize*6):
            screen = 'title'
    elif game_over:
        if mouse_in(width/2, height/2 + 100, 400, 100):
            screen = 'title'
            game_over = False
            snake1 = reset_snake1()
            snake2 = reset_snake2()
            snake1.score = 0
            snake2.score = 0


def keyPressed():
    global snake1, snake2
    snake1.changedir = snake1.control(1)
    snake2.changedir = snake2.control(2)
