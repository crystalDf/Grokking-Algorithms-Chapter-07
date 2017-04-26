from prettytable import PrettyTable

infinity = float("inf")


def find_lowest_cost_node(costs):

    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]

        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijkstra_algorithm(graph, costs, parents, processed):

    while True:
        node = find_lowest_cost_node(costs)

        if node is None:
            break

        node_cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():

            new_neighbor_cost = node_cost + neighbors[n]

            if new_neighbor_cost < costs[n]:
                costs[n] = new_neighbor_cost
                parents[n] = node

        processed.append(node)


def format_print_costs(costs):

    headers = ['Node', 'Value']
    table = PrettyTable(headers)

    for node in costs:
        row = [node, costs[node]]
        table.add_row(row)

    print(table)


def format_print_parents(parents):
    headers = ['Node', 'Parent']
    table = PrettyTable(headers)

    for node in parents:
        row = [node, parents[node]]
        table.add_row(row)

    print(table)

graph = dict()

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

dijkstra_algorithm(graph, costs, parents, processed)

format_print_costs(costs)
format_print_parents(parents)

# A.
print("Solution A:")

graph = dict()

graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["fin"] = 3
graph["c"]["d"] = 6

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}

costs = dict()
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["d"] = None
parents["fin"] = None

processed = []

dijkstra_algorithm(graph, costs, parents, processed)

format_print_costs(costs)
format_print_parents(parents)

# B.
print("Solution B:")

graph = dict()

graph["start"] = {}
graph["start"]["a"] = 10

graph["a"] = {}
graph["a"]["b"] = 20

graph["b"] = {}
graph["b"]["c"] = 1
graph["b"]["fin"] = 30

graph["c"] = {}
graph["c"]["b"] = 1

graph["fin"] = {}

costs = dict()
costs["a"] = 10
costs["b"] = infinity
costs["c"] = infinity
costs["fin"] = infinity

parents = dict()
parents["a"] = "start"
parents["b"] = None
parents["c"] = None
parents["fin"] = None

processed = []

dijkstra_algorithm(graph, costs, parents, processed)

format_print_costs(costs)
format_print_parents(parents)

# C.
print("Solution C:")

graph = dict()

graph["start"] = {}
graph["start"]["a"] = 2
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 2
graph["a"]["c"] = 2

graph["b"] = {}
graph["b"]["a"] = 2

graph["c"] = {}
graph["c"]["fin"] = 2
graph["c"]["b"] = -1

graph["fin"] = {}

costs = dict()
costs["a"] = 2
costs["b"] = 2
costs["c"] = infinity
costs["fin"] = infinity

parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["c"] = None
parents["fin"] = None

processed = []

dijkstra_algorithm(graph, costs, parents, processed)

format_print_costs(costs)
format_print_parents(parents)
