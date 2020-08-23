def dfs(graph, start, goal, depth, visited=[]):
    """Depth First Search"""

    if start == goal:
        return [goal]

    # maximum search depth reached, no path found
    if depth <= 0:
        return []

    # visit all neighbors
    for neigh in graph[start]:
        # only if edge exists
        if neigh not in visited:
            if path := dfs(graph, neigh, goal, depth-1, [*visited, start]):
                return [start, *path]

    # no path found
    return []


def iddfs(graph, start, goal):
    """Iterative Deepening Depth First Search

    Use the expansion strategy of BFS but use the search strategy of DFS
    Always start from the root node (so minimal storage is used, only for path)
    Then apply DFS iteratively for different depths, starting from 1 (best case)
    and going till num_nodes in graph (worst case)
    """
    max_depth = 0
    num_nodes = len(graph)

    # increment search depth till found or not found
    for max_depth in range(1, num_nodes-1):
        if path := dfs(graph, start, goal, max_depth):
            return path

    # no path found
    return []


if __name__ == "__main__":
    graph = {
        "Arad": {
            "Zerind": 75,
            "Timisoara": 118,
            "Sibiu": 140,
        },
        "Zerind": {
            "Arad": 75,
            "Oradea": 71,
        },
        "Timisoara": {
            "Arad": 118,
            "Lugoj": 111,
        },
        "Sibiu": {
            "Arad": 140,
            "Oradea": 151,
            "Fagaras": 99,
            "Rimnicu Vilcea": 80,
        },
        "Oradea": {
            "Zerind": 71,
            "Sibiu": 151,
        },
        "Lugoj": {
            "Timisoara": 111,
            "Mehadia": 70,
        },
        "Fagaras": {
            "Sibiu": 99,
            "Bucharest": 211,
        },
        "Rimnicu Vilcea": {
            "Sibiu": 80,
            "Pitesti": 97,
            "Craiova": 146,
        },
        "Mehadia": {
            "Lugoj": 70,
            "Dobreta": 75,
        },
        "Bucharest": {
            "Fagaras": 211,
            "Pitesti": 101,
            "Giurgiu": 90,
            "Urziceni": 85,
        },
        "Pitesti": {
            "Rimnicu Vilcea": 97,
            "Craiova": 138,
            "Bucharest": 101,
        },
        "Craiova": {
            "Pitesti": 138,
            "Rimnicu Vilcea": 146,
            "Dobreta": 120,
        },
        "Dobreta": {
            "Mehadia": 75,
            "Craiova": 120,
        },
        "Giurgiu": {
            "Bucharest": 90,
        },
        "Urziceni": {
            "Bucharest": 85,
            "Hirsova": 98,
            "Vaslui": 142,
        },
        "Hirsova": {
            "Urziceni": 98,
            "Eforie": 86,
        },
        "Vaslui": {
            "Urziceni": 142,
            "Iasi": 92,
        },
        "Eforie": {
            "Hirsova": 86,
        },
        "Iasi": {
            "Vaslui": 92,
            "Neamt": 87,
        },
        "Neamt": {
            "Iasi": 87
        }
    }
    start = "Arad"
    goal = "Urziceni"

    print("By IDDFS path is...")
    if path := iddfs(graph, start, goal):
        print(path)
    else:
        print("No path found!")
