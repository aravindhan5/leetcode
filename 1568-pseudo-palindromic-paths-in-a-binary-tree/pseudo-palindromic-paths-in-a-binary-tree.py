# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root):
        def dfs(node, mask):
            if not node:
                return 0

            # Toggle the bit corresponding to node value
            mask ^= (1 << node.val)

            # If leaf node
            if not node.left and not node.right:
                return 1 if (mask & (mask - 1)) == 0 else 0

            return dfs(node.left, mask) + dfs(node.right, mask)

        return dfs(root, 0)  