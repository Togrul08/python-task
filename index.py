#Task1
number1 = int(input("write first number"))
number2 = int(input("write second number"))
if number1 > number2:
    print("number1 greater than number2")
elif number1 == number2:
    print("this numbers equal")
else:
    print("number2 greater than number1")    



#Task2
a = int(input("enter number"))
if a == 0:
    print("number is zero")
elif a > 0:
    print("number is positive")
else:
    print("number is negative")



#Task3
a = int(input("enter number"))

if a % 2 == 0:
    print("Even")
else:
    print("Odd")



#Task4
a = int(input("write your exam score"))
if a < 0 or a > 100:
    print("invalid score")
elif a >= 91:
    print("A")
elif 90 >= a >= 81:
    print("B")
elif 80 >= a >= 71:
    print("C")
elif 70 >= a >= 61:
    print("D")
elif 60 >= a >= 51:
    print("E")
else:
    print("F")



#Task5
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)


#Task6
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
op = input("Enter the operation")
if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "%":
    print(a % b)
elif op == "**":
    print(a ** b)
elif op == "//":
    print(a // b)
else:
    print("Invalid operation")



#Task7
age = int(input("Enter your age:"))
if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")



#Task8
a = int(input("Enter total purchase"))
discount = 0
if a <= 100:
    discount = 0
elif a > 100 and a < 300:
    discount = 10
elif a > 299 and a < 500:
    discount = 15 
else:
    discount = 20
b = a - a * discount / 100
print(f"Original prise is {a}, Discount is {discount}% , Final price is {b}")



#Task9

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))
if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)



#Task10
balance = 1000
amount = int(input("Enter withdrawal amount"))
if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
else:
    balance = balance - amount
    print(f"Remaining balance: {balance} AZN")



#Task11
usage = int(input("Monthly electricity usage in kWh"))
if usage < 0:
    print("Invalid")
elif 0 <= usage <= 100:
    rate = 0.08
elif  100 < usage <= 300:
    rate = 0.12
else:
    rate = 0.15
if usage >= 0:
    bill = usage * rate 
    print(f"Usage is {usage}, Applied rate is {rate}, Total bill is {bill}")


#Task12
distance = int(input("Enter distance"))
startingfee = 2
if distance < 0:
    print("Invalid")
elif distance <= 5:
    fee = 0.70
elif distance <= 15:
    fee = 0.60
else:
    fee = 0.50
if distance >= 0:
    distancefee = distance * fee
    total = startingfee + distancefee
    print(f"Starting fee {startingfee}AZN")
    print(f"Distance fee {distancefee}AZN")
    print(f"Total fare {total}AZN")



#Task13
age = int(input("Enter your age"))
salary = int(input("Enter your monthly salary"))
amount = int(input("Enter credit amount"))
if age < 18:
    print("Reject becasue you are maladoy")
else:
    if salary < 500:
        print("Reject because your kasibsan utanmaz adam helem gelir kredit goturur ged ozve adam balasi kimi is tap")
    else:
        if salary * 10 < amount:
            print("Reject razmerve gore mebleg sec")
        else:
            print("Accept")
    


#Task14
