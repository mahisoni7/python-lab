#part1
# x1 = int(input("enter value x1:"))
# x2 = int(input("enter value x2:"))
# y1 = int(input("enter value y1:"))
# y2 = int(input("enter value y2:"))
# import math
# d = math.sqrt((x2-x1)**2+(y2-y1)**2)
# print("distance of points are:",d)

 
# x1 = int(input("enter value x1:"))
# x2 = int(input("enter value x2:"))
# y1 = int(input("enter value y1:"))
# y2 = int(input("enter value y2:"))
# midx = ((x1 + x2)/2) 
# midy = ((y1+y2)/2)
# print((midx,midy))

#part b of exp2 command line 
# import sys
# if(len(sys.argv))!= 3:
#     print("addition of 2 arg by using add.py <a> <b>")
#     sys.exit(1)
# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
# result = num1 + num2
# print(" sum is :" , result)




import sys
if(len(sys.argv))!= 4:
    print("addition of 2 arg by using add.py <a> <b>")
    sys.exit(1)
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
num3 = int(sys.argv[3])
result = num1 * num2 * num3
print(" multi is :" , result)


