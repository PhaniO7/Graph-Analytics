#!/bin/python3

import heapq

road_nodes, road_edges = map(int, input().split())

graph = [dict() for _ in range(road_nodes + 1)]

for _ in range(road_edges):
    u, v, w = map(int, input().split())
    graph[u][v] = w  # keep only the latest edge

INF = 10**18

dist_all = [[INF] * (road_nodes + 1) for _ in range(road_nodes + 1)]

for src in range(1, road_nodes + 1):
    dist = dist_all[src]
    dist[src] = 0

    pq = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)

        if d != dist[u]:
            continue

        for v, w in graph[u].items():
            nd = d + w

            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

q = int(input())

for _ in range(q):
    x, y = map(int, input().split())

    if dist_all[x][y] == INF:
        print(-1)
    else:
        print(dist_all[x][y])
