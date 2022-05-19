
# A child is running up a staircase with n steps and hop either 1, 2, or 3 steps at a time. 
# implement a method to count how many ways the child can go up the stairs
# solve using dynamic programming and memoization. trying the bottom up approach
def tripleStep(i, memo):
    # to climb 0 stairs, there's 1 way to do this.
    memo.append(0)
    # there's also only 1 way to climb 1 stair and 2 ways climb 2 stairs
    memo.append(1)
    memo.append(2)

    for stair in range(3, i+1):
        memo.append(memo[stair - 1] + memo[stair - 2] + memo[stair - 3])

    return memo[i]


# a robot can only move left or down in the 2d array from 0,0 to m,n
#  how many unique are there if the robot starts at 0,0. 
def uniquePaths(m, n):
    # we can solve this using dynamic programming and memoization. 
    memo = []

    # initialize memoization table. 
    # Where each value represents how many ways there are to get to each cell
    for i in range(m):
        memo.append([])
        for _ in range(n):
            memo[i].append(1)
    
    # calculate the number of ways to get to each cell. 
    #  memo[i, j] = memo[i+1, j] + memo[i, j+1] + memo[i,j]
    for i in range(1, m):
        for j in range(1, n):
            # if(i+1 < len(memo) and j+1 < len(memo[i])):
            memo[i][j] = memo[i-1][j] + memo[i][j-1]
            # if(i+1 < len(memo)):
            #     memo[i][j] = memo[i][j] + memo[i+1][j]
            # if(j+1 < len(memo[i])):
            #     memo[i][j] = memo[i][j] + memo[i][j+1]

# uniquePaths(3, 3)
# letterCombinations('23')
# print(tripleStep(4, []))

# djikstra's algorithm
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1, 'E': 4},
    'C': {'A': 1, 'B': 2, 'D': 8, 'F': 2},
    'D': {'B': 1, 'C': 8, 'E': 7, 'F': 6, 'G': 4},
    'E': {'B': 4, 'D': 7, 'G': 6},
    'F': {'C': 2, 'D': 6, 'G': 5, 'H': 4, 'I': 2},
    'G': {'D': 4, 'E': 6, 'F': 5, 'H': 3, 'I': 9},
    'H': {'F': 4, 'G': 3, 'I': 8},
    'I': {'F': 2, 'G': 9, 'H': 8}
}

def djikstra(graph, start, end):
    # keep track of all nodes that have been visited
    visited = []
    # keep track of all nodes that have been visited
    unvisited = graph.keys()
    # keep track of the distances from the start node to each node
    distances = {}
    # keep track of the previous node
    previous = {}
    # set the distance from the start node to itself to 0
    distances[start] = 0
    # while there are still nodes to visit
    while len(unvisited) > 0:
        # find the node with the lowest distance
        current = None
        for node in unvisited:
            if current is None:
                current = node
            elif distances[node] < distances[current]:
                current = node
        # if the distance is infinite, there is no path
        if distances[current] == float('inf'):
            return None
        # add the current node to the visited nodes
        visited.append(current)
        # remove the current node from the unvisited nodes
        unvisited.remove(current)
        # for each child node, calculate the distance from the start node to the child node
        for child in graph[current].keys():
            # if the child node has not been visited
            if child not in visited:
                # calculate the distance from the start node to the child node
                distance = distances[current] + graph[current][child]
                # if the distance is less than the current distance, update the distance
                if child not in distances or distance < distances[child]:
                    distances[child] = distance
                    # set the previous node to the current node
                    previous[child] = current
    # return the distances and previous nodes
    return distances, previous


# compute the levenshtein distance between two strings
# the levenshtein distance is the number of edits needed to transform one string into the other
# 
def levenshtein(s1, s2):
    # if one of the strings is empty, return the length of the other string
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    # create a matrix of the same size as the two strings
    matrix = []
    # for every letter in s1, add a row to the matrix
    
    for i in range(len(s1) + 1):
        matrix.append([0] * (len(s2) + 1))


    # initialize the memoization table
    for i in range(len(matrix)):
        matrix[i][0] = i
    for j in range(len(matrix[0])):
        matrix[0][j] = j

    # for each row in the matrix 
    for i in range(1, len(matrix)):

        for j in range(1, len(matrix[0])):
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j-1] + 1, # replacement
                                matrix[i-1][j] + 1, # insertion
                                matrix[i][j-1] + 1) # deletion
    # return the bottom right corner of the matrix
    return matrix[len(s1)][len(s2)]

# recursive levenshien distance
def recursive_levenshtein(s1, s2):
    # if one of the strings is empty, return the length of the other string
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    # if the first characters of the strings match, recursively call the function on the remaining strings
    if s1[0] == s2[0]:
        return recursive_levenshtein(s1[1:], s2[1:]) #  recursive ( itten, itting)
    # otherwise, return the minimum of the three distances
    return min(recursive_levenshtein(s1[1:], s2) + 1, # deletion
                recursive_levenshtein(s1, s2[1:]) + 1, # insertion
                recursive_levenshtein(s1[1:], s2[1:]) + 1) # replacement

# should return 3
print(recursive_levenshtein('back', 'backbite'))

#     ''  k   i   t   t   e   n  
# ''  0   1   2   3   4   5   6
# s   1   1   2   3   4   5   6
# i   2   2   1   2   3   4   5
# t   3   3   2   1   2   3   4 
# t   4   4   3   2   1   2   3
# i   5   5   3   4   3   2   3    
# n   6   5   4   5   4   3   2
# g   7   5   6   5   5   4   3

# we calculate the distance between two strings at every step
    # in the first row, we calculate the distance between string '' and 'kitten'
        # therefore, doing operation '' - 'k', '' - 'ki', '' - 'kit', '' - 'kitt', '' - 'kitten' would be an insertion.
        #  we are inserting to '' to get 'kitten' and that would take 6 insertions

    #  similaralily, for the first column, we calculate the distance between string '' and 'sitting'
        # therefore, doing the operation 's' - '', 'si' - '', 'sit' - '', 'sitt' - '', 'sitting' - '' would be a deletion.
        #  we are inserting to 'sitting' to get '' and that would take 7 deletions

    #  finally, to do a replacement, 
        # we have to do a deletion and an insertion which is why we look we look at the s1[:i], s2[:j]

