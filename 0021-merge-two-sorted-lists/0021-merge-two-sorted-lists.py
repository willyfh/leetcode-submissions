# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        ans = ListNode()
        temp = ans
        while list1 != None and list2!=None:
            if list1.val < list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                list2 = list2.next
            temp.next = newNode
            temp = temp.next
            
        if list1!=None:
            temp.next = list1
        if list2!=None:
            temp.next = list2
        
        
        return ans.next