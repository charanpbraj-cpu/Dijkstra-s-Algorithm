INF = 999999

# Adjacency Matrix
graph = [
    [0, 10, 0, 5, 0],
    [10, 0, 1, 2, 0],
    [0, 1, 0, 0, 4],
    [5, 2, 0, 0, 2],
    [0, 0, 4, 2, 0]
]

n = len(graph)

source = int(input("Enter the source vertex (0-4): "))

distance = [INF] * n
visited = [False] * n

distance[source] = 0

for i in range(n):

    min_distance = INF
    u = -1

    for j in range(n):
        if not visited[j] and distance[j] < min_distance:
            min_distance = distance[j]
            u = j

    visited[u] = True

    for v in range(n):
        if graph[u][v] != 0 and not visited[v]:
            if distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

print("\nShortest Distance from Source Vertex", source)

for i in range(n):
    print("Vertex", i, ":", distance[i])