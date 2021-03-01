
class Node:
    def __init__(self, d = None):
        # linked list list needs at least a head node.
        self.data = d
        self.next = None

    # appends a node to the list. 
    def appendtotail(self, d):
        end = Node(d)
        current = self
        while(current.next is not None):
            current = current.next
        current.next = end
    
    # deletes a node in the list. If there's a duplicate, get the first instance of node. 
    def delete(self, d):
        current = self
        # if the node to be deleted is the first node, you don't need to set a previous
        if(d == current.data):
            self.data = current.next.data
            self.next = current.next.next
            return True
        else:
            # connect the previous node to the nest node.
            prev = current
            current = current.next
            while(current is not None):
                if(current.data == d):
                    prev.next = current.next
                    return True
                else:
                    prev = current
                    current = current.next
            return False

    # Learned about the runner technique. I can use this in many ways.
    # Here, use it as a look ahead by incrementing the slow runner ever 2.
    def deleteMiddleElement(self):
        fast = self
        slow = fast
        i = 0
        while(fast.next != None):
            i +=1
            fast = fast.next
            
            # we want the one before it
            if((i%2)+1 == 0):
                slow = slow.next

        # I could just use the delete method, but I already have the placement of the node so running through the list again is unecessary.
        # Take the slow element and set the next value to the value after the next one.
        slow.next = slow.next.next
        return slow.next.data

    # returns the kth from.
    # this works the same as delete middle node. 
    def kthFromLast(self, k):
        fast = self
        slow = fast
        i = 0
        while(fast.next != None):
            fast = fast.next
            # every kth element iterate the slow node by 1. 
            # by the end you will have the kth from the end. 
            if((i%k) == 0):
                slow = slow.next
            
            i+=1

        if((i%k) == 0):
            slow = slow.next
        return slow


    # iterates the list and removes duplicates
    def removeDuplictes(self):
        current = self
        duplicatetable = {}
        duplicatetable[current.data] = 1
        current = current.next

        while(current is not None):
            # Doing it like this allows you to allow for a cretain number of duplicates
            if(current.data in duplicatetable):
                self.delete(current.data)
            else:
                duplicatetable[current.data] = 1
            current = current.next

    # resursively reverses the linked list. 
    # 1 -> 2 -> 3 
    # 3 -> 2 -> 1
    def iterativeReverse(self):
        # set a temporary previous value
        previous = None
        current = self
        # stop iterating when reaches the length of the list.
        while(current != None):
            # a temp variable is used to keep track of the next element.
            n = current.next
            # Set current node's next to the previous node
            current.next = previous
            # Set the previous node to the current node and iterate current to next node with the temp variable.
            previous = current
            current = n

        
        self = previous
        return self



    
            



    
    def toString(self):
        current = self
        while(current.next is not None):
            print(current.data)
            current = current.next
        print(current.data)

        


def main():
    link = Node(0)
    link.appendtotail(1)
    link.appendtotail(2)
    # link.appendtotail(2)
    link.appendtotail(3)
    link.appendtotail(4)
    link.appendtotail(5)
    link.appendtotail(6)
    # link.appendtotail(7)
    # link.appendtotail(3)
    # link.appendtotail(3)
    
    # link.removeDuplictes()
    # link.push(4)
    # link.toString()
    link = link.iterativeReverse()
    print("reversed:")
    link.toString()
    # link.toString()
    # should return 2
    # middle = link.deleteMiddleElement()
    # print(middle)
    # kth = link.kthFromLast(2)
    # print(kth.data)
    # link.toString()

    
    

if __name__ == "__main__":
    main()