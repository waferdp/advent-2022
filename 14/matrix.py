
class Matrix2d:
    matrix = None
    width = 0
    height = 0
    minx = 0
    miny = 0
    expando = False
    default = None

    def __init__(self, width, height, default = None, expando = False):
        self.matrix = {}
        self.minx = 0
        self.miny = 0
        self.width = width
        self.height = height
        self.default = default
        self.expando = expando

    def get(self, x, y):
        if x < self.minx or y < self.miny:
            return self.default
        if x >= self.width or y >= self.height:
            return self.default
        try:
            return self.matrix[y][x]
        except:
            return self.default
        
    def set(self, x, y, value):
        if not self.expando:
            if y >= self.height or x >= self.width:
                return
        if y not in self.matrix:
            self.matrix[y] = {}
        self.matrix[y][x] = value
        self.minx = min(self.minx, x)
        self.width = max(self.width, x+1)
        self.miny = min(self.miny, y)
        self.height = max(self.height, y+1)