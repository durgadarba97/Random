# class to set up the tree
class Tree:
    def __init__(self, r = None):
        # list of entities in the tree
        # self.entities = objs
        self.root = r
        # self.root = self.initializeTree()

    # insert new node into tree.
    # Return self so that I can just keep it going.
    def insertIterative(self, newnode):

        if(self.root == None):
            self.root = newnode
            return self.root

        # Here you use the current node as peek into the child.
        # Parent keeps track of the parent
        current = self.root
        parent = None

        # iterate through the tree by using the current node as look ahead.
        # if the current node is null, use the parent to set the newnode.
        while(current != None):

            # After every iteration, we've failed to find an empty node so set parent to current node.
            parent = current

            # Then, peek into the children.
            if(newnode.name <= current.name):
                current = current.left
            else:
                current = current.right

        # We know the parent node of the child. 
        # Set the child to lef tor right based on this.
        if(parent.name <= newnode.name):
            parent.right = newnode
        else:
            parent.left = newnode
        return self.root

    # find the max depth of the binary tree
    def maxDepth(self, root):

        # if the root node is empty, return 0
        if(root == None):
            return 0
        else:
            # if not, find the max depth of left and right sub tree
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            # return the max of the left and right + 1.
            return max(left, right) + 1
        
        # Essentially, it goes all the way to the bottom and return 0,
        # then adds one all the way up the tree.


        
    def preOrderTraversal(self, node):
        # preorder traversal is visting current node before its children left to right.
        if(node != None):
            self.visit(node)
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        # visit children nodes left to right before the parent.
        if(node != None):
            self.preOrderTraversal(node.left)
            self.preOrderTraversal(node.right)
            self.visit(node)
    
    def inOrderTraversal(self, node):
        #  visit left node, root node, then parent node.
        if(node != None):
            self.preOrderTraversal(node.left)
            self.visit(node)
            self.preOrderTraversal(node.right)

    def visit(self, node):
        print(node.name)

class Node:
    def __init__(self, n, l = None, r = None):
        self.name = n
        self.left = l
        self.right = r



def main():
    nodes = [0, -1, 1, 0.5, 3, 2, 4, 6]
    # tree = Tree(nodes)
    # root = Node(0, Node(1), Node(2))
    # tree = Tree(root)
    # tree.insertIterative(Node(3))
    # tree.preOrderTraversal(tree.root)

    tree = Tree()
    for i in nodes:
        root = tree.insertIterative(Node(i))

    tree.preOrderTraversal(root)
    print(tree.maxDepth(root))

    

if __name__ == "__main__":
    main()