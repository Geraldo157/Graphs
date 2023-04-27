def valid_word(g, s, t, w):
    if g is None or len(g) == 0 or s is None or t is None or w is None:
        return None

    ponto_atual = s
    for i, c in enumerate(w):
        proximo_vertice = [v for u, v, label in g.edges(ponto_atual, data="label") if label == c]
        if not proximo_vertice:
            return False
        ponto_atual = proximo_vertice[0]
    return ponto_atual == t
