from pico2d import *

# 이벤트 정의 0, 1, 2, 3
RD, LD, RU, LU = range(4)

# 키 입력확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
}


class IDLE:
    @staticmethod
    def enter(): # 상태에 들어갈 때 행하는 액션
        print('ENTER IDLE')
        pass

    @staticmethod
    def exit(): # 상태를 나올 때 행하는 액션, 고개 들기
        print('EXIT IDLE')
        pass

    @staticmethod
    def do(): # 상태에 있을 떄 지속적으로 행하는 행위, 숨쉬기
        pass

    @staticmethod
    def draw(): # 상태 그리기
        pass
    pass
    
class RUN:
    @staticmethod
    def enter():
        print('ENTER RUN')
        pass

    @staticmethod
    def exit():
        print('EXIT RUN')
        pass

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass

    pass


#3 상태 변환 기술
next_state = {
    IDLE : {RU: RUN, LU : RUN, RD : RUN, LD :RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE},

}


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = [] # 이벤트 큐 초기화
        self.cur_state = IDLE
        self.cur_state.enter() # 초기 상태의 entry 액션 수행

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.q.insert(0,key_event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def update(self):
        self.cur_state.do() # 현재 상태의 do 액션 실행

        # 이벤트를 확인해서, 이벤트가 있으면 이벤트 변환 처리
        if self.q : # q에 이벤트가 있으면, 이벤트가 발생헀으면
            event = self.q.pop()
            self.cur_state.exit() # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event] # 다음 상태를 구한다.
            self.cur_state.enter()


        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw()
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
