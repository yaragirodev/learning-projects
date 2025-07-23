def plus(number1, number2):
	result = number1 + number2
	print(result)
	return

def minus(number1, number2):
	result = number1 - number2
	print(result)
	return

def umnozhenie(number1, number2):
	result = number1 * number2
	print(result)
	return

def delenie(number1, number2):
	result = number1 / number2
	print(result)
	return

while True:
	print("Добро пожаловать в мой калькулятор!!")
	get_num1 = int(input("Введите число (1): "))
	get_num2 = int(input("Введите число (2): "))
	get_mode = input("Выберите действие (+, -, *, /) - ")

	if get_mode == "+":
		plus(get_num1, get_num2)
		input("Нажмите что-нибудь...")

	elif get_mode == "-":
		minus(get_num1, get_num2)
		input("Нажмите что-нибудь...")

	elif get_mode == "*":
		umnozhenie(get_num1, get_num2)
		input("Нажмите что-нибудь...")

	elif get_mode == "/":
		delenie(get_num1, get_num2)
		input("Нажмите что-нибудь...")