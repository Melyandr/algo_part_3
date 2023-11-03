def dfs_helper(vertex, adj, visited):
    if visited[vertex]:
        return

    visited[vertex] = True

    for adjacency_vertex in adj[vertex]:
        if not visited[adjacency_vertex]:
            dfs_helper(adjacency_vertex, adj, visited)


def get_transpose_graph(adj):
    n = len(adj)
    trans_adj = [[] for _ in range(n)]
    for vertex in range(n):
        for adjacency_vertex in adj[vertex]:
            trans_adj[adjacency_vertex].append(vertex)
    return trans_adj


def initialize_visited(n):
    return [False for _ in range(n)]


def find_all_mother_vertices(adj):
    n = len(adj)
    visited = initialize_visited(n)

    last_dfs_called_on = -1

    for vertex in range(n):
        if not visited[vertex]:
            dfs_helper(vertex, adj, visited)
            last_dfs_called_on = vertex

    visited = initialize_visited(n)
    dfs_helper(last_dfs_called_on, adj, visited)

    for vertex in range(n):
        if not visited[vertex]:
            return -1

    motherVertex = last_dfs_called_on

    trans_adj = get_transpose_graph(adj)

    visited = initialize_visited(n)
    dfs_helper(motherVertex, trans_adj, visited)

    ans = []

    for vertex in range(n):
        if visited[vertex]:
            ans.append(vertex)

    return ans[0]


if __name__ == "__main__":
    with open("../test/input2.txt", "r") as input_file:
        lines = input_file.readlines()

    adj = []
    for line in lines:
        part = list(map(int, line.split(" ")))
        adj.append(part[1:])

    motherVertices = find_all_mother_vertices(adj)

    with open("../test/output.txt", "w") as output_file:
        output_file.writelines(str(motherVertices))
        output_file.close()
