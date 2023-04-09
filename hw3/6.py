class Solution(object):
    def hasCycle(self, head):
        list = []
        while(head): #пока head не пустой
            if head in list:
                return True
            list.append(head)
            head = head.next
        else:
            return False

#Сложность O(n)