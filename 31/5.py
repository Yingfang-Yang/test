class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        """翻转二叉树"""
        return None if not root else TreeNode(root.val,
                                              self.invertTree(root.right),
                                              self.invertTree(root.left))