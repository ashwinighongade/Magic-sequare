# magic squear


a=[]

for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("Enter the number :"))
        b.append(j)
    a.append(b)
print("Matrix is .....") 
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
sumd1=0
sumd2=0
for i in range(3):
    for j in range(3):
        if i==j:
            sumd1=sumd1+a[i][j]
        if i+j==3-1:
            sumd2=sumd2+a[i][j]
    # print(sumd1)
    # print(sumd2)
if sumd1!=sumd2:
    f=1
else:
    for i in range(3):
        sumr=0
        sumc=0
        for j in range(3):
            sumr=sumr+a[i][j]
            sumc=sumc+a[i][j]
        if sumr!=sumd1:
            f=1
        elif sumc!=sumd1:
            f=1
        else:
            f=0
if f==0:
    print("Matrix is magic square")
else:
    print("Matrix is not magic square")
            
    
        
   
