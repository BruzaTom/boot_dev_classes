class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

#test was missing module so had to write prints just to see
#lesson 5

    def insert(self, val):
        if self.val == None:
            self.val = val
        elif self.val == val:
            return
        elif val < self.val:
            if self.left == None:
                self.left = BSTNode(val)
                print(f"self.left = BSTNode({val})")
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right == None:
                self.right = BSTNode(val)
                print(f"self.right = BSTNode({val})")
            else:
                self.right.insert(val)
