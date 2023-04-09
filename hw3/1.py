class Solution(object):
    def isPalindrome(self, head):
        curr = head
        list = [] #создаем пустой список
        while curr:
            list.append(curr.val) #в созданный список добавляем элементы односвязного списка
            curr = curr.next
        if list == list[::-1]: #если при чтении с двух сторон список идентичен
            return True
        else:
            return False

#Сложность O(n)