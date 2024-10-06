class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def isSymmetric(root):
    def isMirror(left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val==right.val and isMirror(left.left,right.right) and isMirror(left.right,right.left))
    if not root:
        return True
    return isMirror(root.left,root.right)
def buildTree(lst):
    if not lst:
        return None
    nodes=[None if val is None else TreeNode(val) for val in lst]
    kids=nodes[::-1]
    root=kids.pop()
    for node in nodes:
        if node:
            if kids:node.left=kids.pop()
            if kids:node.right=kids.pop()
    return root

print('-----------Test Case 1-----------')
root1=buildTree([1, 2, 2, 3, 4, 4, 3])
print(f'Input: [1, 2, 2, 3, 4, 4, 3]')
print(f'Output: {isSymmetric(root1)}')
print('-----------Test Case 2-----------')
root2=buildTree([1, 2, 2, None, 3, None, 3])
print(f'Input: [1, 2, 2, None, 3, None, 3]')
print(f'Output: {isSymmetric(root2)}')
print('-----------Test Case 3-----------')
root3=buildTree([1])
print(f'Input: [1]')
print(f'Output: {isSymmetric(root3)}')
print('-----------Test Case 4-----------')
root4=buildTree([])
print(f'Input: []')
print(f'Output: {isSymmetric(root4)}')
print('-----------Test Case 5-----------')
root5=buildTree([1, 2, 2, 3, None, None, 3])
print(f'Input: [1, 2, 2, 3, None, None, 3]')
print(f'Output: {isSymmetric(root5)}')
