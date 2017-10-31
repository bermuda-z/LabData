class Queue:
    def __init__(self, list = None):
        if list == None :
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
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
    def deQueue(self):
        return self.items.pop(0)
    def enCode(self,list,s):
        list2 = [] #String in list
        list3 = [] #num of string
        list4 = [] #num to string
        for i in range (len(list)):
            self.enQueue(list[i])

        for i in range (len(s)):
            list2.append(s[i])
            if list2[i] == ' ':
                num = 32
                list3.append(num)
            else :
                num = ord(list2[i])+self.items[0]
                if num > 122 or (num > 90 and num < 97):
                    num = num-26
                    list3.append(num)
                    out = self.deQueue()
                    self.enQueue(out)
                else:  
                    list3.append(num)
                    out = self.deQueue()
                    self.enQueue(out)
            list4.append(chr(list3[i]))
        for i in range (len(self.items)):
            self.deQueue()
        return list4
    def deCode(self,list,s):   
        list2 = [] #String in list
        list3 = [] #num of string
        list4 = [] #num to string
        for i in range (len(list)):
            self.enQueue(list[i])

        for i in range (len(s2)):
            list2.append(s2[i])
            if list2[i] == ' ':
                num = 32
                list3.append(num)
            else :
                num = ord(list2[i])-self.items[0]
                if  num < 65 or (num>90 and num<97):
                    num = num+26
                    list3.append(num)
                    out = self.deQueue()
                    self.enQueue(out)
                else:  
                    list3.append(num)
                    out = self.deQueue()
                    self.enQueue(out)
            list4.append(chr(list3[i]))
        return list4
#############################  main  #####################
q = Queue()
s1 = "I love Python"
list = [2,5,6,1,8,3]
s2 = "K quwm Saynpv"
print(q.enCode(list,s1))
print(q.deCode(list,s2))