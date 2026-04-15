def Insertion_Sort(x):
    for i in range(1,len(x)):
        j=i
        while x[j-1]>x[j] and j>0:
            x[j-1],x[j]=x[j],x[j-1]
            j-=1
            print(f"After iteration :",x)
    print("Final result : ",x)
a=[3,6,2,8,1]
Insertion_Sort(a)