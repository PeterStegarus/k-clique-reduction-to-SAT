import sys


def read():
    with open(sys.argv[1], 'r') as f:
        k = int(next(f))
        N = int(next(f))
        M = int(next(f))
        edges = []
        for line in f:
            edges.append([int(x) for x in line.split()])
    return k, N, M, edges


def pairs(subg):
    pairs = []
    for i in subg:
        for j in subg:
            if i == j:
                continue
            pairs.append([i, j])
    return pairs


def is_k_clique(subg):
    if len(subg) != k:
        return False
    subg_edges = pairs(subg)
    for edge in subg_edges:
        if edge not in edges and list(reversed(edge)) not in edges:
            return False
    return True


def subgs_k_length(k, subg):
    if k == 0:
        return
    start = subg[-1] + 1 if len(subg) > 0 else 1
    for i in range(start, N + 1):
        subg.append(i)
        subgs.append(subg[:])
        subgs_k_length(k - 1, subg)
        subg.pop()


def gen_subgs():
    subgs_k_length(k, [])


if __name__ == '__main__':
    k, N, M, edges = read()
    subgs = []
    gen_subgs()
    for subg in subgs:
        if is_k_clique(subg):
            print(True)
            sys.exit()
    print(False)
