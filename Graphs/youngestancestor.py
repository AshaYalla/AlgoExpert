# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def depthFunc(top, des):
    depth = 0
    while des!= top:
        depth+=1
        des = des.ancestor
    return depth
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    depthone = depthFunc(topAncestor, descendantOne)
    depthtwo = depthFunc(topAncestor, descendantTwo)

    if depthone > depthtwo:
        while(depthone!=depthtwo):
            descendantOne = descendantOne.ancestor
            depthone-=1
    else:
        while(depthone!=depthtwo):
            descendantTwo = descendantTwo.ancestor
            depthtwo-=1
    while True:
        if descendantOne == descendantTwo:
            return descendantOne
        else:
            descendantOne = descendantOne.ancestor
            descendantTwo = descendantTwo.ancestor
            
            
            
        
        
    
    
    
