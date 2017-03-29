import networkx as nx
from g import *
from time import *
import networkx as nx

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
            nodePourLien = ''
            k = 0
            while i[k] != '(':
                nodePourLien += i[k]
                k += 1
            n = nodePourLien
            value = ''
            k +=1
            while i[k] != ')':
                value += i[k]
                k += 1
            edges.append([node_lien[0] ,n ,value ])


    G = nx.Graph()

    for n in nodes.split(","):
        G.add_node(int(n))

    for e in edges:

        G.add_edge(int(e[0]), int(e[1]), weight=int(e[2]))


    return G  # displayGraph(g)

def treateMatrice(matrix, d):
    nbNodeOK = 0
    nbNode = len(matrix) - 1
    sum=0
    chemin = [d]
    while (nbNodeOK != nbNode):
        index = minimal(matrix[chemin[-1]], chemin)
        sum+=matrix[chemin[-1]][index]
        chemin.append(index)
        nbNodeOK += 1
    chemin.append(d)
    sum+=matrix[chemin[-1]][d]
    return chemin,sum


def minimal(tab, chemin):
    min = -1
    index = -1
    for k in range(len(tab)):
        if ((min < 0 or (tab[k] > 0 and tab[k] < min)) and (k not in chemin)):
            min = tab[k]
            index = k
    return index



def bancDeTestSimple_Fichier():

    G = load("Graph/JeuDeTest/test10.txt")
    matrice = dijtraAllG(G)


    t_start = time()
    chemin,val=treateMatrice(matrice,1)
    t_stop= time()

    print t_stop-t_start
    print("Le plus court est "+str(chemin) +"et sa valeur est "+str(val))


def bancDeTestSimple_Random():

    G = genRandomGraph(100,200)
    matrice = dijtraAllG(G)


    t_start = time()
    chemin,val=treateMatrice(matrice,1)
    t_stop= time()

    print t_stop-t_start
    print("Le plus court est "+str(chemin) +"et sa valeur est "+str(val))


def bancDeTestOpti_Random():
    G = genRandomGraph(11, 20)
    matrice = dijtraAllG(G)

    t_start = time()
    id,min=TSV(G,matrice)
    t_stop = time()

    print t_stop - t_start
    print("Le plus court est " + str(id) + " et sa valeur est " + str(min))

bancDeTestOpti_Random()