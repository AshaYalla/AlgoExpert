class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for i in self.children:
            i.depthFirstSearch(array)
        return array
            


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        stack = [self]
        while stack:
            n = stack.pop()
            array.append(n.name)
            for i in reversed(n.children):
                stack.append(i)
        return array