'''
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/?envType=daily-question&envId=2024-02-25
236. 二叉树的最近公共祖先

'''

#三个参数:  root结点, p结点, q结点
#功能: 返回 p和q 的lca
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in {None, p, q}:  #node竟然可以直接set
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:    return root
        return left or right