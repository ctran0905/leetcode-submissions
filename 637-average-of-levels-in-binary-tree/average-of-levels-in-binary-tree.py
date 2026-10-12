# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        queue = deque([root])
        ans = []

        # While queue still has nodes to pop
        while queue: 
            queue_len = len(queue)
            row_val = 0
            for i in range(queue_len):
                node = queue.popleft()
                row_val += node.val

                # Add node's child nodes to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(row_val/queue_len)
        
        return ans

