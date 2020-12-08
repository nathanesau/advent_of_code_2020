from functools import reduce
import operator


def build_graph(data):
    graph = {}
    data = data.replace(".", "")
    data = data.replace("bags", "bag")
    data.replace("bag", "")
    for line in data.splitlines():
        line = line.strip()
        if line:
            tmp_vertex, tmp_neighbors = line.split("contain")
            # parse vertex
            vertex = tmp_vertex.strip()
            # parse neighbors
            if "no other bag" in tmp_neighbors:
                neighbors = []
            else:
                neighbors = []
                for neighbor in tmp_neighbors.split(","):
                    neighbor = neighbor.strip()
                    words = neighbor.split(' ')
                    weight = words[0].strip()
                    value = ' '.join(words[1:]).strip()
                    neighbors.append({"weight": weight, "value": value})
            graph[vertex] = neighbors
    return graph


def reversed_graph(graph):
    """
    return reversed graph
    """
    rgraph = dict((k, []) for k in graph.keys())
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            nvalue = neighbor["value"]
            nweight = neighbor["weight"]
            rgraph[nvalue].append({"weight": nweight, "value": vertex})
    return rgraph


def bfs_return_visited(graph, src):
    """
    traverse entire graph, don't search for dest
    """
    visited = {src}
    q = [src]
    while q:
        it = q.pop(0)
        for neighbor in graph[it]:
            if neighbor["value"] not in visited:
                visited.add(neighbor["value"])
                q.append(neighbor["value"])
    return visited


def bfs_return_child_count(graph, src):
    child_count = 0
    q = [{"value": src, "weight": 1}]
    while q:
        it = q.pop(0)
        itvalue = it["value"]
        itweight = it["weight"]
        for neighbor in graph[itvalue]:
            nvalue = neighbor["value"]
            nweight = int(neighbor["weight"])
            child_count += itweight * nweight
            q.append({"value": nvalue, "weight": itweight * nweight})
        # NOTE: children will be added to queue once for each of their parents
    return child_count


def solution_1(data):
    graph = build_graph(data)
    rgraph = reversed_graph(graph)
    visited = bfs_return_visited(rgraph, "shiny gold bag")
    return len(visited) - 1


def solution_2(data):
    graph = build_graph(data)
    child_count = bfs_return_child_count(graph, "shiny gold bag")
    return child_count
