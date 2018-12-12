# Button colour
hover_clr=color(228,63,111)
button_normal=color(223,187,177)

# Button timed
def draw_button_timed(button_timed_x, button_timed_y, button_timed_w, button_timed_h):
    if mouseX > button_timed_x and mouseX < button_timed_x + button_timed_w and mouseY > button_timed_y and mouseY < button_timed_y + button_timed_h:
        noStroke()
        fill(hover_clr)
        rect(button_timed_x, button_timed_y, button_timed_w, button_timed_h, 100)
    else: 
        noStroke()
        fill(button_normal)
        rect(button_timed_x, button_timed_y, button_timed_w, button_timed_h, 100)

# Button elimination
def draw_button_elimination(button_elimination_x, button_elimination_y, button_elimination_w, button_elimination_h):
    if mouseX > button_elimination_x and mouseX < button_elimination_x + button_elimination_w and mouseY > button_elimination_y and mouseY < button_elimination_y + button_elimination_h:
        noStroke()
        fill(hover_clr)
        rect(button_elimination_x, button_elimination_y, button_elimination_w, button_elimination_h, 100)
    else:
        noStroke()
        fill(button_normal)
        rect(button_elimination_x, button_elimination_y, button_elimination_w, button_elimination_h, 100)

# Tittle
def draw_title():
    fill("#ff0000")
    textSize(100)
    textAlign(CENTER)
    text("SNAKES", width/2, height/3)

# Mode    
def draw_timed_mode():
    fill(0)
    textSize(15)
    text("timed mode", width/2, height/2 + 20)
def draw_elimination_mode():
    fill(0)
    textSize(15)
    text("elimination mode", width/2, height/2 + 140)
    
def setup():
# Screen size
    size(500, 550)

def draw():
# Start
    background(0)
    draw_title()
    draw_button_timed(width/2 - 50, height/2, 100, 40, )
    draw_button_elimination(width/2 - 70, height/2 + 120, 140, 40)
    draw_timed_mode()
    draw_elimination_mode()
    
    if mousePressed:
        background(255)
    
    
