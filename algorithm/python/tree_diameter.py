class Node(object):
    def __init__(self, value=None ):
        self.value=value
        self.children = []        

    def add(self, node):
        self.children.append(node)

    def __cmp__(self, o):
        return self.value - o.value

    def __str__(self):
        return str(self.value)


class Tree(object):
        
    def __init__(self):
        self.root = None 
        
    def add(self, parent, child):
    
        node = self.walk(parent)                
        if node is None:
            if self.root.value == child:
                new_node = Node(parent)
                new_node.add(self.root)
                self.root = new_node
            else:
                raise SyntaxError((parent, child))
        else:
            node.add(Node(child))        
            
    def walk(self, value):
        
        def find(node, value):            
            if node is None:
                return None
            
            if node.value == value:
                return node
            
            for child in node.children:
                found = find(child, value)
                if found is not None:
                    return found
            
            return None

        if self.root is None:
            self.root = Node(value)
            return self.root
        
        return find(self.root, value) 

    def show(self):
        def show_node(node):
            if node is None:
                return []
            ret=[]
            parent = node.value
            for child in node.children:
                ret.extend([(parent, child.value)] + show_node(child))
            return ret
        
        return show_node(self.root)

def depth(node):
    if node is None:
        return 0  
    
    if len(node.children) == 0:
        return 1

    return max(map(depth, node.children)) + 1


def diameter(node):    
    if node is None:
        return 0

    if len(node.children) == 0:
        return 1

    sum_depth = sum(sorted(map(depth, node.children), reverse=True)[:2]) 
    max_diameter = max(map(diameter, node.children))
    
    return max(sum_depth+1 , max_diameter)
    

def treeDiameter(n, tree):
    bt = Tree()
    
    for link in tree:        
        bt.add(link[0], link[1]) 
        
    print(bt.show())
    return diameter(bt.root) 


def main():
    n=10
    tree = [[1,3], 
 [7,3], 
 [5,3], 
 [8,7], 
 [4,1], 
 [2,3], 
 [9,4], 
 [0,8], 
 [6,8]]

    # nary = Tree()
    # for item in tree:
    #     nary.add(item[0], item[1])

    # print(nary.show() )
    
    print(treeDiameter(n, tree))

if __name__ == '__main__':
    main()
    