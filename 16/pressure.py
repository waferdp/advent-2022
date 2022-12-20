import fileReader
from graph import Graph
from itertools import combinations

class Pressure:
    
    def __init__(self, input):
        self.graph = self.parseInput(input)
        self.time = 26
        self.help = False

    def parseInput(self, input):
        graph = Graph()
        for line in input:
            graph.parseAndAddNode(line)
        return graph

    def maxPressure(self):
        valves = list(self.graph.paths.keys())
        valves.remove('AA')
        return self.dfs(valves, opened={}, current='AA')

    def double(self):
        valves = list(self.graph.paths.keys())
        valves.remove('AA')
        halves = list(combinations(valves, len(valves)//2))
        best = 0
        print(len(halves))
        for half in halves:
            others = list(filter(lambda v: v not in half, valves))
            one = self.dfs(half, opened={}, current='AA')
            other = self.dfs(others, opened={}, current='AA')
            best = max(best, one+other)
            
        return best

    def dfs(self, valves, opened, current):
        minutes = max(opened.values()) if len(opened) else 0
        if minutes >= self.time:
            return self.getFlow(opened)
        options = []
        #ordered = self.getMostValuablePaths(current, opened)
        for path in self.graph.paths[current]:
            if path in opened:
                continue
            if path not in valves:
                continue
            leg = self.graph.paths[current][path]
            time = len(leg)
            if minutes + time > self.time:
                continue
            else:
                openCopy = opened.copy()
                openTime = minutes+time
                openCopy[path] = openTime 
                option = self.dfs(valves, openCopy, path)
                options.append(option)
        if len(options):
            return max(options)
        else:
            return self.getFlow(opened)

    def getAvailablePaths(self, current, remaining, opened):
        paths = [(dest, len(self.graph.paths[current][dest])) for dest in self.graph.paths[current]]
        return list(filter(lambda path: path[0] not in opened and path[1] <= remaining, paths))

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
    flowed1 = pressure.maxPressure()
    print(flowed1)
    flowed2 = pressure.double()
    print(flowed2)
