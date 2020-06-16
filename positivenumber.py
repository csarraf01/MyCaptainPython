list=[]
n=int(input("ENter the no.of elements "))
for i in range(0,n):
    num=int(input())
    list.append(num)
for i in range(0,n):
    print()
    if list[i]>0:
        print(list[i],end=" ")
