
n = int(input("enter a number "))
i=1
print("patern 1")
for i in range(n):
    print("*"*i)
    i = i+1
    
print("patern 2")
for i in range(n):
    print("*"*i)
    i = i+1

print("patern 3")
for i in range(n):
    print((" "*(n-i)) + ("* "*i))
    i = i+1
    
print("patern 4")
for i in range(n):
    print((" "*i) + ("* "*(n-i)))
    i = i+1
    
print("patern 5")
for i in range(n):
    print((" "*(n-i)) + ("* "*i))
    i = i+1
for i in range(n):
    print((" "*i) + ("* "*(n-i)))
    i = i+1
