class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None


    # Insert at the beginning
    def Insert_at_beginning(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
        
    # Insert after a node
    def Insert_after(self,prev_node,value):
        if prev_node is None:
            print("The Previous Node do not exist")
            
        new_node = Node(value)
        new_node.next = prev_node.next    # Connects new node to the next node
        prev_node.next = new_node         # Connects new node to the previous node
        
        
    # Insert at the End
    def Insert_at_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            
        itr = self.head
        
        # Iterate through the entire linked list until it finds the last node
        while itr.next:
            itr = itr.next
        
        itr.next = new_node
        

    def Reverse(self):
        prev_node = None
        curr_node = self.head
        
        while curr_node != None:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        
        self.head = prev_node
    
    
    def Recursive_reverse(self,head):
        if (not head) or (not head.next):
            return head
        
        new_head = self.Recursive_reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
        
    # Display Linked List
    def Display(self):
        if self.head == None:
            print("Linked list is empty")
            
        else:
            current = self.head
            while current != None:
                print(current.item, end="-->")
                current = current.next

        
    def Delete_a_node(self,value):
        prev_node = None
        curr_node = self.head
        
        while curr_node is not None:
            if curr_node.item == value:
                if prev_node is None:
                    self.head = curr_node.next
                    
                else:
                    prev_node.next = curr_node.next
        
                return
            
            prev_node = curr_node
            curr_node = curr_node.next
    
    
    def Search(self,value):
        itr = self.head
        
        while itr is not None:
            if itr.item == value:
                print("Node found in the Linked list")
                break
            
            itr = itr.next
               
    
    def Sort(self):
        curr_node = self.head
        next_node = Node(None)
        
        if curr_node is None:
            return
        
        while curr_node is not None:
            next_node = curr_node.next
            
            while next_node is not None:
                if curr_node.item > next_node.item:
                    curr_node.item,next_node.item = next_node.item, curr_node.item
                    
                next_node = next_node.next
                
            curr_node = curr_node.next
            
    
llist = Linked_List()
llist.Insert_at_beginning(200)
llist.Insert_at_end(9)
llist.Insert_at_end(15)
llist.Insert_at_end(40)
llist.Insert_at_end(35)
llist.Display()
print()
print()
# llist.Insert_after(llist.head.next,15)
# llist.Display()
# print()
# print()
# llist.Reverse()
# llist.Display()
# print()
# print()
# llist.Reverse()
# llist.Delete_a_node(40)
# llist.Display()
# print()
# print()
# llist.Search(30)
# llist.Display()

llist.Sort()
llist.Display()