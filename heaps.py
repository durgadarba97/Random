class MinHeap:
    def __init__(self):
        self.heap = []
        

    def insert(self, newnode):
        # step 1 insert new element to end of heap
        self.heap.append(newnode)

        # step 2 bubble up the tree to ensure it's in the right spot.
        childindex = len(self.heap) - 1
        # while the node still has a parent and the parent is greater than the child,
        while(self.hasParent(childindex) and self.heap[self.getParent(childindex)] > self.heap[childindex]):
            # we have to swap the parent node and child node.
            parentindex = self.getParent(childindex)
            tmp = self.heap[childindex]
            self.heap[childindex] = self.heap[parentindex]
            self.heap[parentindex] = tmp
            
            # the child has now become the parent, so update the chlid index.
            childindex = parentindex


    # returns the top element of the array and restructures the heap by "bubbling down"
    def extractMin(self):
        # gets the smallest element and then resets the last to front
        smallest = self.heap[0]
        self.heap[0] = self.heap[len(self.heap)-1]
        self.heap.pop(len(self.heap)-1)

        # bubble down the elements
        # while element has a left child (only case we need check because it for sure wont have a right then)
        index = 0
        while(self.hasLeft(index)):
            # assume the smallest element is the left node
            smallestel = self.getLeft(index)

            # if there is a right node, and that is smaller replace the smallestel
            if(self.hasRight(index) and self.heap[self.getRight(index)] < self.heap[smallestel]):
                smallestel = self.getRight(index)

            # if the smallest element is bigger than the current, then the current is in the right spot and break out. 
            if(self.heap[smallestel] > self.heap[index]):
                break
            
            # swap the current element and the smallest element
            tmp = self.heap[smallestel]
            self.heap[smallestel] = self.heap[index]
            self.heap[index] = tmp

            index = smallestel


        return smallest
    
    # this translates the data structure to be an arraylist. 
    # return the position of the parent element in the array 
    def getParent(self, index):
        return int((index - 2) / 2)

    # return the position of the left element in the array 
    def getLeft(self, index):
        return (index * 2) + 1
    
    # return the position of the right element in the array 
    def getRight(self, index):
        return (index * 2) + 2

    def hasParent(self, index):
        if(self.getParent(index) < 0):
            return False
        else:
            return True

    def hasLeft(self, index):
        if(self.getLeft(index) >= len(self.heap)):
            return False
        else:
            return True

    def hasRight(self, index):
        if(self.getRight(index) >= len(self.heap)):
            return False
        else:
            return True

    def toString(self):
        for i in self.heap:
            print(i)


heap = MinHeap()
heap.insert(10)
heap.insert(15)
heap.insert(20)
heap.insert(17)
heap.insert(25)
heap.toString()
print('\n')
heap.extractMin()
heap.toString()
