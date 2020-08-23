from heapq import heappush, heappop


def ucs(graph, start, goal):
    """Uniform Cost Search

    A variant of Djikstra's algorithm for large graphs.
    Starting from the start node, we assign it initial weight infinity.
    We then choose the neighbor with the lowest weight, or a previously queued
    node's path if its total weight is lesser than current path.
    A priority queue is used to store only the visited nodes (unlike Djikstra's
    algorithm which stored all the nodes).
    """

    # priority queue: (least_total_cost, curr_node, prev_node)
    pqueue = [(0, start, None)]

    # curr_node: prev_node
    visited = {}

    while pqueue:
        tcost, node, prev = heappop(pqueue)

        # BUG: we are not updating old values in pqueue, but just pushing new
        #      values in... so until goal found, if the old value is poped
        #      then visited's prev node is overwritten with costlier node
        if node not in visited:
            visited[node] = prev

        if node == goal:
            path = []

            # backtrack using the stored prev nodes
            while node:
                path.append(node)
                node = visited[node]

            # the path is from goal to start, so reverse it
            return list(reversed(path))

        # add all the neighbors of current node to pqueue
        for neigh, weight in graph[node].items():
            if neigh not in visited:
                # BUG: push only if neigh not in pqueue
                #      otherwise only update the weight and prev
                heappush(pqueue, (weight + tcost, neigh, node))

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

    print("By UCS path is...")
    if path := ucs(graph, start, goal):
        print(path)
    else:
        print("No path found!")
