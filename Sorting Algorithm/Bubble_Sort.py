x=[23,5,7,2,10]
for i in range(len(x)):
    for j in range(0,len(x)-i-1):
        if x[j]>x[j+1]:
            x[j],x[j+1]=x[j+1],x[j]
    print(f"After iteration {i+1} : ",x)
print("Final result : ",x)


