class DiGraph:
    def __init__(self):
        self.adj = {} #a dictionary to map adjacent nodes

    def addNode(self,u): #Add node u to graph
        assert u not in self.adj, "Duplicate Node hbb"
        self.adj[u] = [] #Empty list which we will fill up when we connect

    def connect(self,u,v): #Connect node u to node v
        assert u in self.adj and v in self.adj, "Node not in graph"
        assert v not in self.adj[u], "Already connected mate"
        self.adj[u].append(v) #appending v to the adjacency list of u

    def __str__(self):
        #Want to print graph
        s = '' #empty string
        for u in self.adj:
            t = ''
            for v in self.adj[u]:
                t = t + str(v) + ','
            s = s + str(u) + ' : '+ t[:-1] + '\n' #t[:-1] eliminates last element, which is comma
        return s

class UnDiGraph(DiGraph):
    def connect(self,u,v):
        DiGraph.connect(self,u,v)
        DiGraph.connect(self,v,u)

class Stack(list): #Stack inherits from list
    def push(self,value):
        self.append(value)
    def top(self):
        assert not self.isEmpty(), "Stack Empty!"
        return self[len(self)-1]
    def isEmpty(self):
        return (len(self)==0)

class Queue:
    def __init__(self,maxSize = 10): #Doesn't have to be 10
        self.L = [None]*maxSize
        self.size = 0
        self.maxSize = maxSize
        self.tail = 0
        self.head = 0

    def enqueue(self,value):
        assert not self.isFull(), "Queue Full"
        self.L[self.tail] = value
        if self.tail<self.maxSize-1:
            self.tail = self.tail + 1
        else:
            self.tail = 0
        self.size = self.size + 1

    def dequeue(self):
        assert not self.isEmpty(), "Queue empty"
        val = self.L[self.head]
        if self.head <self.maxSize - 1:
            self.head = self.head + 1
        else:
            self.head = 0
        self.size = self.size - 1
        return val

    def peakhead(self): #returns head value, raises exception if empty
        assert not self.isEmpty(), "Queue empty"
        return self.L[self.head]

    def isFull(self):
        return self.size == self.maxSize

    def isEmpty(self):
        return self.size == 0



    def __str__(self):
        s = '['
        index = self.head
        count = 0
        while count!=self.size:
            s = s+str(self.L[index])+","
            if index<self.maxSize-1:
                index = index + 1
            else:
                index = 0
            count = count + 1
        if self.size != 0:
            s = s[:-1]
        return s + ']'
    def __len__(self):

        return self.size


def DFSVisit(G,u,parent):
    #Recursive DFS function
    for v in G.adj[u]:
        if v not in parent:
            #If not visited yet, to avoid cycles
            parent[v] = u
            DFSVisit(G,v,parent)

def findReachableNodes(G,s): #From starting point in G, which is s, need all routes
    assert s in G.adj, "Node not in graph"
    parent = {s:None} #Dictionary to track if node is visited or not
    DFSVisit(G,s,parent)
    return list(parent.keys()) #returns list of nodes

def BFS(G,s):
    assert s in G.adj, "Not in graph"
    parent = {s:None} #To record visited nodes
    distance = {s:0} #To initialize how far we are from original node
    #Initialize a qeueue of max size = number of nodes
    Q = Queue(len(G.adj))
    Q.enqueue(s)
    while not Q.isEmpty():
        u = Q.dequeue()
        for v in G.adj[u]:
            if v not in distance: #if not accessed yet
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.enqueue(v)
    return(distance,parent)


G = DiGraph()
G.addNode("A")
G.addNode("B")
G.addNode("C")
G.addNode("D")
G.addNode("E")
G.connect("A","B")
G.connect("A","C")
G.connect("B","C")
G.connect("B","E")
G.connect("D","B")
G.connect("D","E")
print(G)
print(findReachableNodes(G,"A"))
print(BFS(G,"A"))
