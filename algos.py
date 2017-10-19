#!/usr/bin/python

# Independent set algos

# E is represented by a adjacency matrix
# V is represented by an array

import csv
import numpy as np

# To read input
def read(file):
    with open(file, 'r') as input:
        n = int(next(input))
        E = np.zeros(shape=(n,n))
        i = 0
        for line in input:
            j = 0
            for x in line.split():
                E[i][j] = int(x)
                j = j + 1
            i = i + 1
    return (n, E)

def lineValue(l, limit):
    c = 0
    for k in l:
        if (k == 1):
            c = c + 1
        if (c > limit):
            return -1
    return c

def removeNeighbors(E, V, u):
    for i in range(len(E[u])):
        if (E[u][i] == 1):
            if (i in V):
                V.remove(i)
    V.remove(u)

def seekMaximumDegree(E, V):
    max = 0
    uMax = 0
    for i in V:
        c = 0
        for j in E[i]:
            c = c + j
        if (c > max):
            uMax = i
            max = c
    return uMax

def seekSmallVertex(E, V, limit):
    for i in V:
        d = lineValue(E[i], limit)
        if (d == 0):
            return (i, d)
        if (d == 1):
            return (i, d)
        if (d == 2):
            return (i, d)
    return (-1, -1)

# ==========================
            
# Algo R0
def algoR0(E, V):
    # If the graph is empty
    if (not V):
        return 0
    # If the graph has an isolated vertex
    v, d = seekSmallVertex(E, V, 0);
    if (d == 0):
        V.remove(v);
        return 1 + algoR0(E, V)
    # Otherwise
    # Find maximum degree
    u = seekMaximumDegree(E, V)
    V2 = list(V)
    V2.remove(u)
    removeNeighbors(E, V, u)
    return max(1 + algoR0(E, V), algoR0(E, V2))

# Algo R1
def algoR1(E, V):
    # If the graph is empty
    if (not V):
        return 0
    # If the graph has an isolated vertex or degree equals 1
    v, d = seekSmallVertex(E, V, 1);
    if (d == 0):
        V.remove(v);
        return 1 + algoR1(E, V)
    if (d == 1):
        removeNeighbors(E, V, v)
        return 1 + algoR1(E, V)
    # Otherwise
    # Find maximum degree
    u = seekMaximumDegree(E, V)
    V2 = list(V)
    V2.remove(u)
    removeNeighbors(E, V, u)
    return max(1 + algoR1(E, V), algoR1(E, V2))

# AlgoR2
def algoR2(E, V):
    # If the graph is empty
    if (not V):
        return 0
    v, d = seekSmallVertex(E, V, 2);
    if (d == 0):
        V.remove(v);
        return 1 + algoR2(E, V)
    if (d == 1):
        removeNeighbors(E, V, v)
        return 1 + algoR2(E, V)
    if (d == 2):
        u = -1
        w = -1
        for i in range(len(E[v])):
            if (i == 1):
                if (u == -1):
                    u = i
                else:
                    w = i
        # if u and w neighbors
        if (E[u][w] == 1):
            V.remove(u)
            V.remove(w)
            return 1 + algoR2(E, V)
        else:
            removeNeighbors(E, V, v)
            for i in range(len(E[u])):
                E[v][i] = E[u][i] or E[w][i] #cast int?
            E[v][v] = 0
            return 1 + algoR2(E, V)
    # Otherwise
    # Find maximum degree
    u = seekMaximumDegree(E, V)
    V2 = list(V)
    V2.remove(u)
    removeNeighbors(E, V, u)
    return max(1 + algoR2(E, V), algoR2(E, V2))

# Main
(n, E) = read('data/g30.in')
verticles = [i for i in range(n)]
print algoR1(E, verticles)
