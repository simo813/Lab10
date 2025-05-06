import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.DAO = DAO()

    def buildGraph(self, anno):
        listaNodiFiltrati = self.DAO.getNodes(anno)
        listaConnessioniFiltrate = self.DAO.getConnections(anno)
        graph = nx.Graph()
        for node in listaNodiFiltrati:
            graph.add_node(node)
        for connection in listaConnessioniFiltrate:
            graph.add_edge(connection[0], connection[1])


        return graph