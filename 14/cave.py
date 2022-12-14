from matrix import Matrix2d

class Cave(Matrix2d):


    def __init__(self, width, height, default, expando):
        super().__init__(width, height, default)
        self.floor = height + (1 if expando else 0)
        self.expando = expando

    def strokes(self, strokes, value):
        for stroke in strokes:
            self.stroke(stroke[0], stroke[1], stroke[2], stroke[3], value)

    def stroke(self, ax, ay, bx, by, value):
        for y in range(ay, by+1):
            for x in range(ax,bx+1):
                self.set(x, y, value)

    def get(self,x, y):
        if y >= self.floor and self.expando:
            return '#' 
        return super().get(x, y)

    def dropOne(self, origin):
        (x, y) = origin
        while y <= self.floor:
            below = self.get(x, y+1)
            downLeft = self.get(x-1,y+1)
            downRight = self.get(x+1,y+1)
            if below == '.':
                y += 1
            elif downLeft == '.':
                x -= 1
                y += 1
            elif downRight == '.':
                x += 1
                y += 1
            else:
                self.set(x, y, 'o')
                return y == 0
        return True
