from collections import defaultdict

from aocd import get_data
from aocd.post import submit
from graphviz import Digraph

nodes_to_skip = {
    'jxd': 'bbz',
    'glz': 'mxd',
    'clb': 'brd',
}


def main():
    data = get_data(day=25).split('\n')
    # data = open('test').read().split('\n')

    dot = Digraph(engine='sfdp')
    edges = {}

    for line in data:
        parts = line.split(' ')
        main_node = parts[0][:-1]
        nodes = parts[1:]
        # dot.node(main_node, main_node)
        if main_node not in edges:
            edges[main_node] = []

        for node in nodes:
            if main_node in nodes_to_skip:
                if nodes_to_skip[main_node] == node:
                    continue

            if node in nodes_to_skip:
                if nodes_to_skip[node] == main_node:
                    continue

            edges[main_node].append(node)
            if node not in edges:
                edges[node] = []
            edges[node].append(main_node)
            # dot.node(node, node)
            # dot.edge(main_node, node)

    # print(dot.source)
    # Render the graph into a PNG file
    # dot.render('round-table.gv', cleanup=True)
    start = ['bbz']
    temp = []
    nodes_in_graph = [start[0]]
    while start:
        for start_node in start:
            for node in edges[start_node]:
                if node not in nodes_in_graph:
                    temp.append(node)
                nodes_in_graph.append(node)

        start = temp.copy()
        temp = []

    answer = len(list(set(nodes_in_graph)))

    start = ['jxd']
    temp = []
    nodes_in_graph = [start[0]]
    while start:
        for start_node in start:
            for node in edges[start_node]:
                if node not in nodes_in_graph:
                    temp.append(node)
                nodes_in_graph.append(node)

        start = temp.copy()
        temp = []

    answer *= len(list(set(nodes_in_graph)))
    print(answer)
    submit(answer)


if __name__ == '__main__':
    main()
