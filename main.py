import networkx as nx
from g import *


"""Manage tags"""
def genTags(size):
    global tags
    tags=[]
    for k in range(0,size):
        tags.append(False)

def clearTags():
    for k in range(0,len(tags)):
        tags[k]=False

def tagNodei(node):
    tags[node]=True

def isTag(node):
    return tags[node]

def isAllTag():
    for k in tags:
        if not tags:
            return False
    return True



"""Assets for isConnexe()"""
def movePossibilities(node,edgesList,nodesList):
    possilities=[]
    tagNodei(node)
    for k in edgesList :
        if k[0]==nodesList[node] and not isTag(node):
            possilities += movePossibilities(k[0],edgesList,nodesList)
    return possilities


"""Function"""
def isConnexe(edgesList,nodesList):
    genTags(len(nodesList))
    print tags
    for node in nodesList:
        movePossibilities(node,edgesList,nodesList)
        clearTags()
        if not isAllTag():
            return False
    return True

g = genRandomGraph(5,100)
print(g.nodes())
print(g.edges())
#displayGraph(g)
print(isConnexe(g.edges(),g.nodes()))