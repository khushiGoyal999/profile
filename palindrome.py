#palindrome
name=input("Enter name:-")
reverse=name[::-1]
print(name)
print(reverse)

if(name==reverse):
    print("Plaindrome")
else:
    print("noy Plaindrome")