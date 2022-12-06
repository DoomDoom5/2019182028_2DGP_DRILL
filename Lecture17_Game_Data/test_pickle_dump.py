import pickle

class NPC:
    def __init__(self, name, x,y):
        self.name, self.x, self.y = name,x,y

    def show(self):
        print(f'Name:{self.name} @ ({self.x}, {self.y})')

yuri = NPC('Yuri', 100, 200)
print(yuri.__dict__) # 모든 객체는 __dict__ 라는 내부 변수가 자동으로 존재
# tom = NPC('Tom', 200, 100)
# yuri.show()
#
# npcs = [yuri, tom]
# with open('npc.pickle', 'wb') as f:
#     pickle.dump(npcs,f)


yuri.__dict__.update({'name' : 'tom' , 'x' : 100, 'y': 450})
print(yuri.__dict__)

