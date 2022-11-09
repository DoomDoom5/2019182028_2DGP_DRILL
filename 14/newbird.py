import random

from pico2d import *

import game_framework
import game_world

# Boy Run Speed
PIXEL_PER_METER = (10.0/0.5)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(0,800), random.randint(150,250)
        self.xframe = 0
        self.yframe = 0
        self.dir = 1
        self.image = load_image('bird_animation.png')
        self.font = load_font("ENCR10B.TTF", 16)

    def update(self):
        self.xframe = (self.xframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time)
        if self.xframe > 4:
            self.xframe = 0
            self.yframe +=1

        elif self.xframe > 2 and self.yframe > 2:
            self.yframe = 0



        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)
        if(self.x >=1600 - 40):
            self.dir = -1
        elif self.x <= 40:
            self.dir = 1
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_composite_draw(int(self.xframe) * 168,int(self.yframe) * 183, 168, 183, 0, 'h', self.x, self.y, 50, 50)
        elif self.dir == 1:
            self.image.clip_composite_draw(int(self.xframe) * 168,int(self.yframe) * 183, 168, 183, 0, ' ', self.x, self.y, 50, 50)

        self.font.draw(self.x - 60, self.y + 50 , f'{get_time():.2f}',(255,255,0))

    def add_event(self, event):
        self.event_que.insert(0, event)
