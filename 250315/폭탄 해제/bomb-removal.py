unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

class Bomb:
    def __init__(self,unlock_code,wire_color,seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds


code = Bomb(unlock_code,wire_color,int(seconds))

print(f'code : {code.unlock_code}')
print(f'color : {code.wire_color}')
print(f'second : {code.seconds}')
