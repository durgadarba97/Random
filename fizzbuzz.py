# honestly not the best way to do this, but this is an answer ig.
for i in range(1, 100):
    char = ""

    if(i % 3 == 0):
        char = char + "fizz"
    if(i % 5 == 0):
        char = char + "buzz"

    if(char == ""):
        print(i)
    else:
        print(char)