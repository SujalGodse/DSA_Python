stack=list()

def Push(data):
    if len(stack)==0:
        stack.append(data)
    else:
        stack.insert(0,data)

def Pop():
    if len(stack)==0:
        print("--- Stack is Empty ---")
    else:
        stack.pop(0)
        print(f"Deleted successfully")

def Display():
    if len(stack)==0:
        print("--- Stack is Empty ---")
    else:
        for i in stack:
            print(i,end="")

while True:
    print("Choose the Option you want to perform : ")
    inp=eval(input("Press 1-> Inserting the Element, Press 2-> Deleting the Element, Press 3-> Display the Element : "))
    if inp==1:
        data=eval(input("Enter the data to be inserted : "))
        Push(data)
        print(f"{data} inserted successfully")
    elif inp==2:
        Pop()
    elif inp==3:
        Display()
        print(f"Displayed successfully")

