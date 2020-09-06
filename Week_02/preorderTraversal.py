# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.left, i.val])
            elif isinstance(i, int):
                output.append(i)
        return output