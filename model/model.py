import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self.DAO = DAO()
        self.listaPaesi = {}

    def buildGraph(self, anno):
        self.listaPaesi = {}
        listaNodiFiltrati = self.DAO.getNodes(anno)
        listaConnessioniFiltrate = self.DAO.getConnections(anno)
        graph = nx.Graph()
        for paese in listaNodiFiltrati:
            graph.add_node(paese)
            self.listaPaesi[paese.code] = paese.name
        for connessione in listaConnessioniFiltrate:
            graph.add_edge(connessione[0], connessione[1])

        return graph