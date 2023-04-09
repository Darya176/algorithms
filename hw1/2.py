#Алгоритм
# 1. Определить, четное кол-во команд (n), или нет
#   1.1 Если четное, то кол-во матчей (m) в раунде n / 2, и кол-во команд, перешедших в следующий раунд n /2
#   1.2 Если нечетное, то кол-во матчей в раунде (n-1)/ 2, и кол-во команд, перешедших в следующий раунд (n-1) /2 + 1
# 2. Увеличить общее кол-во матчей на m
# 2. Повторять, пока n != 1
#
#Сложность O(n)


def numberOfMatches(n):
    m = 0 #количество матчей в одном раунде
    matches = 0 #общее количество матчей
    while n > 1: #цикл, выполняющийся, пока не останется одна команда
        if n % 2 == 0: #если количество команд чётное
            m = n / 2
            n = n / 2
        elif n % 2 != 0: #если количество команд нечётное
            m = (n - 1) / 2
            n = (n - 1) / 2 + 1
        matches += m #к общему количеству матчей прибавляется количество сыгранных матчей в каждом раунде
    return matches #возвращаем количество матчей, сыгранных в турнире

print(numberOfMatches(14))


