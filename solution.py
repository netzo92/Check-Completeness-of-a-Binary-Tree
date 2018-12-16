# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def num_gens(self, root):
        if root is None: 
            return 0, 0, True
        else:
            left_min, left_max, left_truth = self.num_gens(root.left)
            right_min,right_max, right_truth = self.num_gens(root.right)
            print(root.val, left_min, left_max, left_truth)
            print(root.val, right_min, right_max, right_truth)
            curr_truth = None
            if left_truth is True and right_truth is True:
                if left_min>= right_max >= right_min >= left_max - 1>= left_min-1:
                    curr_truth = True
                else:
                    curr_truth = False
            else:
                curr_truth = False
            return min(left_min, right_min)+1, max(left_max, right_max)+1, curr_truth
    
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a, b, val = self.num_gens(root)
        print(a)
        print(b)
        return val
        
        
