import fileReader
from graph import Graph

class Pressure:
    
    def __init__(self, input):
        self.graph = self.parseInput(input)
        self.time = 30
        self.help = False

    def parseInput(self, input):
        graph = Graph()
        for line in input:
            graph.parseAndAddNode(line)
        return graph

    def maxPressure(self):
        return self.dfs(opened={}, current='AA')
        
    def dfs(self, opened, current):
        minutes = max(opened.values()) if len(opened) else 0
        if minutes >= self.time:
            return self.getFlow(opened)
        options = []
        #ordered = self.getMostValuablePaths(current, opened)
        for path in self.graph.paths[current]:
            if path in opened:
                continue
            leg = self.graph.paths[current][path]
            time = len(leg)
            if minutes + time > self.time:
                continue
            else:
                openCopy = opened.copy()
                openTime = minutes+time
                openCopy[path] = openTime 
                option = self.dfs(openCopy, path)
                options.append(option)
        if len(options):
            return max(options)
        else:
            return self.getFlow(opened)

    def getFlow(self, opened):
        flowed = 0
        for valve in opened:
            rate = self.graph.get(valve).rate
            openedAt = opened[valve]
            flowed += rate * (self.time - openedAt)
        return flowed

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    pressure = Pressure(input)
    pressure.graph.setFlowValves()
    flowed = pressure.maxPressure()
    print(flowed)
