class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None
    root_value = preorder[0]
    root = TreeNode(root_value)
    root_index = inorder.index(root_value)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1:]
    left_preorder = preorder[1:1 + len(left_inorder)]
    right_preorder = preorder[1 + len(left_inorder):]
    root.left = build_tree(left_preorder, left_inorder)
    root.right = build_tree(right_preorder, right_inorder)
    return root

def postorder_traversal(node, result):
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.value)
def find_postorder(preorder, inorder):
    root = build_tree(preorder, inorder)
    result = []
    postorder_traversal(root, result)
    return result

nodeAmount = map(int, input().split())
preorder =  list(map(int, input().split()))
inorder = list(map(int, input().split()))

result = find_postorder(preorder, inorder)
print(*result)