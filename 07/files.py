class File:

    def __init__(self, name, type, size = 0, parent = None):
        self. name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.children = {}

    def addChild(self, child):
        self.children[child.name] = child

    def getSubDirs(self):
        return list(filter(lambda child: child.type == 'dir'), self.children)

    def getSize(self, limit = None, belowLimit = None):
        if self.type == 'file':
            return self.size
        elif self.type == 'dir':
            children = list(self.children.values())
            if len(children) == 0:
                return 0
            childSizes = sum(map(lambda child: child.getSize(limit, belowLimit), children))
            if limit is None or childSizes < limit:
                if belowLimit is not None:
                    belowLimit.append((self.name, childSizes))
            # else:
            #     print(f'{self}: {childSizes}')
            return childSizes

    def __repr__(self) -> str:
        return f'{self.name} ({self.type})'

    def __str__(self) -> str:
        size = f', size={self.size}' if self.size > 0 else ''
        #children = list(map(lambda child: f'  {str(child)}', self.children ))
        return f'- {self.name} ({self.type}{size})'
