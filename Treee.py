from compression import Tree, Node

def BuildTreee(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder.pop(0)
    root = Node(root_val)
    inorder_index = inorder.index(root_val)

    root.left = BuildTreee(preorder, inorder[:inorder_index])
    root.right = BuildTreee(preorder, inorder[inorder_index + 1:])

    return root


def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)


def preorder_traversal(node):
    if node:
        print(node.value, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)


# Example usage:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = BuildTreee(preorder, inorder)

print("Inorder Traversal:")
inorder_traversal(root)

print("\nPreorder Traversal:")
preorder_traversal(root)

tree = Tree()
tree.root = root

print(tree)
