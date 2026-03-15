num = int(input("Enter a number "))
digit1 = num//1000
digit2 = (num//100)%10
digit3 = (num//10)%10
digit4 = num%10
reves_num = (digit1*1)+ (digit2*10 ) + (digit3*100) + digit4*1000

if reves_num == num :
    print(f" the number {reves_num} is palindrome ")
else:
    print(f" the number {reves_num} is not palindrome ")