#!/usr/bin/env python
""" Binary Search Tree"""

class Node:
    """ Node"""
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class BST:
    'Binary Search Tree'

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self._add(val,self.root)


    def _add(self, val, node):
        if val < node.v:
            if node.l != None:
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r != None:
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root != None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if node == None:
            return None

        if val == node.v:
            return node
        elif val < node.v :
            return self._find(val, node.l)
        else:
            return self._find(val, node.r)


    def delete_tree(self):
        self.root = None

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node != None:
            self._print_tree(node.l)
            print str(node.v),
            self._print_tree(node.r)


    def addAll(self, *elems):
        for e in elems:
            self.add(e)

tree = BST()
tree.addAll(*[5, 1, 6, 2, 7, 4, 8, 3, 9])

tree.print_tree()
