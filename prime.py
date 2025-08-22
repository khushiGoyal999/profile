'''write a prog to check given number is prime or not'''
n=int(input("Enter no:"))
for i in range(2,n):
    if(n%i==0):
        print("not prime")
        break 
else:
    print("prime")