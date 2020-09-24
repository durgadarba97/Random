
class Node:
    def __init__(self, d):
        # linked list list needs at least a head node.
        self.data = d
        self.next = None

    def appendtotail(self, d):
        end = Node(d)
        current = self
        while(current.next is not None):
            current = current.next
        current.next = end
    
    def delete(self, d):
        current = self
        if(d == current.data):
            self.data = current.next.data
            self.next = current.next.next
            return True
        else:
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
    link.appendtotail(2)
    link.appendtotail(3)
    link.appendtotail(3)
    link.appendtotail(3)
    
    link.toString()
    link.delete(0)
    link.removeDuplictes()
    print("deleted:")
    link.toString()

if __name__ == "__main__":
    main()