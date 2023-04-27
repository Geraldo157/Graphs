import networkx as nx
# ALteração


def graph_density(G):
    if G is None:
        return None

    if G.is_multigraph():
        return None

    n = len(G.nodes)
    m = len(G.edges)

    if G.is_directed():
        max_edges = n * (n - 1)
    else:
        max_edges = n * (n - 1) / 2

    density = m / max_edges

    return round(density, 2)
