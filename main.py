import networkx as nx
from g import *

"""Manage tags"""


def genTags(size):
    global tags
    tags = []
    for k in range(0, size):
        tags.append(False)


def clearTags():
    for k in range(0, len(tags)):
        tags[k] = False


def tagNodei(node):
    tags[node] = True


def isTag(node):
    return tags[node]


def isAllTag():
    for k in tags:
        if not tags:
            return False
    return True


"""Assets for isConnexe()"""


def movePossibilities(node, edgesList, nodesList):
    possilities = []
    tagNodei(node)
    for k in edgesList:
        if k[0] == nodesList[node] and not isTag(node):
            possilities += movePossibilities(k[0], edgesList, nodesList)
    return possilities


"""Function"""


def isConnexe(edgesList, nodesList):
    genTags(len(nodesList))
    print tags
    for node in nodesList:
        movePossibilities(node, edgesList, nodesList)
        clearTags()
        if not isAllTag():
            return False
    return True


"""Charge un graph depuis un fichier"""


def load(path):
    fich = open(path, 'r')
    str = fich.read()
    tabStr = str.split("\n")
    nodes = tabStr[0]
    edges = []

    for k in range(1, len(tabStr)):
        node_lien = tabStr[k].split(":")
        for i in node_lien[1].split(","):

            n = i[0]
            value = ''
            k = 2
            while i[k] != ')':
                value += i[k]
                k += 1
            edges.append([node_lien[0] ,n ,value ])

    G = nx.Graph()

    for n in nodes.split(","):
        G.add_node(n)

    for e in edges:

        G.add_edge(e[0], e[1], weight=e[2])


    return G  # displayGraph(g)
def treateMatrice(matrix, d):
    nbNodeOK = 0
    nbNode = len(matrix) - 1
    chemin = [d]
    while (nbNodeOK != nbNode):
        index = minimal(matrix[chemin[-1]], chemin)
        chemin.append(index)
        nbNodeOK += 1
    chemin.append(d)
    return chemin


def minimal(tab, chemin):
    min = -1
    index = -1
    for k in range(len(tab)):
        if ((min < 0 or (tab[k] > 0 and tab[k] < min)) and (k not in chemin)):
            min = tab[k]
            index = k
    return index


displayGraph(load("Graph/test.txt"))
