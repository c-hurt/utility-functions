from collections import defaultdict
from collections import namedtuple

Edge = namedtuple('Edge', 'dest weight')
vertices = defaultdict(list)

vertices['a'].append(Edge(dest=10, weight=100))
vertices['a'].append(Edge(dest=12, weight=200))

print(vertices)

for vertex in vertices:
    for edge in vertices[vertex]:
        print(edge.dest)