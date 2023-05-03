class Goomba:
    def __init__(self, pos, speed=1):
        self.speed = speed
        self.alive = True
        self.pos = pos

class Block: #parent class
    def __init__(self, pos, size=10):
        self.size = size
        self.x = x
        self.y = y

class Tube:
    def __init__(self, pos, angle=0, entrace="top"):
        self.pos = pos
        self.angle = angle
        self.entrance = entrace 

