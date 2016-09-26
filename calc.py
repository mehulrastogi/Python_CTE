a=0
b=0

print "This Is a Basic Calculator:"
print "Enter 2 numbers "
a=int(input("1st number:"))
b=int(input("2nd number:"))

print "1:ADD \n 2:SUBTARCT \n 3:MUTIPLY \n 4:DIVIDE \n"

c=int(input("choose 1 option:"))

if c == 1:
	print a+b
elif c == 2:
	print a-b
elif c == 3:
	print a*b
elif c ==  4:
	print a/b
else:
	print "-----ERROR 404:NOT FOUND------"


