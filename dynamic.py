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

    

    print(memo[m-1][n-1])

uniquePaths(3, 3)
# letterCombinations('23')
# print(tripleStep(4, []))
