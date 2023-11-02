def dfs_helper(u, adj, visited):
    if visited[u]:
        return

    visited[u] = True

    for v in adj[u]:
        if not visited[v]:
            dfs_helper(v, adj, visited)


def getTransposeGraph(adj):
    n = len(adj)
    trans_adj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            trans_adj[v].append(u)
    return trans_adj


def initialize_visited(n):
    return [False for _ in range(n)]


def findAllMotherVertices(adj):
    n = len(adj)
    visited = initialize_visited(n)

    last_dfs_called_on = -1

    for u in range(n):
        if not visited[u]:
            dfs_helper(u, adj, visited)
            last_dfs_called_on = u

    visited = initialize_visited(n)
    dfs_helper(last_dfs_called_on, adj, visited)

    for u in range(n):
        if not visited[u]:
            return -1

    motherVertex = last_dfs_called_on

    trans_adj = getTransposeGraph(adj)

    visited = initialize_visited(n)
    dfs_helper(motherVertex, trans_adj, visited)

    ans = []

    for u in range(n):
        if visited[u]:
            ans.append(u)

    return ans[0]


if __name__ == "__main__":
    with open("input2.txt", "r") as input_file:
        lines = input_file.readlines()

    adj = []
    for line in lines:
        part = list(map(int, line.split(" ")))
        adj.append(part[1:])

    motherVertices = findAllMotherVertices(adj)

    with open("output.txt", "w") as output_file:
        output_file.writelines(str(motherVertices))
        output_file.close()
