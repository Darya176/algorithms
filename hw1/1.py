#Алгоритм:
# 1. Проверяем, делится ли число без остатка на 2:
#     1.1 Если да, то делим число на 2 и увеличиваем кол-во шагов на 1
#     1.2 Если нет, то вычитаем из числа 1 и увеличиваем кол-во шагов на 1
# 2. Сложность О(n)



def numberOfSteps(num):
    steps = 0 #вводим переменную, обозначающую кол-во шагов, принимаем ее значение за 0
    while num > 0: #цикл, выполняющийся пока число не станет равным 0
        if num % 2 == 0: #если число чётное
            num = num / 2 #делим его на 2
        else:
            num -= 1 #если число нечётное: вычитаем 1
        steps += 1  #увеличиваем количество шагов на 1
    return steps #возвращаем количество шагов

print(numberOfSteps(8))