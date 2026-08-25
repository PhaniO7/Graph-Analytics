import sys
sys.setrecursionlimit(10**6)

def journeyToMoon(n, astronaut):
    from collections import defaultdict

    # Build adjacency list
    adj = defaultdict(list)
    for u, v in astronaut:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n

    def dfs(node):
        visited[node] = True
        size = 1
        for neighbor in adj[node]:
            if not visited[neighbor]:
                size += dfs(neighbor)
        return size

    # Find sizes of all connected components (countries)
    country_sizes = []
    for i in range(n):
        if not visited[i]:
            country_sizes.append(dfs(i))

    # Compute total valid pairs
    total_pairs = 0
    remaining = n
    for size in country_sizes:
        remaining -= size
        total_pairs += size * remaining

    return total_pairs


if __name__ == "__main__":
    n, p = map(int, sys.stdin.readline().split())
    astronaut = [tuple(map(int, sys.stdin.readline().split())) for _ in range(p)]
    print(journeyToMoon(n, astronaut))