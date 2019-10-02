class Node:
    left = None
    right = None
    value = 0
    def __init__(self, value, left=None, right=None, ):
        self.left = left
        self.right = right
        self.value = value

    def push(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.push(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.push(value)
    
    def lvr(self):
        if self.left != None:
            self.left.lvr()
        print(self.value, end=' ')
        if self.right != None:
            self.right.lvr()
    
    def rvl(self):
        if self.right != None:
            self.right.rvl()
        print(self.value, end=' ')
        if self.left != None:
            self.left.rvl()

    def vlr(self):
        print(self.value, end=' ')
        if self.left != None:
            self.left.lvr()
        if self.right != None:
            self.right.lvr()
    def vrl(self):
        print(self.value, end=' ')
        if self.right != None:
            self.right.lvr()
        if self.left != None:
            self.left.lvr()
        
    def lrv(self):
        if self.left != None:
            self.left.lvr()
        if self.right != None:
            self.right.lvr()
        print(self.value, end=' ')

    def rlv(self):
        if self.right != None:
            self.right.lvr()
        if self.left != None:
            self.left.lvr()
        print(self.value, end=' ')
    

values = input("Enter data: ").split(" ")

tree = Node(int(values[0]))
for value in values[1:]:
    tree.push(int(value))
print("\nLVR", end=' -> ')
tree.lvr()
print("\nRVL", end=' -> ')
tree.rvl()
print("\nVLR", end=' -> ')
tree.vlr()
print("\nVRL", end=' -> ')
tree.vrl()
print("\nLRV", end=' -> ')
tree.lrv()
print("\nRLV", end=' -> ')
tree.rlv()