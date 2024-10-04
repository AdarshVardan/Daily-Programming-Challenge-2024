class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
        
def lowestCommonAncestor(tree_values,p_val,q_val):
    def build_tree(values):
        if not values:
            return None
        nodes=[None if val is None else TreeNode(val) for val in values]
        kids=nodes[::-1]
        root=kids.pop()
        for node in nodes:
            if node:
                if kids:node.left=kids.pop()
                if kids:node.right=kids.pop()
        return root

    def find_node(root,val):
        if root is None:
            return None
        if root.val==val:
            return root
        left=find_node(root.left,val)
        return left if left else find_node(root.right,val)

    def find_lca(root,p,q):
        if not root:
            return None
        if root==p or root==q:
            return root
        left_lca=find_lca(root.left,p,q)
        right_lca=find_lca(root.right,p,q)
        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca
    root = build_tree(tree_values)
    p=find_node(root,p_val)
    q=find_node(root,q_val)
    return find_lca(root,p,q)

print('-----------Test Case 1-----------')
print('Input: root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p = 5, q = 4')
print(f'Output: {lowestCommonAncestor([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],5,4).val}')
print('-----------Test Case 2-----------')
print('Input: root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], p = 5, q = 1')
print(f'Output: {lowestCommonAncestor([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],5,1).val}')
print('-----------Test Case 3-----------')
print('Input: root = [1, 2], p = 1, q = 2')
print(f'Output: {lowestCommonAncestor([1, 2],1,2).val}')
