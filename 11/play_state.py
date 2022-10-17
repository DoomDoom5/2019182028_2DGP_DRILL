from pico2d import *
import game_framework
import title_state
import item_state
import boy_add_delete_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.item = None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800 :
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1 :
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1 :
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

        if self.item == 'Ball' :
            self.ball_image.draw(self.x+ 10, self.y+50)
        elif self.item == "BigBall":
            self.big_ball_image.draw(self.x+ 10, self.y+50)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_i):
                game_framework.push_state(item_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_b):
                game_framework.push_state(boy_add_delete_state)

boy = None
boys =[None] # c = NULL
grass = None

# 초기화
def enter():
    global boys, grass, boy
    boys = [Boy()]
    grass = Grass()


# 종료
def exit(): # 파이선 내장 코드라 딴 곳에 서는 다르게 이름 지어야 됨
    global boys, grass
    del boys
    del grass

# 월드에 존재하는 객체들을 업데이트
def update():
    for boy in boys:
        boy.update()
    # grass는 update X

# world를 그린다
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for boy in boys:
        boy.draw()
def pause():
    pass
def resume():
    pass
