class Node:
    def __init__(self, data, next = None): 
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,data):
        self.data = data
    def setNext(self,next):
        self.next = next

class List:
    def __init__(self, n = None):
        if n==None:
            self.head=self.tail=None
            self.size=0
        else:
            self.head = self.tail=n
            self.size=1
    def __str__(self):
        p = self.head
        s = ""
        while p != None:
            s += str(p.data)
            p = p.next
        return s
    def isEmpty(self):
        if self.head == None:
            return True
        else :
            return False

    def insertAppend(self,n):      #insertbottom
        if self.head == None:
            self.head = n          
        else:    
            self.tail.next=n
        self.tail = n
        self.size += 1
    def insertFrist(self,n):       #insertfrist
        if self.head == None:
            self.insertAppend(n)
        else:
            n.next=self.head
            self.head=n
        self.size += 1
    def insertAfter(self,n,m):     #insertafter
        p = self.before(m).next
        n.next = p.next
        p.next = n
        self.size += 1
    def bottomUp(self,i):
        lasth = None
        if self.head == None:
            print("Nothing")
        else:
            perCent = (i*self.size)/100
            self.tail.next = self.head
            count=0
            while count != perCent:
                lasth=self.head
                self.head=self.head.next
                count+=1
            lasth.next = None
    def before(self,data):  #return node ก่อน node ที่ใส่ดาต้า
        current = self.head
        previous = None
        lastp = None
        while current != None:
            if current.data == data:
                previous = lastp
                break
            else:
                lastp = current
                current = current.next
        return previous
    def riffleShuffle(self,i):
        lasth = None
        if self.head == None:
            print("Nothing")
        else:
            self.head1=self.head
            tail1=self.head
            self.head2=self.head
            tail2=self.tail
            perCent = int((i*self.size)/100)
            if perCent <1:
                perCent=1
            count=0
            while count != perCent:
                lasth=self.head2
                self.head2=self.head2.next
                count+=1
            tail1=lasth
            lasth.next = None
            
            self.head = self.tail = None
            self.size = 0

            if self.head == None:
                self.head = self.tail = self.head1
                self.head1 = self.head1.next
                self.size = 1
            while self.head1!=None and self.head2 !=None:
                if self.size %2!=0 :
                        self.tail.next = self.head2
                        self.tail = self.head2
                        self.head2 = self.head2.next
                        self.size+=1
                else:
                        self.tail.next = self.head1
                        self.tail = self.head1
                        self.head1 = self.head1.next
                        self.size+=1
            size1=0
            size2=0
            p1 = self.head1
            p2 = self.head2
            while p1!=None:
                size1+=1
                p1=p1.next
            while p2!=None:
                size2+=1
                p2=p2.next
            if self.head1 == None:
                self.tail.next = self.head2
                self.tail = self.head2
                self.size +=size1
            elif self.head2 == None:
                self.tail.next = self.head1
                self.tail = self.head1
                self.size +=size2

            s3 = ""
            while self.head != None:
                s3 += str(self.head.data)
                self.head = self.head.next
            print(s3)
    
    def removeHead(self):
        self.head = self.head.next
        self.size-=1
    def removeTail(self):
        p = self.before(self.tail.data)
        p.next = None
        self.tail = p
        self.size-=1
    def remove(self,data):
        p = self.before(data)
        if self.head == None:
            print("error")
        else:
            if self.head.data == data:
                self.removeHead() 
            elif self.tail.data == data:
                self.removeTail()
            else:
                p.next = p.next.next
    

     

A = List()
A.insertAppend(Node(1,None))
A.insertAppend(Node(2,None))
A.insertAppend(Node(3,None))
A.insertAppend(Node(2,None))
A.insertAppend(Node(5,None))
A.insertAppend(Node(6,None))
A.insertAppend(Node(2,None))
A.insertAppend(Node(8,None))
A.insertAppend(Node(2,None))
A.insertAppend(Node(10,None))
################################################################

h = []
def printList(h):     
    if h is not None:         
        print(h.data, end = ' ')         
        printList(h.next) 
 
def createLfromlist(h, i):     
    global fromList      
    if i >= 0:         
        p = Node(fromList[i], h)         
        p = createLfromlist(p, i-1)         
        return p     
    else:         
        return h 
def delete(h,data):
    if h.data == data:
        h = h.next
    if h.next != None:
        if  h.next.data == data:
            h.next = h.next.next
        delete(h.next,data)

fromList = [1,5,2,2,4,3] 
i = len(fromList)-1 
h = None 
h = createLfromlist(h, i)
delete(h,2)
printList(h)


