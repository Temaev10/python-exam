# 1
# while True:
#     num = int(input("введите число: "))
#     if num < 0:
#         break
#     else:
#         print(num ** 2)


# 2
# lst = ['c#', 'java', ['rust', 'python', 'js']]

# print([lst[2][1]])

# 3
# result = []
# for i in range(1,11):
#     result.append(i ** 2)

# print(result)


# def nums(a, b):
#     if a > b:
#         return a
#     else:
#         return b
    
# print(nums(5,6))



# from random import randint

# nums = []
# for i in range(5):
#     num = randint(1, 100)
#     nums.append(num)

# print(nums)



# def summa(a, b):
#     return a + b




# calenadr = {
#     'январь':31 ,
#     'февраль': 28, 
#     'март': 31
# }





import time 

correct_login = "Ansar"
correct_password = "12345"

count = 0

while True:
    login = input("введите логин: ")
    passorwd = input("введите пароль: ")

    if login == correct_login and passorwd == correct_password:
        print("добро пожаловать! ")
        break

    else:
        print('не правильный логин или пароль, повторите! ')
        count += 1

        if count >= 3:
            print('доступ заблокирован на 10 секунд')
            time.sleep(10)