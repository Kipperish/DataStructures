class Node():
    def __init__(self, identifier):
        self.identifier = identifier
        self.edges = []

class Edge():
    def __init__(self, nextNode, weight):
        self.nextNode = nextNode
        self.weight = weight

class Network():
    def __init__(self):
        self.nodes = []

    def addNode(self, identifier):
        available = True
        for node in self.nodes:
            if node.identifier == identifier:
                available = False
        if available:
            self.nodes.append(Node(identifier))
        else:
            print(f"Node with given identifier ({identifier}) already found in the Network")

    def addEdge(self, firstNode, secondNode, weight):
        firstNodeFound = False
        secondNodeFound = False
        for node in self.nodes:
            if node.identifier == firstNode:
                firstNodeFound = True
                node1 = node
            elif node.identifier == secondNode:
                secondNodeFound = True
                node2 = node
        if firstNodeFound and secondNodeFound:
            node1.edges.append(Edge(node2, weight))
            node2.edges.append(Edge(node1, weight))
        else:
            print("Could not find one or more of the given nodes within the network")

network = Network()

network.addNode("A")
network.addNode("B")
network.addNode("C")
network.addNode("D")
network.addNode("E")

network.addEdge("A","B", 15)
network.addEdge("A","D", 12)
network.addEdge("A","E", 7)
network.addEdge("B","D", 13)
network.addEdge("C","D", 5)
network.addEdge("C","E", 17)

def allEdges(network):
    for node in network.nodes:
        for edge in node.edges:
            print(node.identifier, "-->", edge.nextNode.identifier, edge.weight)

allEdges(network)