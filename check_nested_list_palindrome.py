from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.value = val
        self.next_node = next_node

    def __str__(self):
        result = list()
        current_pointer = self # текущий узел
        while current_pointer:
            result.append(str(current_pointer.value))
            current_pointer = current_pointer.next_node
        return ' --> '.join(result)

class Solution:
    def isPalindrome(self, head_pointer: Optional[ListNode]) -> bool:
        if not head_pointer.next_node:
            return True

        # находим середину списка
        slow_pointer,fast_pointer = head_pointer,head_pointer
        while fast_pointer and fast_pointer.next_node:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node


        # разворачиваем вторую половину списку с slow_pointer
        previous_pointer,current_pointer = None,slow_pointer
        while current_pointer:
            next_step_node = current_pointer.next_node
            current_pointer.next_node = previous_pointer #1 n-> None #2 n-1 > n #3 n-2 > n-1 > n
            previous_pointer = current_pointer #1 n #2 n-1 #3 n-2
            current_pointer = next_step_node #1 n-1 #2 n-2 #n-3


        # проверка на пaлиндром
        left_pointer,right_pointer = head_pointer,previous_pointer
        is_palindrome = True
        while right_pointer:
            if left_pointer.value != right_pointer.value:
                is_palindrome = False
                break
            left_pointer = left_pointer.next_node
            right_pointer = right_pointer.next_node

        # возвращаем вложенный список
        previous_pointer,current_pointer = None,previous_pointer
        while current_pointer:
            next_step_node = current_pointer.next_node
            current_pointer.next_node = previous_pointer
            previous_pointer = current_pointer
            current_pointer = next_step_node

        return is_palindrome



def create_linked_list(values):
    if not values:
        return None

    head_node = ListNode(values[0])
    current_node = head_node
    for value in values[1:]:
        current_node.next_node = ListNode(value)
        current_node = current_node.next_node
    return head_node



def test_lined_list_palindrome():
    solution = Solution()
    #test One
    values = [1,2,3,4,2,1]
    head_pointer = create_linked_list(values)
    result = solution.isPalindrome(head_pointer)
    print(f"Is Linked List {head_pointer} a palindrome? answer: {result}")


test_lined_list_palindrome()

