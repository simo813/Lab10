import flet as ft
import networkx as nx


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls = []
        self._view.update_page()
        anno = self._view._txtAnno.value
        if anno is None or anno == "" or self.is_integer(anno) != True or int(anno) > 2016 or int(anno) < 1816:
            self._view.create_alert("Inserire il valore correttamente")
            return
        graph = self._model.buildGraph(int(anno))
        componentiConnesse = len(list(nx.connected_components(graph)))
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato correttamentre\n"
                                                      f"Il grafo ha {componentiConnesse}\n"
                                                      f"Di seguito il dettaglio sui nodi\n"
                                                        f"{self.listaNodi(graph)}"))
        self._view.update_page()

    def is_integer(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def listaNodi(self, graph):
        stampa = ""
        for node in graph:
            stampa += str(self._model.listaPaesi[node]) + " -- " + str(graph.degree(node)) + "\n"
        return stampa


