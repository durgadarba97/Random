# implement an algorithms to determinee if a string has all unique characters. 
def isUnique(str):
    unique = []
    for i in str:
        # This works as a solution but uses an unecessary data structure. 
        # if(i in unique):
        #     return False
        # else:
        #     unique.append(i)
        if(str.count(i) > 1):
            return False
        
    return True

# aaabbbccc should return 3a3b3c
def countAndSay(inputstr):
    retstring = ""
    currentrun = inputstr[0]
    count = 1
    # Go through the length of string
    for i in range(1, len(inputstr)):
        # for every character check to see if its the same character as before
        if(inputstr[i] != currentrun):
            # if not, we found a new character, start the count over again, add the count and say to the return string
            retstring = retstring + str(count) + currentrun
            currentrun = inputstr[i]
            count = 1
        else:
            # if not, add to the count. 
            count += 1

    # return the return string
    return retstring

# Given an image, represented by and NxN matrix where each pixel in the image is represented by an integer, 
# write and method to rotate the image by 90 deg. 
# Can you do this in place?
def rotateMatrix(matrix):

    # iterate through matrix and switch row and col
    for row in range(len(matrix)):
        for col in range(row, len(matrix)):
            print(str(row) + " " + str(col))
            # print(type(matrix[col][row]))
            # swtich [row][col] value to [col][row]
            # tmp = matrix[row][col]
            # matrix[row][col] = matrix[col][row]
            # matrix[col][row] = tmp
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in range(len(matrix)):
        # iterate only half of the row.
        for col in range(0, int(len(matrix)/2)):
            # take the element at row, col replace with element at row, len(matrix[row])-col-1
            tmp = matrix[row][col]
            matrix[row][col] = matrix[row][len(matrix)-col-1]
            matrix[row][len(matrix)-col-1] = tmp
    print(matrix)



# the basic idea of binary search is that we half the elements until we
# find the one we're looking for.
def binarySearch(arr, lookingfor):

    low = 0
    high = len(arr)-1
    mid = (low + high) // 2

    while(low <= high):
        if(arr[mid] < lookingfor):
            low = mid + 1
        elif(arr[mid] > lookingfor):
            high = mid - 1
        else:
            return arr[mid]

        mid = (low + high) // 2
    return None

print(binarySearch([1,2,3,4,5,6], 2))
# oneAway("pale", "lape") 

    # if the differences between the strings is greater than 1, then return false.

    
    
    

# matrix = [[0,1],
#             [2, 3]]
# matrix =[
#         [1, 2,  3,   4],
#         [5, 6,  7,   8],
#         [9, 10, 11, 12],
#         [13, 14, 15, 16]]
# matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]
# rotateMatrix(matrix)


# print(countAndSay('aaabbbccc'))

# def letterCombinations(digits):
#     if(not digits):
#         return []

#     phone = {
#                 '2' : ['a', 'b', 'c'],
#                 '3' : ['d','e', 'f'],
#                 '4' : ['g', 'h', 'i'],
#                 '5' : ['j', 'k', 'l'],
#                 '6' : ['m', 'n', 'o'],
#                 '7' : ['p', 'q', 'r', 's'],
#                 '8' : ['t', 'u', 'v'],
#                 '9' : ['w', 'x', 'y', 'z']
#             }

