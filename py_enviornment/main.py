class BSTNode:
    def height(self):
        left, right = 0, 0
        if self.val == None:
            return 0
        if self.left:
            left = self.left.height()
        if self.right:
            right = self.right.height()
        return max(left, right) + 1


    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

