import sys
from itertools import combinations


def read():
    with open(sys.argv[1], 'r') as f:
        k = int(next(f))
        N = int(next(f))
        M = int(next(f))
        edges = []
        for line in f:
            edges.append([int(x) for x in line.split()])
    return k, N, M, edges


def is_k_clique(edges: list, subg):
    subg_edges = list(combinations(subg, 2))
    for edge in subg_edges:
        edge = list(edge)
        if edge not in edges and list(reversed(edge)) not in edges:
            return False
    return True


def subgs_k_length(k, N, edges, subg):
    if k == 0:
        if is_k_clique(edges, subg):
            print(True)
            sys.exit()
        return
    start = subg[-1] + 1 if len(subg) > 0 else 1
    for i in range(start, N + 2 - k):
        subg.append(i)
        subgs_k_length(k - 1, N, edges, subg)
        subg.pop()


def gen_subgs(k, N, edges):
    subgs_k_length(k, N, edges, [])


if __name__ == '__main__':
    k, N, M, edges = read()
    gen_subgs(k, N, edges)
    print(False)
