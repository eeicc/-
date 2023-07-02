import random

class 遊戲角色:
    生命值 = 400
    def __init__(self, 姓名):
        self.姓名 = 姓名
    def 防禦(self, 指令):
        if 指令 == 1:
            print(f'{self.姓名}擺出了格擋姿勢 !') #f-string {指定的變量名稱}
            return 0.5 #承受傷害減半
        elif 指令 == 2:
            print(f'{self.姓名}嘗試閃避攻擊 !')
            return random.choice([0,1.5]) #閃避成功不受傷害，閃避失敗多0.5倍的傷害
class 戰士(遊戲角色): #繼承遊戲角色
    def 攻擊(self, 指令):
        if  指令 == 1:
            print(f'{self.姓名}使出了撞擊 !')
            return 200 #200點傷害
        elif 指令 == 2:
            print(f'{self.姓名}使出了龍翔斬 !')
            return random.choice([300,100]) #300 or 100點傷害
class 魔物(遊戲角色):
    def 攻擊(self, 指令):
        if 指令 == 1:
            print(f'{self.姓名}使出了撕咬 !')
            return 180 #180點傷害
        elif 指令 == 2:
            print(f'{self.姓名}使出了會心一擊 !')
            return random.choice([320,100]) #320 or 100點傷害