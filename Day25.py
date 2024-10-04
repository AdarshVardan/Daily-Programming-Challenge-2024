class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def isValidBST(root: TreeNode)->bool:
    def validate(node,low=float('-inf'),high=float('inf')):
        if not node:
            return True
        if not (low<node.val<high):
            return False
        return (validate(node.left,low,node.val) and 
                validate(node.right,node.val,high))
    return validate(root)

def build_tree(values):
    if not values:
        return None
    nodes=[None if val is None else TreeNode(val) for val in values]
    kids=nodes[::-1]
    root=kids.pop()
    for node in nodes:
        if node:
            if kids: node.left=kids.pop()
            if kids: node.right=kids.pop()
    return root

print('-----------Test Case 1-----------')
root = build_tree([2,1,3])
print('Input: root = [2, 1, 3]')
print(f'Output: {isValidBST(root)}')
print('-----------Test Case 2-----------')
root = build_tree([5,1,4,None,None,3,6])
print('Input: root = [5, 1, 4, None, None, 3, 6]')
print(f'Output: {isValidBST(root)}')
print('-----------Test Case 3-----------')
root = build_tree([10,5,15,None,None,6,20])
print('Input: root = [10, 5, 15, None, None, 6, 20]')
print(f'Output: {isValidBST(root)}')
