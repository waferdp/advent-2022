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
        return self.dfs(0, '', 0, 0, self.graph.get('AA'))

    def getMostValuablePaths(self, a, opened):
        paths = []
        for path in self.graph.paths[a]:
            leg = self.graph.paths[a][path]
            rate = self.graph.get(path).rate
            paths.append((path, rate/(len(leg)-1)) )
        ordered = sorted(paths, key=lambda x: x[1], reverse=True)
        return [node[0] for node in ordered]
        
    
    def dfs(self, minutes, opened, flowed, flow, current):
        if minutes >= 30:
            return flowed
        options = []
        if current.rate > 0:
            #opened.append(current.name)
            opened += current.name
            minutes += 1
            flowed += flow
            # flow increases in every following minute
            flow += current.rate
        ordered = self.getMostValuablePaths(current.name)
        for path in ordered:
            if path in opened:
                continue
            leg = self.graph.paths[current.name][path]
            time = len(leg)-1
            if minutes + time > self.time:
                continue
            else:
                option = self.dfs(minutes+time, opened, flowed + flow * time, flow, self.graph.get(path))
                options.append(option)
                break
        if len(options):
            return max(options)
        else:
            return (30-minutes)*flow + flowed

    def double(self):
        self.dfs(0, '', 0, 0, self.graph.get('AA'))

if __name__ == '__main__':
    input = fileReader.read('input.txt')
    pressure = Pressure(input)
    pressure.graph.setFlowValves()
    flowed = pressure.maxPressure()
    print(flowed)
