from __future__ import print_function
from collections import deque

class Node(object):

    def __init__(self, value=None, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

    def __repr__(self):
        return "Node(value={value},left={left},right={right})".format(**self.__dict__)


class BinaryTree(object):

    def __init__(self):
        self.root=None
        
    def inorder(self):
        def inorder_helper(node):
            if node is not None:
                inorder_helper(node.left)
                print(node.value)
                inorder_helper(node.right)

        inorder_helper(self.root)

    def bfs(self):
        queue=deque()
        queue.append(self.root)

        while len(queue) > 0:
            item = queue.popleft()
            if item is None:
                continue

            print(item.value)
            
            queue.append(item.left)
            queue.append(item.right)

    def zigzag(self):
        stack=[]
        stack.append(self.root)
        
        while len(stack) > 0:
            item = stack.pop()
            if item is None:
                continue
            print(item.value)
            stack.append(item.left)
            stack.append(item.right)

def buildTree():
    '''
                5
              7    10
            3     1   14
          4   2  6  9
    '''
    

    data=[Node(5), Node(7), Node(3), Node(4), Node(2), Node(10), Node(1),Node(6), Node(9), Node(14)]

    data[2].left = data[3]
    data[2].right = data[4]
    data[1].left = data[2]
    data[6].left = data[7]
    data[6].right = data[8]
    data[5].left = data[6]
    data[5].right = data[9]
    data[0].left = data[1]
    data[0].right = data[5]
    bt = BinaryTree()
    bt.root = data[0]
    return bt


bt = buildTree()
#bt.inorder()
#print('----')
#bt.bfs()
bt.zigzag()

