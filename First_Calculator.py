# int addition(int x, int y) {
# 	int sum = x + y;
# 	return &sum;
# }

# int main() {
# 	unsigned int sum;
# 	sum = addition(4, 5);
# 	print(sum);

# 	return 0;
#

def addition(x, y):
	return (x + y)

def subtraction(x, y):
	return (x - y)

def multiplication(x, y):
	return (x * y)

def division(x, y):
	return (x / y)

def modulus(x, y):
	return (x % y)

def help():
	data = """
		1. Addition
		2. Subtraction
		3. Multiplication
		4. Division
		5. Modulus

		e. Exit Calculation
	"""
	print(data)

def operation():
	opr = ''
	while opr != 'e':
		help()
		opr = input("Enter the operation: ")
		if opr == 'e':
			break
		x = input("Enter somthing: ")
		y = input("Enter something: ")
		x = int(x)
		y = int(y)
		if opr == '1':
			sum = addition(x,y)
			print(sum)
		elif opr == '2':
			sub = subtraction(x,y)
			print(sub)
		elif opr == '3':
			mul = multiplication(x,y)
			print(mul)
		elif opr == '4':
			div = division(x,y)
			print(div)
		elif opr == '5':
			mod = modulus(x,y)
			print(mod)
		else:
			print("Invalid command!!")

	print("THANKS FOR USING NISSI'S CALCULATOR")


operation()

# x = ''
# while x != 'e':
# 	x = input("Enter something: ")
# 	print("You entered: ", x)