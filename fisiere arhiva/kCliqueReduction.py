from posixpath import join
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


def join_clauses(clauses):
    p = ""
    for c in clauses:
        p += c + " ^ "
    return p[:-3]


def clauses_1():
    clauses = []
    for i in range(1, k + 1):
        c = "("
        for v in range(1, N + 1):
            c += f"L{v}{i} V "
        c = c[:-3]
        c += ")"
        clauses.append(c)
    return clauses


def clauses_2():
    clauses = []
    for v in range(1, N + 1):
        for i in range(1, k):
            for j in range(i + 1, k + 1):
                c = f"(~L{v}{i} V ~L{v}{j})"
                clauses.append(c)
    return clauses


def clauses_3(edges):
    clauses = []
    for u in range(1, N):
        for v in range(u + 1, N + 1):
            edge = [u, v]
            for i in range(1, k + 1):
                for j in range(1, k + 1):
                    if i == j:
                        continue
                    if edge not in edges and list(reversed(edge)) not in edges:
                        c = f"(~L{u}{i} V ~L{v}{j})"
                        clauses.append(c)
    return clauses


if __name__ == '__main__':
    k, N, M, edges = read()
    clauses = []
    clauses.extend(clauses_1())
    clauses.extend(clauses_2())
    clauses.extend(clauses_3(edges))
    print(join_clauses(clauses))
    # print("(L11 V L21 V L31 V L41 V L51 V L61 V L71 V L81 V L91 V L101) ^ (L12 V L22 V L32 V L42 V L52 V L62 V L72 V L82 V L92 V L102) ^ (L13 V L23 V L33 V L43 V L53 V L63 V L73 V L83 V L93 V L103) ^ (L14 V L24 V L34 V L44 V L54 V L64 V L74 V L84 V L94 V L104) ^ (L15 V L25 V L35 V L45 V L55 V L65 V L75 V L85 V L95 V L105) ^ (L16 V L26 V L36 V L46 V L56 V L66 V L76 V L86 V L96 V L106) ^ (L17 V L27 V L37 V L47 V L57 V L67 V L77 V L87 V L97 V L107) ^ (~L11 V ~L12) ^ (~L11 V ~L13) ^ (~L11 V ~L14) ^ (~L11 V ~L15) ^ (~L11 V ~L16) ^ (~L11 V ~L17) ^ (~L12 V ~L13) ^ (~L12 V ~L14) ^ (~L12 V ~L15) ^ (~L12 V ~L16) ^ (~L12 V ~L17) ^ (~L13 V ~L14) ^ (~L13 V ~L15) ^ (~L13 V ~L16) ^ (~L13 V ~L17) ^ (~L14 V ~L15) ^ (~L14 V ~L16) ^ (~L14 V ~L17) ^ (~L15 V ~L16) ^ (~L15 V ~L17) ^ (~L16 V ~L17) ^ (~L21 V ~L22) ^ (~L21 V ~L23) ^ (~L21 V ~L24) ^ (~L21 V ~L25) ^ (~L21 V ~L26) ^ (~L21 V ~L27) ^ (~L22 V ~L23) ^ (~L22 V ~L24) ^ (~L22 V ~L25) ^ (~L22 V ~L26) ^ (~L22 V ~L27) ^ (~L23 V ~L24) ^ (~L23 V ~L25) ^ (~L23 V ~L26) ^ (~L23 V ~L27) ^ (~L24 V ~L25) ^ (~L24 V ~L26) ^ (~L24 V ~L27) ^ (~L25 V ~L26) ^ (~L25 V ~L27) ^ (~L26 V ~L27) ^ (~L31 V ~L32) ^ (~L31 V ~L33) ^ (~L31 V ~L34) ^ (~L31 V ~L35) ^ (~L31 V ~L36) ^ (~L31 V ~L37) ^ (~L32 V ~L33) ^ (~L32 V ~L34) ^ (~L32 V ~L35) ^ (~L32 V ~L36) ^ (~L32 V ~L37) ^ (~L33 V ~L34) ^ (~L33 V ~L35) ^ (~L33 V ~L36) ^ (~L33 V ~L37) ^ (~L34 V ~L35) ^ (~L34 V ~L36) ^ (~L34 V ~L37) ^ (~L35 V ~L36) ^ (~L35 V ~L37) ^ (~L36 V ~L37) ^ (~L41 V ~L42) ^ (~L41 V ~L43) ^ (~L41 V ~L44) ^ (~L41 V ~L45) ^ (~L41 V ~L46) ^ (~L41 V ~L47) ^ (~L42 V ~L43) ^ (~L42 V ~L44) ^ (~L42 V ~L45) ^ (~L42 V ~L46) ^ (~L42 V ~L47) ^ (~L43 V ~L44) ^ (~L43 V ~L45) ^ (~L43 V ~L46) ^ (~L43 V ~L47) ^ (~L44 V ~L45) ^ (~L44 V ~L46) ^ (~L44 V ~L47) ^ (~L45 V ~L46) ^ (~L45 V ~L47) ^ (~L46 V ~L47) ^ (~L51 V ~L52) ^ (~L51 V ~L53) ^ (~L51 V ~L54) ^ (~L51 V ~L55) ^ (~L51 V ~L56) ^ (~L51 V ~L57) ^ (~L52 V ~L53) ^ (~L52 V ~L54) ^ (~L52 V ~L55) ^ (~L52 V ~L56) ^ (~L52 V ~L57) ^ (~L53 V ~L54) ^ (~L53 V ~L55) ^ (~L53 V ~L56) ^ (~L53 V ~L57) ^ (~L54 V ~L55) ^ (~L54 V ~L56) ^ (~L54 V ~L57) ^ (~L55 V ~L56) ^ (~L55 V ~L57) ^ (~L56 V ~L57) ^ (~L61 V ~L62) ^ (~L61 V ~L63) ^ (~L61 V ~L64) ^ (~L61 V ~L65) ^ (~L61 V ~L66) ^ (~L61 V ~L67) ^ (~L62 V ~L63) ^ (~L62 V ~L64) ^ (~L62 V ~L65) ^ (~L62 V ~L66) ^ (~L62 V ~L67) ^ (~L63 V ~L64) ^ (~L63 V ~L65) ^ (~L63 V ~L66) ^ (~L63 V ~L67) ^ (~L64 V ~L65) ^ (~L64 V ~L66) ^ (~L64 V ~L67) ^ (~L65 V ~L66) ^ (~L65 V ~L67) ^ (~L66 V ~L67) ^ (~L71 V ~L72) ^ (~L71 V ~L73) ^ (~L71 V ~L74) ^ (~L71 V ~L75) ^ (~L71 V ~L76) ^ (~L71 V ~L77) ^ (~L72 V ~L73) ^ (~L72 V ~L74) ^ (~L72 V ~L75) ^ (~L72 V ~L76) ^ (~L72 V ~L77) ^ (~L73 V ~L74) ^ (~L73 V ~L75) ^ (~L73 V ~L76) ^ (~L73 V ~L77) ^ (~L74 V ~L75) ^ (~L74 V ~L76) ^ (~L74 V ~L77) ^ (~L75 V ~L76) ^ (~L75 V ~L77) ^ (~L76 V ~L77) ^ (~L81 V ~L82) ^ (~L81 V ~L83) ^ (~L81 V ~L84) ^ (~L81 V ~L85) ^ (~L81 V ~L86) ^ (~L81 V ~L87) ^ (~L82 V ~L83) ^ (~L82 V ~L84) ^ (~L82 V ~L85) ^ (~L82 V ~L86) ^ (~L82 V ~L87) ^ (~L83 V ~L84) ^ (~L83 V ~L85) ^ (~L83 V ~L86) ^ (~L83 V ~L87) ^ (~L84 V ~L85) ^ (~L84 V ~L86) ^ (~L84 V ~L87) ^ (~L85 V ~L86) ^ (~L85 V ~L87) ^ (~L86 V ~L87) ^ (~L91 V ~L92) ^ (~L91 V ~L93) ^ (~L91 V ~L94) ^ (~L91 V ~L95) ^ (~L91 V ~L96) ^ (~L91 V ~L97) ^ (~L92 V ~L93) ^ (~L92 V ~L94) ^ (~L92 V ~L95) ^ (~L92 V ~L96) ^ (~L92 V ~L97) ^ (~L93 V ~L94) ^ (~L93 V ~L95) ^ (~L93 V ~L96) ^ (~L93 V ~L97) ^ (~L94 V ~L95) ^ (~L94 V ~L96) ^ (~L94 V ~L97) ^ (~L95 V ~L96) ^ (~L95 V ~L97) ^ (~L96 V ~L97) ^ (~L101 V ~L102) ^ (~L101 V ~L103) ^ (~L101 V ~L104) ^ (~L101 V ~L105) ^ (~L101 V ~L106) ^ (~L101 V ~L107) ^ (~L102 V ~L103) ^ (~L102 V ~L104) ^ (~L102 V ~L105) ^ (~L102 V ~L106) ^ (~L102 V ~L107) ^ (~L103 V ~L104) ^ (~L103 V ~L105) ^ (~L103 V ~L106) ^ (~L103 V ~L107) ^ (~L104 V ~L105) ^ (~L104 V ~L106) ^ (~L104 V ~L107) ^ (~L105 V ~L106) ^ (~L105 V ~L107) ^ (~L106 V ~L107) ^ (~L11 V ~L52) ^ (~L11 V ~L53) ^ (~L11 V ~L54) ^ (~L11 V ~L55) ^ (~L11 V ~L56) ^ (~L11 V ~L57) ^ (~L12 V ~L51) ^ (~L12 V ~L53) ^ (~L12 V ~L54) ^ (~L12 V ~L55) ^ (~L12 V ~L56) ^ (~L12 V ~L57) ^ (~L13 V ~L51) ^ (~L13 V ~L52) ^ (~L13 V ~L54) ^ (~L13 V ~L55) ^ (~L13 V ~L56) ^ (~L13 V ~L57) ^ (~L14 V ~L51) ^ (~L14 V ~L52) ^ (~L14 V ~L53) ^ (~L14 V ~L55) ^ (~L14 V ~L56) ^ (~L14 V ~L57) ^ (~L15 V ~L51) ^ (~L15 V ~L52) ^ (~L15 V ~L53) ^ (~L15 V ~L54) ^ (~L15 V ~L56) ^ (~L15 V ~L57) ^ (~L16 V ~L51) ^ (~L16 V ~L52) ^ (~L16 V ~L53) ^ (~L16 V ~L54) ^ (~L16 V ~L55) ^ (~L16 V ~L57) ^ (~L17 V ~L51) ^ (~L17 V ~L52) ^ (~L17 V ~L53) ^ (~L17 V ~L54) ^ (~L17 V ~L55) ^ (~L17 V ~L56) ^ (~L21 V ~L92) ^ (~L21 V ~L93) ^ (~L21 V ~L94) ^ (~L21 V ~L95) ^ (~L21 V ~L96) ^ (~L21 V ~L97) ^ (~L22 V ~L91) ^ (~L22 V ~L93) ^ (~L22 V ~L94) ^ (~L22 V ~L95) ^ (~L22 V ~L96) ^ (~L22 V ~L97) ^ (~L23 V ~L91) ^ (~L23 V ~L92) ^ (~L23 V ~L94) ^ (~L23 V ~L95) ^ (~L23 V ~L96) ^ (~L23 V ~L97) ^ (~L24 V ~L91) ^ (~L24 V ~L92) ^ (~L24 V ~L93) ^ (~L24 V ~L95) ^ (~L24 V ~L96) ^ (~L24 V ~L97) ^ (~L25 V ~L91) ^ (~L25 V ~L92) ^ (~L25 V ~L93) ^ (~L25 V ~L94) ^ (~L25 V ~L96) ^ (~L25 V ~L97) ^ (~L26 V ~L91) ^ (~L26 V ~L92) ^ (~L26 V ~L93) ^ (~L26 V ~L94) ^ (~L26 V ~L95) ^ (~L26 V ~L97) ^ (~L27 V ~L91) ^ (~L27 V ~L92) ^ (~L27 V ~L93) ^ (~L27 V ~L94) ^ (~L27 V ~L95) ^ (~L27 V ~L96) ^ (~L41 V ~L102) ^ (~L41 V ~L103) ^ (~L41 V ~L104) ^ (~L41 V ~L105) ^ (~L41 V ~L106) ^ (~L41 V ~L107) ^ (~L42 V ~L101) ^ (~L42 V ~L103) ^ (~L42 V ~L104) ^ (~L42 V ~L105) ^ (~L42 V ~L106) ^ (~L42 V ~L107) ^ (~L43 V ~L101) ^ (~L43 V ~L102) ^ (~L43 V ~L104) ^ (~L43 V ~L105) ^ (~L43 V ~L106) ^ (~L43 V ~L107) ^ (~L44 V ~L101) ^ (~L44 V ~L102) ^ (~L44 V ~L103) ^ (~L44 V ~L105) ^ (~L44 V ~L106) ^ (~L44 V ~L107) ^ (~L45 V ~L101) ^ (~L45 V ~L102) ^ (~L45 V ~L103) ^ (~L45 V ~L104) ^ (~L45 V ~L106) ^ (~L45 V ~L107) ^ (~L46 V ~L101) ^ (~L46 V ~L102) ^ (~L46 V ~L103) ^ (~L46 V ~L104) ^ (~L46 V ~L105) ^ (~L46 V ~L107) ^ (~L47 V ~L101) ^ (~L47 V ~L102) ^ (~L47 V ~L103) ^ (~L47 V ~L104) ^ (~L47 V ~L105) ^ (~L47 V ~L106) ^ (~L61 V ~L72) ^ (~L61 V ~L73) ^ (~L61 V ~L74) ^ (~L61 V ~L75) ^ (~L61 V ~L76) ^ (~L61 V ~L77) ^ (~L62 V ~L71) ^ (~L62 V ~L73) ^ (~L62 V ~L74) ^ (~L62 V ~L75) ^ (~L62 V ~L76) ^ (~L62 V ~L77) ^ (~L63 V ~L71) ^ (~L63 V ~L72) ^ (~L63 V ~L74) ^ (~L63 V ~L75) ^ (~L63 V ~L76) ^ (~L63 V ~L77) ^ (~L64 V ~L71) ^ (~L64 V ~L72) ^ (~L64 V ~L73) ^ (~L64 V ~L75) ^ (~L64 V ~L76) ^ (~L64 V ~L77) ^ (~L65 V ~L71) ^ (~L65 V ~L72) ^ (~L65 V ~L73) ^ (~L65 V ~L74) ^ (~L65 V ~L76) ^ (~L65 V ~L77) ^ (~L66 V ~L71) ^ (~L66 V ~L72) ^ (~L66 V ~L73) ^ (~L66 V ~L74) ^ (~L66 V ~L75) ^ (~L66 V ~L77) ^ (~L67 V ~L71) ^ (~L67 V ~L72) ^ (~L67 V ~L73) ^ (~L67 V ~L74) ^ (~L67 V ~L75) ^ (~L67 V ~L76) ^ (~L91 V ~L102) ^ (~L91 V ~L103) ^ (~L91 V ~L104) ^ (~L91 V ~L105) ^ (~L91 V ~L106) ^ (~L91 V ~L107) ^ (~L92 V ~L101) ^ (~L92 V ~L103) ^ (~L92 V ~L104) ^ (~L92 V ~L105) ^ (~L92 V ~L106) ^ (~L92 V ~L107) ^ (~L93 V ~L101) ^ (~L93 V ~L102) ^ (~L93 V ~L104) ^ (~L93 V ~L105) ^ (~L93 V ~L106) ^ (~L93 V ~L107) ^ (~L94 V ~L101) ^ (~L94 V ~L102) ^ (~L94 V ~L103) ^ (~L94 V ~L105) ^ (~L94 V ~L106) ^ (~L94 V ~L107) ^ (~L95 V ~L101) ^ (~L95 V ~L102) ^ (~L95 V ~L103) ^ (~L95 V ~L104) ^ (~L95 V ~L106) ^ (~L95 V ~L107) ^ (~L96 V ~L101) ^ (~L96 V ~L102) ^ (~L96 V ~L103) ^ (~L96 V ~L104) ^ (~L96 V ~L105) ^ (~L96 V ~L107) ^ (~L97 V ~L101) ^ (~L97 V ~L102) ^ (~L97 V ~L103) ^ (~L97 V ~L104) ^ (~L97 V ~L105) ^ (~L97 V ~L106)")
