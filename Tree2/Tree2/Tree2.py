class Node:
    def __init__(self, data ,left = None ,right = None):
        self.data = data
        self.left = left
        self.right = right


def addi(r,data):
    if r is None:
        return Node(data)
    else:
        if data < r.data:
            r.left = addi(r.left,data)
        else:
            r.right = addi(r.right,data)
        return r
def inOrder(r):
    if r:
        inOrder(r.left)
        print(r.data , end = ' ')
        inOrder(r.right)           
def printSideway(r,level):
    if r:
        printSideway(r.right,level+1)
        print('   '*level,r.data,sep = ' ')
        printSideway(r.left,level+1)
def preOrder(r):
    if root:   
        print(r.data, end = ' ')
        preOrder(r.left)
        preOrder(r.right)
def postOrder(r):
    if r:             
        postOrder(r.left)
        postOrder(r.right)
        print(r.data, end = ' ')
def height(r):
    if r is None :
        return 0
    return max(height(r.left),height(r.right))+1
def search(r,data):
    if r is None:
        return None
    elif data < r.data :
        return search(r.left,data)
    elif data > r.data :
        return search(r.right,data)   
    else:
        return r.data   
def path(r,data):
    if r : 
        if data < r.data :         
            print(r.data,end = ' ')
            return path(r.left,data)
        elif data > r.data :
            print(r.data,end = ' ')
            return path(r.right,data) 
        elif data == r.data:
            print(r.data)
    else:
        return None
def depth(r,data):
    if r:
        if data < r.data :
            return depth(r.left,data)+1
        elif data > r.data :
            return depth(r.right,data)+1
        else:
            return 0
def children_count(node):
    cnt = 0
    if node.left:
        cnt += 1
    if node.right:
        cnt += 1
    return cnt

def delete(r,data,parent = None):
    if data < r.data:
        return delete(r.left,data,r)
    elif data > r.data:
        return delete(r.right,data,r)
    else:
        child = children_count(r)
        if child == 0:
            if parent:
                if parent.left is r:
                    parent.left = None
                else:
                    parent.right = None
                #del r
            else:
                r.data = None
        elif child == 1:
            if r.left:
                n = r.left
            else:
                n = r.right
            if parent:
                if parent.left is r:
                    parent.left = n
                else:
                    parent.right = n
                #del r
            else:
                r.left = n.left
                r.right = n.right
                r.data = n.data
        else:
            # if node has 2 children
            # find its successor
            parent = r
            successor = r.right
            while successor.left:
                parent = successor
                successor = successor.left
            # replace node data by its successor data
            r.data = successor.data
            # fix successor's parent's child
            if parent.left == successor:
                parent.left = successor.right
            else:
                parent.right = successor.right        

def deleteleaf(r,parent = None):
    if r:
        child = children_count(r)
        if child == 0:
            if parent:
                if parent.left is r:
                    parent.left = None
                else:
                    parent.right = None
                #del r
            else: 
                r.data = None
        else:
            deleteleaf(r.left,r)
            deleteleaf(r.right,r)
    else:
        return None

l = [14,4,9,7,15,3,18,16,20,5,16]

r = None
for ele in l:
    r = addi(r, ele)
print('inorder:')
inOrder(r)
print(' ')
print('printSideWay:')
printSideway(r, 0)
print('height of ', r.data, '=', height(r));
d = 5
print('path:', d, '=', end = ' ')
path(r, d)
d = 9
print('search of ', d,'=',search(r, d))
d = 18
print('depth of node data ', d, '=', depth(r, d))
deleteleaf(r)
printSideway(r, 0)