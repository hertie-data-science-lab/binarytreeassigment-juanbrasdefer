# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Juan Brasdefer 225936, Fabian Pawelczyk 226921
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)



print(len(lbt))
print(lbt.height(lbt.root()))
print()




# Preorder Traversal
print("Preorder Traversal:")
for node in lbt.preorder():
    print(node.element(), end=" ")
print()

# Inorder Traversal
print("Inorder Traversal:")
for node in lbt.inorder():
    print(node.element(), end=" ")
print()

# Postorder Traversal
print("Postorder Traversal:")
for node in lbt.postorder():
    print(node.element(), end=" ")
print()

# Breadth-first Traversal
print("Breadth-first Traversal:")
for node in lbt.breadth_first():
    print(node.element(), end=" ")
print()



print("woohoooooo")