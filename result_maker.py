# take the five subjects marks from the user
sub1 = int( input(" enter the first subject marks"))
sub2 = int( input(" enter the second subject marks"))
sub3 = int( input(" enter the third subject marks"))
sub4 = int( input(" enter the fourth  subject marks"))
sub5 = int( input(" enter the fifth  subject marks"))
percentage = ((sub5+sub4+sub3+sub2+sub1)/500)*100
print(f" the percentage is {percentage}")
if sub1 > 33 and sub2>33 and sub3>33 and sub4>33 and sub5>33 :
    print(" YOU ARE PASS")
else:
    print(" YOU ARE FAIL")


