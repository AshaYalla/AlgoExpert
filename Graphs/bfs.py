class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            node = queue.pop(0)
            array.append(node.name)
            for i in node.children:
                queue.append(i)
        return array