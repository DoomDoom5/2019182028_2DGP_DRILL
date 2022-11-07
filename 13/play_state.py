from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy


boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)

# 초기화
def enter():
    global boy
    boy = Boy()
    grass = Grass()
    game_world.addObject(boy, 1)
    game_world.addObject(grass,0)
    grass = Grass()
    grass.y = 10
    game_world.addObject(grass,2)
    # 영속 개채(영원히 살아있는 게임 객체) ex) 플레이어 , 맵
# 종료
def exit():
    game_world.claer()
    pass

def update():
    for game_object in game_world.all_objects():
        game_object.update() # game_world에서 제너레이터 하였기 때문에

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw() # game_world에서 제너레이터 하였기 때문에
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass

def test_self():
    import play_state
    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
