# Reading a constraint table presented in a .txt file and storing it in memory

# graph = {
#     vertex1: {
#         'predecessors': [predecessor1, predecessor2, ...],
#         'successors': [(successor1, weight1), (successor2, weight2), ...],
#         'rank': rank_of_vertex1
#     },
def create_dict(file_path):
    graph = {}
    # We initiate the 0 index to be the source vertex
    graph[0] = {'predecessors': [], 'successors': [], 'duration': 0, 'rank': 0}
    constraints = []
    n = 0

    with open(file_path, 'r') as file:
        for line in file:
            n = n + 1
            line = line.split(' ')
            # remove \n from the last element
            line[-1] = line[-1].strip()
            # convert the elements to integers
            line = list(map(int, line))
            # the first element is the vertex
            vertex = line[0]
            # the second element is its duration
            duration = line[1]
            # the other are their constraints
            constraints.append(line[2:])
            # add the vertex to the graph
            graph[vertex] = {'predecessors': [], 'successors': [], 'duration': duration, 'rank': -1}
            print(line)

    # add omega (n+1) vertex to the graph
    graph[n+1] = {'predecessors': [], 'successors': [], 'duration': 0, 'rank': -1}

    print(constraints)
    # add the constraints to the graph
    n = 0
    for constraint in constraints:
        n = n + 1
        if len(constraint) == 0:
            graph[0]['successors'].append(n)
            graph[n]['predecessors'].append(0)

        else:
            for c in constraint:
                graph[c]['successors'].append(n)
                graph[n]['predecessors'].append(c)

    # add omega to vertices with no successors except itself
    for vertex in graph:
        if len(graph[vertex]['successors']) == 0:
            graph[vertex]['successors'].append(n+1)
            graph[n+1]['predecessors'].append(vertex)

    graph[n+1]['successors'] = []

    return graph

def print_graph(graph):
    for vertex in graph:
        print(f"Vertex {vertex}:")
        print(f"Predecessors: {graph[vertex]['predecessors']}")
        print(f"Successors: {graph[vertex]['successors']}")
        print(f"Duration: {graph[vertex]['duration']}")
        print(f"Rank: {graph[vertex]['rank']}")
        print()

def print_vertices(graph):
    # Print number of vertices and edges
    # Print all vertices like this: vertice1 -> vertice2 = duration
    # example : 0 -> 1 = 5
    for vertex in graph:
        for successor in graph[vertex]['successors']:
            print(f"{vertex} -> {successor} = {graph[vertex]['duration']}")

def value_matrix(graph):
    # Create and display the value matrix of the graph
    # The value matrix is a matrix where each element is the duration of the edge between the two vertices
    # If there is no edge, the duration is *
    # The matrix is displayed in a table format
    n = len(graph)
    print("",end='   ')
    for vertex in graph:
        print(vertex,end='  ')
    matrix = [['*' for i in range(n)] for j in range(n)]
    for vertex in graph:
        for successor in graph[vertex]['successors']:
            matrix[vertex][successor] = graph[vertex]['duration']

    for i in range(n):
        print()
        print(i,end='  ')
        for j in range(n):
            print(matrix[i][j],end='  ')

    print()



