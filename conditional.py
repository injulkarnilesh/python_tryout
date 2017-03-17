
b = True
d = False

print(b, type(b));
print(d, type(d));

print("23 > 12", 23 > 12)
print("23 < 12", 23 < 12)
print("23 == 12", 23 == 12)
print("23 >= 12", 23 >= 12)
print("23 =< 12", 23 <= 12)

num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))


if num1 > num2 :
    print("Executed if")
    print("Number1 is greater than Number 2")
elif num1 < num2 :
    print("Executed elif")
    print("Number 2 is greater than Number 1")
else :
    print("Executed else")
    print("Number 1 is equal to number 2")
    print("Inside nesting")
print("Outside nesting")
        
if False:
    print("Without spacing does not work")
print("Spacing is important")    


if not ( (num1 > num2 and (num2 % 2) == 0) or (num2 == num1 and (num1 % 5) == 0) ) :
    print("Not And Or")
