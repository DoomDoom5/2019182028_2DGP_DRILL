from pico2d import *

# 이벤트 정의 0, 1, 2, 3
RD, LD, RU, LU, TIMER, A = range(6)

# 키 입력확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYDOWN, SDLK_a) : A,
}


class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.timer = 1000

    def exit(self): # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT IDLE')
        self.dir = 0
        pass
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER) # 조금 더 객체 지향적인 방법,,,
    pass


    def draw(self): # 상태 그리기
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass
    pass
    
class RUN:
    def enter(self, event):
        print('ENTER RUN')
        # 방향을 결정해야 하는데, 뭘 근거로? 어떤키가 눌렸기 때문에?
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir +=1
        pass

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir
        pass


    def do(self):
        self.frame = (self.frame + 1) % 8
        # x 좌표 변경, 달리기
        self.x += self.dir
        self.x = clamp(0,self.x,800)
        pass


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

    pass

class SLEEP:
    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self):
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        print('DRAW SLEEP')
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592 / 2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592 / 2, '', self.x - 25, self.y - 25, 100, 100)

class AUTO_RUN:
    def enter(self, event):
        print('ENTER AUTO RUN')
        self.dir = self.face_dir
        pass

    @staticmethod
    def exit(self):
        print('ENTER AUTO RUN')
        self.dir = 0
        pass

    def do(self):
        print('DO AUTO RUN')
        self.frame = (self.frame + 1) % 8
        # x 좌표 변경, 달리기
        if(self.x <= 0):
            self.dir = 1
            self.face_dir = 1
        elif(self.x >= 800):
            self.dir = -1
            self.face_dir = -1
        self.x += self.dir

        self.x = clamp(0, self.x, 800)
        pass

    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 0, 100, 100, 0, '', self.x + 10, self.y + 10, 120, 120)
        else:
            self.image.clip_composite_draw(self.frame * 100, 100, 100, 100, 0, '', self.x + 10 , self.y + 10, 120, 120)
        pass
    pass



#3 상태 변환 기술
next_state = {
    SLEEP: {RD : RUN , LD:RUN, RU:RUN, LD:RUN, TIMER:SLEEP, A : SLEEP},
    IDLE : {RU: RUN, LU : RUN, RD : RUN, LD :RUN, TIMER:SLEEP, A : AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, A : AUTO_RUN},
    AUTO_RUN : {RD: RUN , LD: RUN, RU: RUN, LD: RUN, A : IDLE},
}


class Boy:
    def enter(self, event):
        print('ENTER RUN')
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
    def exit(self):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)
        # if(self.x < 0):
        #     self.dir += 1;
        # elif (self.x > 1000):
        #     self.dir -= 1;


    def draw(self):
        print('DRAW RUN')
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.timer = 100
        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

