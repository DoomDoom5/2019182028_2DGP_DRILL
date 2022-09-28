from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0
frame = 0

# 여기를 채우세요.
for x in range(0, 800, 5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    # clip_draw(이미지(left, bottom, width, height), 캔버스(x ,y))
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.01)
    get_events()

close_canvas()

