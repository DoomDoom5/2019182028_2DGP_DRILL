from pico2d import *
import game_framework
import play_state
import logo_state

image = None

def enter():
    global image
    image = load_image("title.png")
    # fill here
    pass

def exit():
    # fill here
    global image
    del image
    pass

def handle_events():
    # fill here
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(logo_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(play_state)
    delay(0.01)
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass






