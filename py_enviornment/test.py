import unittest
from main import BSTNode
#had to make myu own test with copiolet to 
#try and complete assighnment. didnt really follow through
#since i have no defininate right or wrong
class TestBSTNodeDelete(unittest.TestCase):
    def setUp(self):
        self.tree = BSTNode()
        for val in [50, 30, 70, 20, 40, 60, 80]:
            self.tree.insert(val)

    def tree_to_list(self, node):
        if not node:
            return []
        return self.tree_to_list(node.left) + [node.val] + self.tree_to_list(node.right)

    def test_delete_leaf(self):
        self.tree.delete(20)
        self.assertNotIn(20, self.tree_to_list(self.tree))

    def test_delete_node_with_one_child(self):
        self.tree.insert(65)
        self.tree.delete(60)
        self.assertNotIn(60, self.tree_to_list(self.tree))
        self.assertIn(65, self.tree_to_list(self.tree))

    def test_delete_node_with_two_children(self):
        self.tree.delete(30)
        self.assertNotIn(30, self.tree_to_list(self.tree))
        self.assertIn(40, self.tree_to_list(self.tree))  # 40 should replace 30

    def test_delete_root(self):
        self.tree.delete(50)
        self.assertNotIn(50, self.tree_to_list(self.tree))
        self.assertTrue(self.tree.val != 50)

    def test_delete_nonexistent(self):
        original = self.tree_to_list(self.tree)
        self.tree.delete(999)
        self.assertEqual(original, self.tree_to_list(self.tree))

if __name__ == "__main__":
    unittest.main()

    
