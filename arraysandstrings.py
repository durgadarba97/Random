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



print(countAndSay('aaabbbccc'))