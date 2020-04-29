def check_armstrong(number):
    number = str(number)
    sum = 0
    power = len(number)
    for digit in number:
        sum = sum + int(digit)**power
    if sum==int(number):
        return True
    else:
        return False

number = int(input("enter an integer number:"))
armstrong = check_armstrong(number)
if armstrong:
	print(number,"is a armstrong number")
else:
	print(number,"is not a armstrong number")