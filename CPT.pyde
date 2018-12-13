screen = 'title'

hover_clr='#ff0000'
button_normal=255

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

def draw_title():
    fill("#ff0000")
    textSize(100)
    textAlign(CENTER)
    text("SNAKES", width/2, height/3)

def setup():
    size(500, 550)

def draw():
    global screen
    if screen == 'title':
        background(0)
        draw_title()
        draw_button_timed(width/2 - 50, height/2, 100, 40)
        draw_button_elimination(width/2 - 70, height/2 + 120, 140, 40)
    else:
        if screen == 'timed':
            background(0)
            
        if screen == 'slimination':
            background(0)
    
def mouseClicked():
    global screen
    if screen == 'title':
        if mouse_in_button(width/2 - 50, height/2, 100, 40):
            screen = 'timed'
        if mouse_in_button(width/2 - 70, height/2 + 120, 140, 40):
            screen = 'elimination'
