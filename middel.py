# to find the middel number from given 3 numbers
a = int(input("enter the first number "))
b = int(input(" enter the second number "))
c = int(input(" enter the third number "))

# logic
if a>b and a<c or a<b and a>c:
    print(f" the {a} is the middel number ")
elif b<a and b>c or b>a and b<c:
    print(f" the {b} is the middel number ")
else :
    print(f" the {c} is the middel number ")
print(" lets go")