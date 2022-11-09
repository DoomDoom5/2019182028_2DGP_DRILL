import random

from pico2d import *

import game_framework
import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class bird:
    def __init__(self):
        self.x, self.y = random.randint(0,800), 200
        self.xframe = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png.png')
        self.font = load_font("ENCR10B.TTF", 16)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) %14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)
        pass

    def draw(self):
        if self.dir == -1:
            self.clip_composite_draw(self.frame//3 * 918/5 , self.frame//5 * 506/3,183, 169, 0, 0, self.x,self.y,20,20)
        elif self.dir == 1:
            self.clip_composite_draw(self.frame // 3 * 918 / 5, self.frame // 5 * 506 / 3, 183, 169, 0, 'v', self.x,self.y,20,20)

        self.font.draw(self.x - 60, self.y + 50 , f'{get_time():.2f}',(255,255,0))

    def add_event(self, event):
        self.event_que.insert(0, event)
