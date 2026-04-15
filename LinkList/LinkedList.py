# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LL:
#     def __init__(self):
#         self.head=None
#
#     def insert(self,data):
#         if self.head==None:
#             n=Node(data)
#             self.head=n
#         else:
#             n1=Node(data)
#             temp = self.head
#             while temp.next != None:  # go to last node
#                 temp = temp.next
#             temp.next = n1

    # def insert_position(self,pos,data):
    #     n=Node(data)
    #     temp=self.head
    #     for i in range(1,pos-1):
    #         temp=temp.next
    #     n.next=temp.next
    #     temp.next=n

    # def insert_end(self,data):
    #     if self.head==None:
    #         n=Node(data)
    #     else:
    #         n1=Node(data)
    #         temp=self.head
    #         while temp.next!=None:
    #             temp=temp.next
    #         temp.next=n1

    # def delete_begining(self):
    #     if self.head==None:
    #         print("Linked List is Empty")
    #     else:
    #         temp=self.head
    #         self.head=temp.next
    #         temp.next=None

    # def delete_ending(self):
    #     if self.head==None:
    #         print("Linked List is Empty")
    #     elif self.head.next==None:
    #         self.head=None
    #     else:
    #         temp=self.head
    #         while temp.next.next != None:
    #             temp=temp.next
    #         temp.next=None

    # def display(self):
    #     if self.head==None:
    #         print("Linked List is Empty")
    #     else:
    #         temp=self.head
    #         while temp:
    #             print(temp.data,end=" ")
    #             temp=temp.next


# l=LL()
# l.insert(10)
# l.insert(20)
# l.insert(30)
# l.insert(40)
# l.display()
# print()
# l.insert_position(4,35)
# l.display()
# print()
# l.delete_begining()
# l.delete_begining()
# l.display()
# print()
# l.delete_ending()
# l.display()
# l.insert_end(50)
# l.display()




