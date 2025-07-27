# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         newnode = Node(data)
#         if self.root is None:
#             self.root = newnode
#         else:
#             temp = self.root
#             while True:
#                 if data < temp.data:
#                     if temp.left is None:
#                         temp.left = newnode
#                         break
#                     else:
#                         temp = temp.left
#                 else:
#                     if temp.right is None:
#                         temp.right = newnode
#                         break
#                     else:
#                         temp = temp.right

#     def inorder(self, root):
#         if root is not None:
#             self.inorder(root.left)
#             print(root.data, end=" ")
#             self.inorder(root.right)
#     def preorder(self, root):
#         if root is not None:
#             print(root.data, end=" ")
#             self.preorder(root.left)
#             self.preorder(root.right)
#     def postorder(self, root):
#         if root is not None:
#             self.postorder(root.left)
#             self.postorder(root.right)
#             print(root.data, end=" ")

# t = Tree()
# t.insert(50)
# t.insert(100)
# t.insert(75)
# t.insert(5)
# t.insert(3)
# t.insert(12)
# t.insert(7)
# t.insert(110)
# t.insert(107)
# t.insert(2)
# t.insert(4)
# t.insert(117)
# t.insert(116)

# t.inorder(t.root)
# print()
# t.preorder(t.root)
# print()
# t.postorder(t.root)
# print()


# from collections import deque
# queue = deque([1,2,3])
# queue.append(queue.popleft())
# queue.popleft()
# print(["hai" for i in queue])



# stack= []
# info = {'a': 1, 'b': 2, 'c': 3}
# stack.append('a')
# stack.append('b')
# if info[stack[-1]]%2 == 0:
#     stack.pop()
# stack.append('c')
# if info[stack[0]] + info[stack[-1]] > 3:
#     stack.append('d')
# print(stack)
