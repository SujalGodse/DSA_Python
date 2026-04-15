# Linear Data Structure : Tree , Graph
# Tree: Node,Parent, Child, Leaf, Ancestor, Siblings, Root, Branches

# 1.Binary Tree : Tree which is having 2 or 0 child
# -> Types of Binary Tree :
# 1) Full Binary Tree - Tree which has 2 child or leaf node having 0 child
# 2) Perfect Binary Tree - Node having 2 child of parent and leaf node having 0 child forming symmetric figure
# 3) Complete Binary Tree - Leaf node should be at 0th and 1st height
# 4) Pathological Binary Tree - Node having at most 1 child node
# 5) Skewed Binary Tree - i) Left Skewed Binary Tree : nodes lying at left side of root node
#                         ii) Right Skewed Binary Tree : nodes lying at right side of root node
# 6) Balanced Binary Tree - The height of left subtree and right subtree should be same

#Example 1
# class Node:
#     def __init__(self,data):                         #                    10
#         self.data=data                               #                 /       \
#         self.left=None                               #             20              30
#         self.right=None                              #            / \                 \
#                                                      #         40      50              60
# root=Node(10)
# root.left=Node(20)
# root.right=Node(30)
# root.left.left=Node(40)
# root.left.right=Node(50)
# root.right.right=Node(60)
# print(root.right.right.data)
#
# # Depth Traversal
# # 1.Inorder Traversal - left->top->right       #Inorder of above tree : 40,20,50,10,30,60
# # 2.Preorder Traversal - top->left->right
# # 3.Postorder Traversal - left->right->top
#
# class Tree:
#     def inorder(root):
#         if root!=None:
#             Tree.inorder(root.left)
#             print(root.data,end=" ")
#             Tree.inorder(root.right)
# Tree.inorder(root)


# Example 2
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#
# root=Node(10)
# root.left=Node(20)
# root.right=Node(30)
# root.left.left=Node(35)
# root.left.right=Node(45)
# root.right.left=Node(55)
# root.right.right=Node(65)
# root.left.right.left=Node(79)
# root.left.right.right=Node(80)
# root.right.left.right=Node(99)
# root.right.right.left=Node(100)
# # print(root.left.right.left.data)
#
# class Tree:
    # def inorder(root):
    #     if root!=None:
    #         Tree.inorder(root.left)
    #         print(root.data, end=" ")
    #         Tree.inorder(root.right)
    #
    # def preorder(root):
    #     if root!=None:
    #         print(root.data,end=" ")
    #         Tree.preorder(root.left)
    #         Tree.preorder(root.right)
    #
    # def postorder(root):
    #     if root!=None:
    #         Tree.postorder(root.left)
    #         Tree.postorder(root.right)
    #         print(root.data, end=" ")
    # def height(root):
    #     if root==None:
    #         return 0
    #     else:
    #         lh = Tree.height(root.left)
    #         rh = Tree.height(root.right)
    #         return max(lh, rh) + 1

# Tree.inorder(root)
# print()
# Tree.preorder(root)
# print()
# Tree.postorder(root)
# print()
# print(Tree.height(root))


#Example 3
# class Node:
#     def __init__(self,data):                         #                    10
#         self.data=data                               #                 /       \
#         self.left=None                               #             20             30
#         self.right=None                              #            /              /    \
#                                                      #         25              40      50
# root=Node(10)                                        #                                 /
# root.left=Node(20)                                   #                               60
# root.right=Node(30)
# root.left.left=Node(25)
# root.right.right=Node(50)
# root.right.left=Node(40)
# root.right.right.left=Node(60)
#
# class Tree:
#     def height(root):
#         if root==None:
#             return 0
#         else:
#             lh=Tree.height(root.left)
#             rh=Tree.height(root.right)
#             return max(lh,rh)+1
# print(Tree.height(root))


