# Day 7

1. Find number of bags which can contain "shiny gold" bag.

2. Find number of bags inside "shiny gold" bag.

https://csacademy.com/app/graph_editor/

Graph:

```
light_red
bright_white
muted_yellow
dark_orange
shiny_gold
faded_blue
dark_olive
vibrant_plum
dotted_black
light_red bright_white
light_red muted_yellow
dark_orange bright_white
dark_orange muted_yellow
bright_white shiny_gold
muted_yellow shiny_gold
muted_yellow faded_blue
shiny_gold dark_olive
shiny_gold vibrant_plum
dark_olive faded_blue
dark_olive dotted_black
vibrant_plum faded_blue
vibrant_plum dotted_black
```

Reversed Graph:

```
light_red
bright_white
muted_yellow
dark_orange
shiny_gold
faded_blue
dark_olive
vibrant_plum
dotted_black
bright_white light_red
muted_yellow light_red
bright_white dark_orange
muted_yellow dark_orange
shiny_gold bright_white
shiny_gold muted_yellow
faded_blue muted_yellow
dark_olive shiny_gold
vibrant_plum shiny_gold
faded_blue dark_olive
dotted_black dark_olive
faded_blue vibrant_plum
dotted_black vibrant_plum
```

Talking points (1):
* show reversed graph
* explain how to find all bags contain "shiny gold" using reversed graph
* implement code

Talking points (2):
* show graph
* explain how "shiny gold" has 2 vibrant plum, 1 dark olive
* add vibrant plum (1 X 2) to queue, add dark olive (1 X 1) to queue
* explain how "vibrant plum" has 5 faded blue, 6 dotted black
* add faded blue (1 X 2 X 5) to queue, add dotted black (1 X 2 X 6) to queue
* explain how "dark olive" has 3 faded blue, 4 dotted black
* add faded blue (1 X 1 X 3) to queue, add dotted black (1 X 1 X 4) to queue
* totals = 2 + 1 + 10 + 12 + 3 + 4 = 32

```python
# ex. data = """light red bag contain 1 bright white bag, 2 muted yellow bag.
#               dark orange bag contain 3 bright white bag, 4 muted yellow bag.
#               bright white bag contain 1 shiny gold bag."""
def build_graph(data):
    graph = {}
    data = data.replace(".", "")
    data = data.replace("bags", "bag")
    for line in data.splitlines():
        line = line.strip()
        if line:
            tmp_vertex, tmp_neighbors = line.split("contain")
            vertex = tmp_vertex.strip()
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
    rgraph = dict((k, []) for k in graph.keys())
    for vertex, neighbors in graph.items():
        for neight in neighbors:
            nvalue = neighbor["value"]
            nweight = neighbor["weight"]
            rgraph[nvalue].append({"value": vertex, "weight": nweight})
    return rgraph


def bfs_return_visited(graph, src):
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
    # no visited
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
        # NOTE: children will be added to queue once for each parent
    return child_count
    

def solution_1(graph):  # graph is reversed graph
    graph = build_graph(data)
    rgraph = reversed_graph(graph)
    visited = bfs_return_visited(graph, "shiny gold bag")
    return len(visited) - 1


def solution_2(graph):
    graph = build_graph(data)
    child_count = bfs_return_child_count(graph, "shiny gold bag")
    return child_count
```
