class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None  
    
    def Push(self,data):
        if self.top==None:
            n=Node(data)
            self.top=n
        else:
            n1=Node(data)
            n1.next=self.top
            self.top=n1

    def Display(self):
        if self.top==None:
            print("Stack is Empty")
        else:
            temp=self.top
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next

    def Pop(self):
        if self.top==None:
            print("Stack is Empty")
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None

s=Stack()
s.Push(10)
s.Push(20)
s.Push(30)
s.Push(30)
s.Pop()
s.Pop()
s.Pop()
s.Pop()
s.Display()
