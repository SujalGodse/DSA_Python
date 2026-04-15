class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLL:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        if self.head==None:
            n=Node(data)
            self.head=n
            self.head.next = n
        else:
            n1=Node(data)
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=n1
            n1.next=self.head

    def delete_end(self):
        if self.head==None:
            print("CircularLL is Empty")
        else:
            temp=self.head
            while temp.next.next!=self.head:
                temp=temp.next
            temp.next.next=None
            temp.next=self.head


    def display(self):
        if self.head==None:
            print("CircularLL is Empty")
        else:
            temp = self.head
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break

c=CircularLL()
c.insert_end(10)
c.insert_end(20)
c.insert_end(30)
c.insert_end(40)
c.display()
print()
c.delete_end()
c.delete_end()
c.display()