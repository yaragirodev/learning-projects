def hello(name, age):
	print(f"Привет! Тебя зовут {name}, и тебе {age} лет!" )

name = input("Имя - ")
age = int(input("Возраст - "))

hello(name, age)

if age < 10:
	print(f"Оу {name}, так ты вообще ребенок!")

if age > 12:
	print(f"Оу! Подросток, да? Круто! Я тоже!")

if age > 30:
	print(f"Ух ты! Мужчина в рассвете сил!")

input()
