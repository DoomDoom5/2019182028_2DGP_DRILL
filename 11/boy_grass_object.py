from pico2d import *

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
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

boy = None # c = NULL
grass = None
running = True

# 초기화
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True


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



open_canvas()
enter()
# game main loop code
while running:
    handle_events()
    update()
    draw()
    delay(0.05)
exit()

close_canvas()
