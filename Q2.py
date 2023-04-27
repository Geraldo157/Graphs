def is_candidate(G, q_list, q, d):
    if G is None or q_list is None or q is None or d is None or q not in G.nodes or d < 0:
        return None

    if q in q_list:
        return None

    visited = set(q_list)
    stack = [v for v in q_list]

    while stack:
        v = stack.pop()
        for u in G.neighbors(v):
            if u not in visited and G[v][u]['weight'] <= d:
                visited.add(u)
                stack.append(u)

    return q in visited
