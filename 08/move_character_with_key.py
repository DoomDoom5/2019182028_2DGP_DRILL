from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    # fill here
    global running
    global x_dir
    global y_dir
    global inverse
    global idle

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN :
            idle = False
            if event.key == SDLK_RIGHT:
                x_dir +=1
                inverse = False
            elif event.key == SDLK_LEFT:
                x_dir -=1
                inverse = True
            elif event.key == SDLK_UP:
                y_dir += 1
            elif event.key == SDLK_DOWN:
                y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                idle = True
                x_dir -= 1
            elif event.key == SDLK_LEFT:
                idle = True
                x_dir += 1
            elif event.key == SDLK_UP:
                idle = True
                y_dir -= 1
            elif event.key == SDLK_DOWN:
                idle = True
                y_dir += 1
    pass


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
grass = load_image('grass.png')
character = load_image('animation_sheet.png')
inverse = False
idle = True
running = True
x = KPU_WIDTH // 2
y = KPU_HEIGHT // 2

frame = 0

x_dir = 0
y_dir = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if idle:
        if inverse:
            character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    else :
        if inverse:
            character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    if x < KPU_WIDTH - 50 and x > 50 :
        x += x_dir * 5
    elif x >= KPU_WIDTH - 50:
        x = KPU_WIDTH - 55
    elif x <= 50 :
         x = 55

    if (y < KPU_HEIGHT - 50 and y > 50):
        y += y_dir * 5
    elif y >= KPU_HEIGHT - 50:
        y = KPU_HEIGHT - 55
    elif y <= 50:
        y = 55

    delay(0.01)

close_canvas()

