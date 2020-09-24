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

# A single node of the stack
class StackNode:
    def __init__(self, d):
        self.data = d
        self.next = None


def main():
    stack = Stack(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    # Should continue to return None
    stack.pop()
    stack.toString()


if __name__ == "__main__":
    main()