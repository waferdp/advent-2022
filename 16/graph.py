import re
from node import Node
from itertools import permutations

class Graph:
    def __init__(self):
        self.nodes = dict()
        self.paths = dict()
        self.flowValves = []

    def parseNode(text):
        valve, tunnels = text.split(';')
        name = re.findall('[A-Z]{2}', valve)[0]
        flow = int(re.findall('-?[0-9]+', valve)[0])
        leadsTo = re.findall('[A-Z]{2}', tunnels)
        return Node(name, flow, leadsTo)

    def addNode(self,node):
        self.nodes[node.name] = node

    def parseAndAddNode(self, nodeText):
        self.addNode(Graph.parseNode(nodeText))
    
    def get(self, name):
        return self.nodes[name]

    def findFlowValves(self):
        return list(map(lambda node: node.name, filter(lambda n: n.rate > 0, self.nodes.values())))        

    def findRoutes(self):
        flowValves = list(map(lambda node: node.name, filter(lambda n: n.rate > 0, self.nodes.values())))
        pairs = list(permutations(flowValves, 2))
        shortest = dict()
        for pair in pairs:
            if pair[0] not in shortest:
                shortest[pair[0]] = dict()
            shortest[pair[0]][pair[1]] = self.getShortestPath(pair[0], pair[1])
        shortest['AA'] = dict()
        for flowValve in flowValves:
            shortest['AA'][flowValve] = self.getShortestPath('AA', flowValve)
        return shortest
    
    def setFlowValves(self):
        self.flowValves = self.findFlowValves()
        self.paths = self.findRoutes()

    def getShortestPath(self, a, b):
        paths = [[a]]
        visited = set()
        while True:
            newPaths = []
            for path in paths:
                visited.add(path[-1])
            for path in paths:
                options = list(filter(lambda n: n not in visited, self.get(path[-1]).leads))
                for option in options:
                    newPath = path + [option]
                    if option == b:
                        return newPath
                    newPaths.append(newPath)
            paths = newPaths
                
