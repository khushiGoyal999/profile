 # draw a left pyramid
n=int(input("Enter n:-")) #take input from user
for r in range(1,n+1): #always row me column ati h so start loop with row(r),1 se start hoga fir 1+n
    for c in range(1,r+1):#r+1 islye coz row me star badhenge
        print("*", end=" ")#end is used to give space
    print()#this is used bcz every star gets a new line,after completing it in row


#draw right pyramid
n=int(input("Enter n:-"))
for r in range(1,n+1):
    for s in range(n-r,0,-1): #space is used to move star from left to right,n-r will count the space
        print(" ",end=" ")#it will give the space
    for c in range(1,r+1):
        print("*", end=" ")
    print() 

#draw a triangle
n=int(input("Enter n:-"))
for r in range(1,n+1):
    for s in range(n-r,0,-1):
        print(" ",end="")#remove space from end
    for c in range(1,r+1):
        print("* ", end="")#remove space from end and add space after * star
    print()

#draw triangle with different digits in each row
n=int(input("Enter n:-"))
for r in range(1,n+1): 
    for c in range(1,r+1):
        print(c, end=" ")
    print()

#draw triangle with same digits in each row
n=int(input("Enter n:-"))
for r in range(1,n+1): 
    for c in range(1,r+1):
        print(r, end=" ")#just remove "*", and add r
    print()

#draw right pyramid for different digits in each row
n=int(input("Enter n:-"))
for r in range(1,n+1):
    for s in range(n-r,0,-1): 
        print(" ",end=" ")
    for c in range(1,r+1):
        print(c, end=" ")
    print() 
    
#draw right pyramid for same digits in each row
n=int(input("Enter n:-"))
for r in range(1,n+1):
    for s in range(n-r,0,-1): 
        print(" ",end=" ")
    for c in range(1,r+1):
        print(r, end=" ")
    print()

#draw a upside down pyramid, it is incomplete,where 5 ,54,543,5432,54321
n=int(input("Enter n:-"))
for r in range(1,n+1):
    for s in range(n-r,0,-1): 
        print(" ",end=" ")
    for c in range(1,r+1):
        print(c, end=" ")
    print()