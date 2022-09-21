from pico2d import *
import math

open_canvas()

# fill here
os.chdir('D:/2019182028_2DGP_DRILL/06')


grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 이동 코드

x = 0
y = 90

while(x < 800 - 10):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x = x + 2
    delay(0.01)
    
while(y < 600 - 30):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y = y + 2
    delay(0.01)

while(x > 10):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x = x - 2
    delay(0.01)
    
while(y > 90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y = y - 2
    delay(0.01)

    
# 원 이동 코드
x = 400
y = 345
rx = 400
ry = 255
dgree = 0

for dgree in range(0,360):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x + rx * math.cos(dgree/360 * 2 * math.pi),
                        y + ry * math.sin(dgree/360 * 2 * math.pi))
    delay(0.01)
    

close_canvas()
