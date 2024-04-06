# Tree
Trees are a data structure that consists of nodes similar to linked lists. Both linked lists and trees are connected by **Pointers**. Each node in a tree can connect via pointers to multiple other **Child Nodes**. This allows us to create a **Hierarchical Structure** that is unavailable in linked lists. The topmost node is called the **Root** and can have no parent nodes. The nodes with no children are called **Leaf Nodes**. We will discuss several types of trees Binary Trees, Binary Search Trees, and Balanced Binary Search Trees.

![Figure 1](/Trees.JPG)

<br>

## Binary Trees
In a Binary Tree no node connects to more than 2 child nodes or **Subtrees**. It is common for each child node to point back to the parent node.

<br>

## Binary Search Trees
A Binary Search Tree (BST) is a Binary Tree with some exceptions so that the data will be **Stored**. When adding data to a BST first compare the data being placed in the tree with the parent node. If the value of the data being added is less than the value of the parent it is added to the **Left** subtree. On the other hand if the value of the data being added is greater than the value of the parent it is added to the **Right** subtree.

![Figure 2](/Hierarchy.JPG)

<br>

## Balanced Binary Search Trees
A Balanced Binary Search Tree (Balanced BST) is a BST where the height of the tree is kept minimal by keeping left and right subtrees of each node as close to the same height as possible. The **Height of a Tree** is the maximum number of nodes between the root and leaves. The closer your tree is to being balanced the better efficent your tree will be. A Balanced BST will have the efficiency of O(log n). Balance is not achived on accident we rely on algorithms to maintain balance some common algorithms include: AVL Trees and Red-Black Trees. 

![Figure 3](/Balanced_Unbalanced.JPG)

### AVL Trees
AVL trees don't allow the height difference between subtrees to be greater than one. If the height difference is ever greater than one a rotation is preformed.

![Figure 4](/AVL_tree.JPG)

### Red-Black Trees
In a Red-Black tree every node caries and extra bit marking it as either red or black (the root is always black). Red nodes cannot have red children. Every path from a node to its descendant null nodes contains the same number of black nodes. New nodes are always red. If the height of the black nodes are out of balance color changes and a rotation is preformed.

![Figure 5](/Red-Black_tree.JPG)

<br>

## Inserting Into A BST
1. Begin the insertion process by starting at the root of the binary search tree.
2. Compare the value of the new node with the value of the current node.
3. If the value of the new node is less than the value of the current node, move to the left subtree. If the value is greater, move to the right subtree.
4. Repeat steps 2 and 3 recursively until you reach a leaf node where the new node can be inserted.
5. Insert the new node as a child of this leaf node. If the value of the new node is less than the leaf node's value, insert it as the left child. If the value of the new node is greater than the leaf node's value, insert it as the right child.

```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    if root is None:
        # Create a new node with the given value
        return TreeNode(value)
    
    # If the value is less than the current node, insert into the left subtree
    if value < root.value:
        root.left = insert_node(root.left, value)
    # If the value is greater than or equal to the current node, insert into the right subtree
    else:
        root.right = insert_node(root.right, value)
    
    return root

# Example usage:
root = None
values = [10, 5, 15, 3, 7, 12, 20]

# Inserting values into the binary search tree
for value in values:
    root = insert_node(root, value)
```
<br>

## Traversing A BST
Traversing a BST requires visiting each node of the tree in a specific order and displaying the data in the tree. An **In-Order Traversal** will display the data in ascending order. This will involve visiting the left subtree, then the current node, and finally the right subtree.

```python
def in_order_traversal(node):
    if node:
        # Traverse left subtree
        in_order_traversal(node.left)
        # Visit current node
        print(node.value)
        # Traverse right subtree
        in_order_traversal(node.right)
```
