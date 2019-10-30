from pprint import pprint


def minKey(keys, included):
    min = float('inf')
    min_index = -1

    for v, _ in enumerate(included):
        if keys[v] < min and not included[v]:
            min = keys[v]
            min_index = v

    return min_index


def primMST(graph):
    # Array of who the parent of the node is
    parent = [0 for x in graph]
    # Minimum weights
    keys = [float('inf') for x in graph]
    # Have the vertices been included yet?
    included = [False for x in graph]

    parent[0] = -1
    keys[0] = 0

    for _ in range(len(parent) - 1):
        # Pull the minimum key
        min_key = minKey(keys, included)
        # Mark the key as used
        included[min_key] = True
        for v in range(len(graph)):
            # Loop through other vertices and find non-included vertices to pathfind to
            if graph[min_key][v] and not included[v] and graph[min_key][v] < keys[v]:
                parent[v] = min_key
                keys[v] = graph[min_key][v]
    printMST(graph, parent)


def printMST(graph, parent):
    # Initialize an empty array of same size as graph
    output = [[0 for x in y] for y in graph]
    # Pull values from the parent and map them to the new graph
    for k, v in enumerate(parent):
        # Skip the first iteration
        if v == -1:
            continue
        output[k][v] = graph[k][v]
        output[v][k] = graph[v][k]
    # Output as 2d whitespace delimeted array
    for row in output:
        print(*row, sep=" ")


with open('prim_input.txt') as f:
    lines = f.readlines()
    data = []
    # Loop through data
    for line in lines:
        # Push split data into array
        data.append([int(x) for x in line.split(' ')])

    primMST(data)
