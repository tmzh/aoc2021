from main import build_graph, traverse_graph_2, traverse_graph


sample_input = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()

neighbours = {}

def test_get_all_paths():
    graph = build_graph(sample_input)
    assert 10 ==  traverse_graph('start', graph, set())
    assert 36 ==  traverse_graph_2('start', graph, set(), True)