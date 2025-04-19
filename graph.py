# хеш-таблица графов
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["end"] = 1
graph["b"] = {}
graph["b"]["end"] = 5
graph["b"]["a"] = 3
graph['end'] = {}

#хеш-таблица стоймости
infinity = float('inf')
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

# хеш-таблица родителей
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None
# обработчик узлов
processed = []


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra(graph, costs, parents, processed):

    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]


        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]

            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node

        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    return costs, parents

costs, parents = dijkstra(graph, costs, parents, processed)

# Вывод результатов
print("Кратчайшие расстояния от узла 'start':")
for node, cost in costs.items():
    print(f"До {node}: {cost}")

print("\nРодители для восстановления пути:")
for node, parent in parents.items():
    print(f"{node}: {parent}")

# Восстановление пути до 'end'
def find_path(parents, end):
    path = [end]
    current = end
    while current in parents and parents[current] is not None:
        current = parents[current]
        path.append(current)
    return path[::-1]  # Разворачиваем путь

print("\nКратчайший путь до 'end':")
path = find_path(parents, "end")
print(" -> ".join(path))
