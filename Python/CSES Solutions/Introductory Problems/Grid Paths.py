def hamiltonians(G, vis = []):
    if not vis:
        for n in G:
            for p in hamiltonians(G, [n]):
                yield p
    else:
        dests = set(G[vis[-1]]) - set(vis)
        if not dests and len(vis) == len(G):
            yield vis
        for n in dests:
            for p in hamiltonians(G, vis + [n]):
                yield p
G = {'a' : 'bc', 'b' : 'ad', 'c' : 'b', 'd' : 'ac'}
print(list(hamiltonians(G)))