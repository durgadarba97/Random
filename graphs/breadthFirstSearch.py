import sys

'''
The idea is to check all nodes before you proceed.
Not a perfect solution. Pretty crude tbh. 
'''

class Graph:
    def __init__(self, s, g):
        # use a hash map to initialize graph
        self.graph = {}
        self.source = s.replace('\n', '')

        for i in g:
            nodes = i.split(",")
            nodes[0] = nodes[0].replace('\n', '')
            nodes[1] = nodes[1].replace('\n', '')

            if(nodes[0] in self.graph):
                self.graph[nodes[0]].append(nodes[1])
            else:
                self.graph[nodes[0]] = [nodes[1]]

        print(self.graph)

#  use BFS to solve this.
    def bfs(self, root):
        visited = []
        queue = []

        # the queue is a list of depths, 
        depth = 0
        queue.append((root, depth))
        visited.append(root)

        while(queue):
            node = queue.pop(0)

            if(root == self.source):
                print(node[0] + " " + str(node[1]))
            else:
                print(node[0] + " " + "INF")

            if(node[1] > depth):             
                depth += 1

            if(node[0] in self.graph):
                for i in self.graph[node[0]]:
                    if(i not in visited):
                        queue.append((i, depth + 1))
                        visited.append(i)

        return visited

    def getDistance(self):
        v = self.bfs(self.source)
        for i in self.graph:
            if(i not in v):
                v = self.bfs(i)




input = sys.stdin.readlines()
print(input)
g = Graph(input[0], input[1].split(";"))
g.getDistance()



# the input is kinda bullshit and given like this
# A
# A,B;B,C;A,C;B,D;C,D;D,E;F,G;F,H;G,H