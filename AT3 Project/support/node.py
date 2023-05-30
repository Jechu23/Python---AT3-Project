class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    # Insert Node
    def insert(self, data):
        # compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    # print tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, root):
        res = []
        if root:
            res= self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = self.inorderTraversal(root.left)
            res = res + self.inorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res =[]
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    # Findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval) + " not found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval) + " not found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + " is found")


root = Node(40)

root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(51)
root.insert(42)

root.PrintTree()
print(f'In order: {root.inorderTraversal(root)}')
print(f'Pre-Order: {root.PreorderTraversal(root)}')
print(f'Post-Order: {root.PostorderTraversal(root)}')


print(root.findval(447))
print(root.findval(44444))
