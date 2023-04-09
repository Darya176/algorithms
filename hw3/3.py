class Solution(object):
    def averageOfLevels(self, root):
        stack = [root]  # root-начальное значение обхода(корень)
        answer = []

        while stack:
            lenght = len(stack)  # lenght = количеству элементов в stack
            count = 0  # счетчик кол-ва элементов на уровне
            curr_level = .0  # сумма элементов на уровне

            while count < lenght:
                curr = stack.pop(0)  # возвращаем значение 0-го элемента и удаляем его из stack
                curr_level += curr.val
                if curr.left != None:  # если слева от вершины существует другая
                    stack.append(curr.left)
                if curr.right != None:
                    stack.append(curr.right)
                count += 1  # к кол-ву элементов на уровне прибавляем 1

            answer.append(round(curr_level / lenght, 5))  # в ответ добавляем сумму элементов/колчество этих элементов

        return answer

# Сложность O(n)