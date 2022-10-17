import pico2d
from pico2d import *
import game_framework
import play_state
import item_state
image = None


def enter():
    global image
    image = load_image("add_delete_boy.png")
    pass

def exit():
    global image
    del image
    pass

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state() # 이전 상태인 play_state로 복귀
                    return
                case pico2d.SDLK_j: # 소년 증가
                    newBoy = play_state.Boy()
                    newBoy.__init__()
                    play_state.boys.append(newBoy)
                    del newBoy
                    pass
                case pico2d.SDLK_i:
                    game_framework.change_state(item_state)

                case pico2d.SDLK_k: # 소년 감소
                    if len(play_state.boys) > 1:
                        play_state.boys.pop()
                    pass



