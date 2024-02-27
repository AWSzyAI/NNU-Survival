
# read file "南京地铁.txt"，根据其中的数据构建无向有权图的邻接链表表示法，并打印邻接表
# 使用Dijkstra算法求单源最短（省时）路径，并打印最短路径
# 调用networkx库实现单源最短（省时）路径的可视化图形显示


import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.next = []

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class NanjingMetro:
    def __init__(self):
        self.Vertexes = [] 
        self.Edges = []

    def ImportGraph(self,filename):
        with open(filename,'r') as f:
            print("Importing "+filename)

            lines = f.readlines()

            AmountOfGraph = int(lines[0]) 
            print("Amount of Graph:",AmountOfGraph)

            lines = lines[1:]
            
            while(AmountOfGraph>0):
                AmountOfGraph -= 1
                NumberOfEdge = int(lines[0])
                print("Amount of Edge:",NumberOfEdge)
                lines = lines[1:]
                for i in range(NumberOfEdge):
                    start, end, weight = lines[i].split(",")
                    if self.checkVertex(start) == False:
                        self.Vertexes.append(Vertex(start))
                    if self.checkVertex(end) == False:  
                        self.Vertexes.append(Vertex(end))

                    
                    self.setVertex(start).next.append(end)
                    self.setVertex(end).next.append(start)

                    edge = Edge(start, end, int(weight))
                    if edge not in self.Edges:
                        self.Edges.append(edge)
                    edge = Edge(end, start, int(weight))
                    if edge not in self.Edges:
                        self.Edges.append(edge)
                lines = lines[NumberOfEdge:]
            print("Importing finished")



    def getNumberOfVertexes(self):
        return len(self.Vertexes)
    def getNumberOfEdges(self):
        return len(self.Edges)/2  #无向图
    
    def checkVertex(self,name):
        for i in self.Vertexes:
            if i.name == name:
                return True
        return False
    def setVertex(self,name):
        for i in self.Vertexes:
            if i.name == name:
                return i
    def getVertexIndex(self,name):
        for i in range(len(self.Vertexes)):
            if name == self.Vertexes[i].name:
                return i
    def setEdge(self,start,end):
        for i in self.Edges:
            if i.start == start and i.end == end:
                return i

    def print_adjacency_list(self):
        # list = [i.name for i in self.Vertexes]
        # print(list) 
        for vertex in self.Vertexes:
            print(vertex.name,":",end=" ")
            for i in vertex.next:
                #print(i,self.setEdge(vertex.name,i).weight,end=" ")
                print(i,end=" ")
            print()


    # 求A站到B站到最短路线 龙眠大道——学则路
    # 给出Dijstra算法
    def ShortPath(self,start:str,end:str):
        parent = {} #节点关系，用于回溯
        distance = {} #起点到各个节点的距离
        # init
        for i in self.Vertexes:
            distance[i.name] = float('inf')
        distance[start] = 0

        queue = []
        heapq.heappush(queue,[0,start])
        while len(queue) > 0:
            d, v = heapq.heappop(queue)
            if d > distance[v]:
                continue
            for i in self.setVertex(v).next:
                if distance[i] > distance[v] + self.setEdge(v,i).weight:
                    distance[i] = distance[v] + self.setEdge(v,i).weight
                    parent[i] = v
                    heapq.heappush(queue,[distance[i],i])
        print("Distance from",start,"to",end,"=",distance[end])
        path = [end]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        self.showPath(path)


    

 

    def showPath(self, path):
        G = nx.Graph()
        for vertex in self.Vertexes:
            G.add_node(vertex.name, name=vertex.name)
            for i in vertex.next:
                G.add_edge(vertex.name, i, weight=self.setEdge(vertex.name, i).weight)

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color='gray', node_size=500, alpha=0.8)
        nx.draw_networkx_edges(G, pos, edge_color='gray')

        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

        for i in path:
            nx.draw_networkx_nodes(G, pos, nodelist=[i], node_color='red', node_size=1000, alpha=0.8)

        nx.draw_networkx_labels(G, pos, font_family="SimHei", font_size=12) # 修改这里

        plt.axis('off')
        plt.show()




if __name__ == '__main__':
    filename = "./南京地铁.txt"
    nm = NanjingMetro()
    nm.ImportGraph(filename)
    nm.print_adjacency_list()
    nm.ShortPath("龙眠大道","学则路")