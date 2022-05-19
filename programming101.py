class Programming:

    def __init__(self):
        self.arr = [1, 1]
        self.var1 = 1
        self.var2 = "String Juan"

    def fillArr(self, x, y, z):
        self.arr.append(x)
        self.arr.append(y)
        self.arr.append(z)

        for i in self.arr:
            print(i)

    # fill arr from arr.length = 0 to arr.legnth = arrlength
    # 0, 1, 1, 2, 3, 5, 8
    # example: 
    #  fibonacci(5)
    # arr = [1, 1]
    #  arr = [1, 1, 2]
    # arr = [1123]
    # arr = [11235]
    # print(arr)

    def fibonacci(self, arrlength):


        for i in range(len(self.arr), arrlength):
            first = self.arr[len(self.arr) - 2]
            second = self.arr[len(self.arr) - 1]

            current = first + second

            self.arr.append(current)

        print(self.arr)

p = Programming()
# p.fibonacci(5)
print(p.var2[0])