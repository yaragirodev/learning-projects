import time

task_one = input("Введите задачу - ")
task_two =  input("Введите задачу - ")
task_three = input("Введите задачу - ")
task_four = input("Введите задачу - ")
task_five = input("Введите задачу - ")

task_list = f"""
1. {task_one}
2. {task_two}
3. {task_three}
4. {task_four}
5. {task_five}
"""

time.sleep(1)
print(task_list)
input()