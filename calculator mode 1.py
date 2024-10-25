#calculator
user = input("choose what you want to do   +,-,*,/ :")
number_1 = float(input("choose a number : "))
number_2 = float(input("choose a second number : "))
if user == "+":
    result = number_1 + number_2
    print(result)
elif user == "-":
    result = number_1 - number_2
    print(result)
elif user == "*":
    result = number_1 * number_2
    print(result)
elif user == "/":
    result = number_1 / number_2
    print(result)
else :
    print("see you soon")




