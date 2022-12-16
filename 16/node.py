class Node:
    def __init__(self, name:str, rate:int, leads):
        self.name = name
        self.rate = rate
        self.leads = leads

    def __text(self):
        return f'{self.name}: {self.flow} -> {",".join(self.leads)}'    

    def __repr__(self):
        return self.__text()

    def __str__(self):
        return self.__text()