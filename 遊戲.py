import random
from 參數 import 遊戲角色, 戰士, 魔物 #導入參數

玩家姓名 = input('請輸入角色名稱 :')
玩家 = 戰士(玩家姓名)
敵方 = 魔物('凱薩')
while True:
  隨機防禦 = random.choice([1,2])
  while True:
    try:
      攻擊指令 = int(input('請輸入您的攻擊指令(1)普通攻擊(2)特殊攻擊:'))
      if 攻擊指令<=0 or 攻擊指令>=3:
        print('請輸入1或2 !')
      else:
        break
    except ValueError:
      print('請輸入1或2 !')
  玩家攻擊力 = 玩家.攻擊(攻擊指令)
  損血=int(敵方.防禦(隨機防禦)*玩家攻擊力)
  敵方.生命值 -= 損血
  if 敵方.生命值<=0:
      print(f'{敵方.姓名}倒下了，{玩家.姓名}獲勝!')
      break
  else:
      print(f'{敵方.姓名}受到{損血}傷害! 生命值剩下{敵方.生命值}')
      print('')
  
  隨機攻擊 = random.choice([1,2])
  while True:
    try:
      防禦指令 = int(input('請輸入您的防禦指令(1)格擋(2)閃避:'))
      if 防禦指令<=0 or 防禦指令>=3:
        print('請輸入1或2 !')
      else:
        break
    except ValueError:
      print('請輸入1或2 !')
  敵方攻擊力 = 敵方.攻擊(隨機攻擊)
  損血=int(玩家.防禦(防禦指令)*敵方攻擊力)
  玩家.生命值 -= 損血
  if 玩家.生命值<=0:
      print(f'{玩家.姓名}倒下了，遊戲結束')
      break
  else:
      print(f'{玩家.姓名}受到{損血}傷害! 生命值剩下{玩家.生命值}')
      print('')
