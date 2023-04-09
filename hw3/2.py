class Solution(object):
    def getDecimalValue(self, head):
        string_head = ""
        while head:
            string_head += str(head.val) #добавляем в строку элементы односвязного списка
            head = head.next
        str_head_1 = int(string_head, 2) #пребразовываем двоичную строку в десятичную
        return str_head_1

#Сложность O(n)