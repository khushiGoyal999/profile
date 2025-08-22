'''write amenu driven prog to find the area of square,rectagle,circle,triangle'''
'''u can write true instead of 1'''
while(1):      
    print("\n***********************")
    print("Press 1 for square")
    print("Press 2 for rectagle")
    print("Press 3 for circle")
    print("Press 4 for triangle")
    print("Press 5 for exit")
    ch=int(input("enter your choice="))
    if(ch==1):
        l=float(input("enter length:-"))
        area=l*l
        print("area of sqaure= ",area)
    elif(ch==2):
        l=float(input("enter length:-"))
        b=float(input("enter breadth:-"))
        area=l*b
        print("area of rectangle= ",area)
    elif(ch==3):
        r=float(input("enter radius:-"))
        area=3.14*r*r
        print("area of circle= ",area)
    elif(ch==4):
        l=float(input("enter length:-"))
        h=float(input("enter height:-"))
        area=1/2*l*h
        print("area of triangle= ",area)
    elif(ch==5):
        break
    else:
        print("Invalid choice!!!!!")
