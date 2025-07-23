def agesystem(age):
	agenew = age + 10
	print(f"Вам будет {agenew} через 10 лет!")
	return agenew

ageinput = int(input("Введите свой возраст - "))
agesystem(ageinput)
input()