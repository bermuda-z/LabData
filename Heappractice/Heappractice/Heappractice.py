def print90(l,index,level):
    if index < len(l):
        print90(l,index*2+1,level+1)    
        print('   '*level,l[index],sep = ' ')
        print90(l,index*2,level+1) 

def insert(h,val):
    h.append(val)
    i = len(h)-1
    while i//2 > 0:
      if h[i] < h[i // 2]:
         h[i] ,h[i // 2] = h[i // 2] , h[i]
      i = i//2

def minChild(h,i,k):
    if i * 2 + 1 > k:
        return i * 2
    else:
        if h[i*2] < h[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1
def delMin(h,k):
    re = h[1]
    h[1] = h[k]
    i=1
    while (i * 2) <= k:
        mc = minChild(h,i,k)
        if h[i] > h[mc]:
            h[i] , h[mc] = h[mc],h[i]
        i = mc
    h[k] = re
##################################### heap ################################
l = [0,68,65,32,24,26,21,19,13,16,14] 
h = []
a = []

for i in range(len(l)):
    insert(h,l[i])
print(h[1:])
print90(h,1,0)
print("=================== heap sort ==========================")
for i in range (1,len(h)-1):
    delMin(h,len(h)-i)
print(h[1:])
print90(h,1,0)
