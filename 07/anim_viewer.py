from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('Ice_Kirby_empty.png')

frame = 0

def Kirby_Walk (x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(114 + frame * 35, 616-39, 35, 33, x, y)

def Kirby_Dash(x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(112 + frame * 34, 616 - 80, 34, 33, x, y)

def Kirby_dumbring(x = 0,y = 0,frame = 0):
        frame = frame%11
        character.clip_draw(112 + frame * 37, 616 - 126, 37, 38, x, y)

def Kirby_frying(x = 0,y = 0,frame = 0):
        frame = frame%6
        character.clip_draw(112 + frame * 40, 616 - 353, 40, 41, x, y)

def Kirby_spin(x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(6 + frame * 40, 616 - 605, 40, 33, x, y)

def Kirby_Rotate(x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(11 + frame * 37, 616 - 559, 37, 36, x, y)

def Ice_Effect(x = 0,y = 0,frame = 0):
        frame = frame%4
        character.clip_draw(527 + frame * 72, 616 - 300, 72, 78, x, y)
def Ice_Charge(x = 0,y = 0,frame = 0):
        frame = frame%2
        character.clip_draw(658 + frame * 40, 616 - 208, 35, 30, x, y)
def Ice_Swim(x = 0,y = 0,frame = 0):
        frame = frame%8
        character.clip_draw(860 + frame * 34, 616 - 308, 33, 28, x, y)

# 여기를 채우세요.
while True:
        x = 50
        for x in range(50,800,5):
                clear_canvas()
                grass.draw(400, 30)

                Kirby_Walk(x, 70, frame)
                Kirby_Dash(x, 140, frame)
                Kirby_dumbring(x, 210, frame)
                Kirby_frying(x, 280, frame)
                Kirby_spin(x, 350, frame)
                Kirby_Rotate(x, 490, frame)
                Ice_Effect(x, 420, frame)
                Ice_Charge(x, 420, frame)
                Ice_Swim(x, 560, frame)

                frame = (frame + 1) % 20
                update_canvas()
                delay(0.03)
                get_events()




close_canvas()

