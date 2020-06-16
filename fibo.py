n=int(input("Enter the number of terms: "))
n1,n2=0,1
count = 0
if n<=0:
   print("Invalid Input");
elif n==1:
   print("Fibonacci Series ")
   print(n1)

else :
    print("Fibonacci Series ")
    while count<n:
        print(n1,end=" ")
        temp=n1+n2
        n1=n2
        n2 = temp
        count += 1
