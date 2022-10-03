from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


running = True
x = 0
frame = 0


def handle_events():
    global running
    # 전역에서 선언한 변수를 함수에서 가져옴

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT: # SDL_QUIT == 윈도우창 상단 X버튼
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False;
    pass


while x < 800 and running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += 5
    delay(0.01)

close_canvas()

