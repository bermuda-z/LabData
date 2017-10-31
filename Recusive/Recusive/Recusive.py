def printNdown(n):
    if n == 1:
        print(n)
    else:
        print(n)
        printNdown(n-1)
       
#printNdown(-2)

def printToN(n):
    if n==1:
        print(n)
    else:
        printToN(n-1)
        print(n)

#printToN(4)

def sumToN(n):  
    if n==1:
        n=1
    else:        
        n+=sumToN(n-1)
        
    return n
#print(sumToN(5))

def printFlow(L,i):
    if i<len(L):
        print(L[i],end = ' ')
        printFlow(L,i+1)      
L = [2,3,4,5,6]
#printFlow(L,0)       

def printBack(L,i):
    if i<len(L):
        printBack(L,i+1)
        print(L[i])       
#printBack(L,0)

def App(L,n):
    if n ==1:
        L.append(1)
    else:
        App(L,n-1)        
        L.append(n)
        
def AppB(L,n):
    if n ==1:
        L.append(1)
    else:       
        L.append(n)
        AppB(L,n-1)        
        
list = []       
AppB(list,5)
print(list)