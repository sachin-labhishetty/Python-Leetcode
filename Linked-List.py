class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Sol:
  def rev_linklist(self, head:ListNode) -> ListNode:
    prev = head
    node = prev.next
    prev.next = None
    
    while(node.next is not None):
      temp = node.next
      node.next = prev
      prev = node
      node = temp
    
    return(prev)
