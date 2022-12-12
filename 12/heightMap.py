from matrix import Matrix2d

class HeightMap(Matrix2d):
    
    def getPaths(self, x, y):
        possible = []
        height = self.get(x, y)
        above = self.get(x, y-1)
        below = self.get(x, y+1)
        left = self.get(x-1,y)
        right = self.get(x+1,y)

        if above - height <= 1:
            possible.append((x, y-1))
        
        if below - height <= 1:
            possible.append((x, y+1))

        if left - height <= 1:
            possible.append((x-1, y))
            
        if right - height <= 1:
            possible.append((x+1, y))

        return possible