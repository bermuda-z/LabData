class Stack:
    def __init__(self, list = None):
        if list == None :
            self.items = []
        else:
            self.items = list
    def push(self,i):
        self.items.append(i)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def isFull(self):
        if len(self.items) == 4:
            return True
        else:
            return False
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def arrive(self,list):
        if self.isFull():
            print("car "+str(list) + " cannot arrive : SOI FULL")
        else :
            self.push(list)
            print("car "+str(list) + "         space " + str(4-self.size()))
    def depart(self,list):
        if self.isEmpty():
           print("car " + str(list) + " cannot depart : SOI empty")
        elif list not in self.items :
           print("car " + str(list) + " cannot depart : no car " + str(list))
        else :
           list1=[]
           for i in range(4):
               if self.items[len(self.items)-i-1] == list and len(self.items)-i-1>=0:
                   print(self.items[len(self.items)-i-1])
                   self.items.pop(len(self.items)-i-1)
       
s1=Stack()
s1.arrive(1)
s1.arrive(2)
s1.arrive(3)
s1.arrive(4)
print(s1.items)
s1.depart(3)
print(s1.items)
s1.depart(2)
print(s1.items)