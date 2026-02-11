# x = int(input("enter the no. to check even or odd"))
# if x


x = int(input("enter:"))
if x%5==0 and x%11== 0:
    print("by both")
elif x%5== 0:
    print("by 5")
elif x%11 == 0:
    print("by 11")

else:
    print("by none")            

