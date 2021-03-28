class Stack:
    # implement pop
    # implement push
    # implement peek
    # implement isEmpty
    def __init__(self, d):
        self.top = StackNode(d)

    # pops the top of the stack 
    def pop(self):
        if(self.top == None):
            return None
        else:
            item = self.top
            self.top = self.top.next
            return item

    # add a new node to the top of the stack
    def push(self, d):
        temptop = self.top
        self.top = StackNode(d)
        self.top.next = temptop

    # peek the top of the stack without deleting
    def peek(self):
        return self.top.data

    def toString(self):
        if(self.top == None):
            print(None)
        else:
            print(self.top.data)

class SetofStacks:
    def __init__(self, size, start):
        # max size of each stack
        self.maxlen = size

        # Essentially, making a list of stacks.
        self.current = StackNode(start)
        self.stackset = []
        self.stackset.append(self.current)
        self.currentlen = 1

    def push(self, data):
        # if we don't need anoter stack of plates, push it to this stack
        if(self.currentlen < self.maxlen):
            self.current.next = StackNode(data)
            self.current = self.current.next
            self.currentlen += 1
        else:
            # if not, start a new stack.
            self.current.next = None
            self.current = StackNode(data)
            self.stackset.append(self.current)
            self.currentlen = 1
    
    def toString(self):
        for i in self.stackset:
            j = i
            while(j is not None):
                print(j.data)
                j = j.next

            print("hello")
        

# A single node of the stack
class StackNode:
    def __init__(self, d):
        self.data = d
        self.next = None


def main():
    # stack = Stack(0)
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # # Should continue to return None
    # stack.pop()
    # stack.toString()

    setofstacks = SetofStacks(3, 0)
    setofstacks.push(1)
    setofstacks.push(2)
    setofstacks.push(3)
    setofstacks.push(4)
    setofstacks.push(5)
    setofstacks.toString()


if __name__ == "__main__":
    main()