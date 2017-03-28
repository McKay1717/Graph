#!/usr/bin/env python
import itertools
import matplotlib.pyplot as plt
import networkx as nx
from heapq import heappush, heappop
from itertools import count
from random import randrange


def genRandomGraph(NodeNumber,NumberOfLink):
    G = nx.Graph()
    for i in range(0,NumberOfLink):
        exit = True
        while exit:
            n1 = randrange(0,NodeNumber)
            n2 = randrange(0, NodeNumber)
            while n1 == n2 :
                n2 = randrange(0,NodeNumber)
            if not (G.has_edge(n1,n2)):
                G.add_edge(n1,n2,weight=randrange(1,100))
                exit = not exit
    while(len(G.edge) != NodeNumber):
        G.add_node(randrange(0,NodeNumber))
    return G

def displayGraph(G):
    pos = nx.circular_layout(G)
    nx.draw_networkx_nodes(G,pos,node_size=700)
    nx.draw_networkx_edges(G,pos,width=6)
    nx.draw_networkx_edge_labels(G,pos)

    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
    plt.axis('off')
    plt.show()

def dijtra(G, source, weight='weight'):
    c1 = heappush
    c2 = heappop
    dist = {}
    s= {source: 0}
    c = count()
    tmp = []
    c1(tmp, (0, next(c), source))
    while tmp:
        (d, _, v) = c2(tmp)
        if v in dist:
            continue
        dist[v] = d
        Gcontent = iter(G[v].items())
        for i, edgedata in Gcontent:
            tmp_dist = dist[v] + edgedata.get(weight, 1)
            if i not in s or tmp_dist < s[i]:
                s[i] = tmp_dist
                c1(tmp, (tmp_dist, next(c), i))
    return dist

def dijtraAllG(G,weight='weight'):
    chemins = {}
    for n in G:
        chemins[n] = dijtra(G, n,weight=weight)
    return chemins


def TSV(G):
    df = dijtraAllG(G)
    ar = list(itertools.permutations(df, len(G.node)))
    min = pow(10, 99)
    id = 0
    for item in ar:
        l = list(item)
        l.append(list(item)[0])
        bad = False
        sum = 0
        for i in range(1, len(l)):
            sum += df[l[i - 1]][l[i]]
            if (sum > min):
                bad = not bad
                break
        if (not bad and sum < min):
            id = l
            min = sum
    print("Le plus court est " + str(id) + " et sa valeur est " + str(min))


G = genRandomGraph(11, 12)

TSV(G)

displayGraph(G)
