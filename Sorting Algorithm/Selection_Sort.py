def Selection_Sort(x):
    for i in range(len(x)-1):
        minpos=i
        for j in range(i,len(x)):
            if x[j]<x[minpos]:
                minpos=j
        x[i],x[minpos]=x[minpos],x[i]
        print(f"After iteration {i} : ",x)
    print(f"Final result : ",x)

a=[5,6,3,8,1]
Selection_Sort(a)
