#List Comprehention
# x=[1,3,7,8,9,10,11]
# a=[]
# for i in x:
#     if i%2==0:
#         a.append(i**2)
#     else:
#         a.append(i**3)
# print(a)
#
# print([i**2 if i%2==0 else i**3 for i in x])

#Dictionary Comprehention
# x=["python","java","sql","pen","copy","no"]
# d={}
# for i in x:
#     if len(i)%2==0:
#         d[i]=i[::-1]
#     else:
#         d[i]=[i]
# print(d)
#
# print({i:i[::-1] if len(i)%2==0 else [i] for i in x})