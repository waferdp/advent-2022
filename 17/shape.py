class Shape:

    def __init__(self, shape, resting):
        self.sign = shape
        
        self.resting = resting

        height = self.getHeight() + 4
        self.initialHeight = height
        if shape == '-':
            self.shape = [(height,2),(height,3),(height,4),(height,5)]
        elif shape == '+':
            self.shape = [(height+2,3),
             (height+1,2),(height+1,3),(height+1,4),
                          (height, 3)]
        elif shape == 'L':
            self.shape =     [      (height+2, 4),
                                    (height+1, 4),
            (height, 2), (height, 3), (height, 4)]
        elif shape == 'I':
            self.shape = [  (height+3,2),
                            (height+2,2),
                            (height+1,2),
                            (height,2)]
        elif shape == '#':
            self.shape = [  (height+1,2), (height+1,3),
                            (height,2), (height,3)]
        else:
            raise Exception(f"{shape} not matching any shapes")

    def move(self, sign):
        if sign == '<':
            direction = (0, -1)
        elif sign == '>':
            direction = (0, 1)
        else: 
            direction = (-1, 0)

        if not self.canMove(direction):
            return False

        dy,dx = direction

        for i in range(0, len(self.shape)):
            y,x = self.shape[i]
            x += dx
            y += dy
            self.shape[i] = y,x
        return True
    
    def canMove(self, direction):
        dy,dx = direction
        for y,x in self.shape:
            if dx != 0:
                if x + dx < 0 or x + dx > 6:
                    return False
                if dx != 0 and self.resting.get(x+dx,y) != '.':
                    return False
            if dy != 0:
                if self.resting.get(x, y+dy) != '.':
                    return False
        return True

    def getHeight(self):
        return self.resting.maxY
