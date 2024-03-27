import queue
import time
import networkx as nx
import matplotlib.pyplot as plt

def order_bfs(graph, start_node):
    visited = set()
    q = queue.Queue()
    q.put(start_node)
    order = []

    while not q.empty():
        vertex = q.get()
        if vertex not in visited:
            order.append(vertex)
            visited.add(vertex)
            for node in graph[vertex]:
                if node not in visited:
                    q.put(node)
    return order

def order_dfs(graph, start_node, visited = None):
    if visited is None:
        visited = set()

    order = []

    if start_node not in visited:
        order.append(start_node)
        visited.add(start_node)
        for node in graph[start_node]:
            if node not in visited:
                order.extend(order_dfs(graph, node, visited))
    return order

def visualize_search(order, title, G, pos):
    plt.figure()
    plt.title(title)
    for i, node in enumerate(order, start=1):
        plt.clf()
        plt.title(title)
        nx.draw(G, pos, with_labels=True, node_color=['b' if n == node else 'g' for n in G.nodes])
        plt.draw()
        plt.pause(0.5)
    plt.show()
    time.sleep(0.5)

def generate_connected_random_graph(n, m):
    while True:
        G = nx.gnm_random_graph(n, m)
        if nx.is_connected(G):
            return G

G = generate_connected_random_graph(10, 15)

pos = nx.spring_layout(G)

visualize_search(order_bfs(G, 0), 'BFS Vis', G, pos)
visualize_search(order_dfs(G, 0), 'DFS Vis', G, pos)


