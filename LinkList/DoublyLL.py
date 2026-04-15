class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            n = Node(data)
            self.head = n
        else:
            n1=Node(data)
            temp = self.head
            while temp.next:
                temp=temp.next
            temp.next = n1    # link forward
            n1.prev=temp    # link backward
            temp=n1

    def insert_begining(self,data):
        if self.head is None:
            n = Node(data)
            self.head = n
        else:
            n1=Node(data)
            n1.next=self.head
            self.head.prev=n1
            self.head=n1

    def delete_end(self):
        if self.head==None:
            print("Doubly LL is Empty")
        temp=self.head
        if temp.next==None:
            self.head=None
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        temp.prev = None

    def delete_begining(self):
        if self.head==None:
            print("Doubly LL is Empty")
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def display(self):
        if self.head is None:
            print("DoublyLL is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" ")
                temp = temp.next


d = DoublyLL()
d.insert(10)
d.insert(20)
d.insert(30)
d.insert(40)
d.display()
print()
# d.insert_begining(5)
# d.insert_begining(1)
# d.display()
# print()
# d.delete_end()
# d.delete_end()
# d.display()
# print()
# d.delete_begining()
# d.delete_begining()
# d.display()
