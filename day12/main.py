import os

def build_graph(lines):
    neighbours = {}
    edges = [l.split('-') for l in lines]
    for s, e in edges:
        neighbours[s] = neighbours.get(s, []) + [e]
        neighbours[e] = neighbours.get(e, []) + [s]
    return neighbours

def traverse_graph(start, graph, seen):
    if start == 'end':
        return 1
    if start in seen:
        if start == 'start' or start.islower():
            return 0
    return sum(traverse_graph(n, graph, seen | {start}) for n in graph[start])

def traverse_graph_2(start, graph, seen, visit_twice=True):
    if start == 'end':
        return 1
    if start in seen:
        if start == 'start':
            return 0
        if start.islower():
            if not visit_twice:
                return 0
            else:
                visit_twice = False
    return sum(traverse_graph_2(n, graph, seen | {start}, visit_twice) 
    for n in graph[start])


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    input_file = "input.txt"
    input_file_path = os.path.join(script_dir, input_file)
    input_lines = [l.strip() for l in open(input_file_path).readlines()]
    graph = build_graph(input_lines)
    print("day 12a", traverse_graph('start', graph, set()))
    print("day 12b", traverse_graph_2('start', graph, set()))
