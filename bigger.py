def bigger(a, b):
    if a > b:
        print(f'{a} больше чем {b}!')

    if b > a:
        print(f'{b} больше чем {a}!')

in1 = int(input("Число 1 - "))
in2 = int(input("Число 2 - "))

bigger(in1,in2)
