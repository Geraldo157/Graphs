import networkx as nx


def associate_astronauts(list_a):
    if list_a is not None and isinstance(list_a, list) and all(isinstance(item, tuple) and len(item) == 3 for item in list_a):
        grafo = nx.Graph()
        nodes = []

        for i, item in enumerate(list_a):
            first_name, last_name, country = item
            grafo.add_node(i, first_name=first_name, last_name=last_name, country=country)
            nodes.append((i, {"first_name": first_name, "last_name": last_name, "country": country}))

        for i in range(len(list_a)):
            for j in range(i + 1, len(list_a)):
                if list_a[i][2] != list_a[j][2]:
                    grafo.add_edge(i, j)

        retorno = grafo
    else:
        retorno = None
    return retorno
