def minDistance(distances, included):
    min = float('inf')
    min_index = -1

    for v, _ in enumerate(included):
        if distances[v] <= min and not included[v]:
            min = distances[v]
            min_index = v
    print("min_index: ", min_index)
    print("min_val: ", min)
    return min_index


def dijkstra(graph, s):
    distances = [float('inf') for x in graph]
    included = [False for x in graph]
    distances[s] = 0
    for _ in range(len(graph) - 1):
        min_key = minDistance(distances, included)
        included[min_key] = True

        for v in range(len(graph)):
            print(included)
            print(distances)
            if not included[v] and graph[min_key][v] and distances[min_key] != float('inf') and distances[min_key] + graph[min_key][v] < distances[v]:
                distances[v] = distances[min_key] + graph[min_key][v]

    displaySolution(distances)


def displaySolution(distances):
    for k, d in enumerate(distances):
        if k == 0:
            continue
        charcode = chr(64 + k)
        print(f'Source -> Node{charcode}: {d}')


with open('dijk_input.txt') as f:
    lines = f.readlines()
    data = []
    # Loop through data
    for line in lines:
        # Push split data into array
        data.append([int(x) for x in line.split(' ')])

    dijkstra(data, 0)
