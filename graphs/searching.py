class Graph:
    def __init__(self):
        self.nodes = []

    def dfs(self, root, visited = None):
        if(root is None):
            return 
        else:
            self.visit(root)
            if(visited == None):
                visited = []
            visited.append(root)

            for i in root.children:
                if(not i in visited):
                    self.dfs(i, visited)

    def interativedfs(self):
        pass

    def listToGraph(self, routes):
        graph = {}

        for i in connections:
            graph[i[0]] = i[1 : len(i)]
        return graph

    # returns the number of edges to reverse to make it so that all nodes go to 0.
    # n is the number of edges. connections is a List of a List
    def allNodesLeadToZero(self, n, connections):
        # turn list of list into adjcency list
        graph = self.listToGraph(connections)
        print(graph, graph[0])

    def search(self, graph, root, visited=None):
        # we want to visit the child node
        if(root == None): return 0

        self.visit(root)
        visited.append(root)
        for i in graph[root]:
            if(i not in visited):
                self.search(graph, i, visited)




    def visit(self, node):
        print(node.name)


class Node:
    def __init__(self, name, children = None):
        self.name = name
        self.children = children

connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
graph = Graph()
graph.allNodesLeadToZero(6, connections)


# n0 = Node(0)
# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)

# n0.children = [n0, n1]
# n1.children = [n1, n3]
# n2.children = [n2, n3]
# n3.children = [n4, n0]
# n4.children = [n4, n5]
# # n5.children = []

# graph = Graph([n0, n1, n2, n3, n4])
# graph.dfs(n0)


# I implemented this using dynamic programming. Going try using dfs/recursion.
# def uniquePaths(m , n):
#     # starting from m and n, it'll go to 0,0.
#     # the recursion will break when m <= 1 or  n<=1
#     if(m <= 1 or n <= 1):
#         # there's only 1 way we can get to these position.
#         return 1
#     else:
#         return uniquePaths(m-1, n) + uniquePaths(m, n-1)

# print(uniquePaths(3, 3))