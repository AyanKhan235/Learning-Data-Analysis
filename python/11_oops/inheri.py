class rect:
    def __init__(self, length, breath):
        
        self.length=length
        self.breath=breath
    def Area(self):
        return self.length*self.breath
class sq(rect):
    def __init__(self, side):
        # self.length=side
        # self.breath=side
        # rect.__init__(self, side, side)

        super()__init__(self, side, side)


    
r=rect(4,6)
s=sq(4)
print(s.Area())
print(r.Area())