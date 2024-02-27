import networkx as nx

G = nx.Graph()
G.add_node('a')
G.add_nodes_from(['b', 'c'])

G.add_nodes_from([
    ("竹山路",{"color":"red"}),
    ("龙眠大道",{"color":"blue"}),
])



H = nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)
G.nodes()