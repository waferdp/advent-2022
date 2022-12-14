from matrix import Matrix2d

class Cave(Matrix2d):


    def __init__(self, width, height, default, expando):
        super().__init__(width, height, default, expando)
        self.floor = height


    def strokes(self, strokes, value):
        for stroke in strokes:
            self.stroke(stroke[0], stroke[1], stroke[2], stroke[3], value)

    def stroke(self, ax, ay, bx, by, value):
        for y in range(ay, by+1):
            for x in range(ax,bx+1):
                self.set(x, y, value)

    def get(self,x, y):
        if y > self.floor:
            return '#' 
        return super().get(x, y)

    def dropOne(self, origin):
        (x, y) = origin
        maxy = self.height + 2 if self.expando else self.height
        while y < maxy:
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

    def __repr__(self):
        return self.draw()

    def draw(self):
        lines = []
        for y in range(self.miny, self.height):
            line = ''
            for x in range(self.minx, self.width):
                line += self.get(x,y)
            lines.append(line)
            line = ''
        return lines
