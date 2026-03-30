graph_structure = {
    'a':['b','c'],
    'b':['a','d'],
    'c':['a','d'],
    'd':['b','e'],
    'e':['d']
}
print(graph_structure)

# Displaying the Vertices:

# Creating a class of graph
class graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())


    
gobj = graph(graph_structure)
print("The given Vertices are",gobj.getVertices())