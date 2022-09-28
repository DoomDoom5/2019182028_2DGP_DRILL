from pico2d import *
# *표는 pico2d의 모든 함수를 import 하겠다는 뜻

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 여기를 채우세요.
x = 0
for x in range(0, 800+1 ,2 ):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, 90)
    update_canvas()
    delay(0.01)
    get_events() # 메시 펌프에서 OS에 프로세스.. 머였떠라

close_canvas()

