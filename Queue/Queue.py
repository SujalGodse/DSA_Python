# Queue : FIFO/LILO             eg.  front---> [9,1,2,5,6] <---rear
# Operations : 1. Enqueue-Inserting element (Inserts ele from rear side of queue)
#              2. dequeue-Deleting element (Deletes ele from front side of queue)

# Implementation of Queue using list

# def Enqueue(l):
#     d=eval(input("Enter the element you want to insert :"))
#     l.append(d)
# def Dequeue(l):
#     if len(l)==0:
#         print("Queue is Empty")
#     else:
#         del l[0]
# def Display(l):
#     if len(l)==0:
#         print("Queue is Empty")
#     else:
#         for i in l:
#             print(i,end=" ")
# def main():
#     l=[]
#     while True:
#        print("\nEnter Your Choice : ")
#        choice = eval(input("Press 1 -> Enqueue \nPress 2 -> Dequeue \nPress 3 -> Display \nPress 4 -> Exit\n"))
#        if choice == 1:
#            Enqueue(l)
#            print("\nElement Inserted Successfully")
#        elif choice == 2:
#            Dequeue(l)
#            print("\nElement Removed Successfully")
#        elif choice == 3:
#            Display(l)
#        else:
#            print("\nInvalid choice")
#
# if __name__=='__main__':
#     main()


# Implementation using Linked List

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def Enqueue(self,data):
        if self.front==None and self.rear==None:
            n=Node(data)
            self.front=n
            self.rear=n
        else:
            n1=Node(data)
            self.rear.next=n1
            self.rear=n1
            self.rear.next=None

    def Dequeue(self):
        if self.front==None and self.rear==None:
            print("Queue is Empty")
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None

    def Display(self):
        if self.front==None and self.rear==None:
            print("Queue is Empty")
        else:
            temp=self.front
            print("\nQueue After Operations ")
            while temp:
                print(temp.data,end=" ")
                temp=temp.next

def main():
    q = Queue()
    q.Enqueue(10)
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    q.Display()
    q.Dequeue()
    q.Dequeue()
    q.Display()

if __name__=='__main__':
    main()