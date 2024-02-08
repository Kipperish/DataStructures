import math

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
    
    def allEdges(self):
        for node in self.nodes:
            for edge in node.edges:
                print(node.identifier, "-->", edge.nextNode.identifier, edge.weight)

    def shortestDistance(self, firstNode, secondNode):
        firstNodeFound = False
        secondNodeFound = False
        visitedNodes = []
        unvisitedNodes = []
        workingValues = []
        nodeIndex = 0
        nodeDistanceIndex = 1
        previousNodeIndex = 2
        for node in self.nodes:
            unvisitedNodes.append(node.identifier)
        for node in self.nodes:
            workingValues.append([node.identifier, math.inf, None])
        for node in self.nodes:
            if node.identifier == firstNode:
                node1 = node
                firstNodeFound = True
            if node.identifier == secondNode:
                node2 = node
                secondNodeFound = True
        if firstNodeFound and secondNodeFound:
            visitedNodes.append(node1.identifier)
            for index in workingValues:
                if index[nodeIndex] == node1.identifier:
                    index[nodeDistanceIndex] = 0
            while unvisitedNodes:
                for visitedNode in visitedNodes:
                    node = None
                    for nodes in self.nodes:
                        if nodes.identifier == visitedNode:
                            node = nodes
                    currentDistance = None
                    for index in workingValues:
                        if index[nodeIndex] == node.identifier:
                            currentDistance = index[nodeDistanceIndex]
                    for edge in node.edges:
                        if edge.nextNode.identifier in unvisitedNodes:
                            totalDistance = None
                            nodeInd = None
                            for index in range(len(workingValues)):
                                if workingValues[index][nodeIndex] == edge.nextNode.identifier:
                                    totalDistance = workingValues[index][nodeDistanceIndex]
                                    nodeInd = index
                            if totalDistance > (currentDistance + edge.weight):
                                workingValues[nodeInd][nodeDistanceIndex] = (currentDistance + edge.weight)
                                workingValues[nodeInd][previousNodeIndex] = node.identifier
                for index in workingValues:
                    smallestLength = math.inf
                    for index in workingValues:
                        if index[nodeDistanceIndex] < smallestLength and index[nodeIndex] in unvisitedNodes:
                            visitedNodes.append(index[nodeIndex])
                            unvisitedNodes.remove(index[nodeIndex])
            distanceFound = None
            for index in workingValues:
                if index[nodeIndex] == secondNode:
                    distanceFound = index[nodeDistanceIndex]
            print(f"The shortest length between {firstNode} and {secondNode} is {distanceFound}")
        else:
            print(f"Could not find the shortest distance between {firstNode} and {secondNode} as one or more of the given nodes could not be found in the network")
        print(workingValues)
            
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

network.allEdges()
print()
network.shortestDistance("A", "D")