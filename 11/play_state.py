from pico2d import *
import game_framework
import logo_state
import title_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(logo_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)

boy = None # c = NULL
grass = None

# 초기화
def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()


# 종료
def exit(): # 파이선 내장 코드라 딴 곳에 서는 다르게 이름 지어야 됨
    global boy, grass
    del boy
    del grass

# 월드에 존재하는 객체들을 업데이트
def update():
    boy.update()
    # grass는 update X

# world를 그린다
def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
