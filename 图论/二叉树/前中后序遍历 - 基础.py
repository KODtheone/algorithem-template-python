'''



'''

# 参数: node是给出的root  res 是自己写一个空列表 用来存放遍历值
def inorder(node: TreeNode, res: List[int]):
    if node:
        inorder(node.left, res)
        res.append(node.val)
        inorder(node.right, res)

