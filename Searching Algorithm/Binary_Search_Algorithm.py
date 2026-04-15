#1
# l=[3,5,9,15,17]
# key=15
# def binary_search(l,key):
#     li=0
#     hi=len(l)-1
#     while li<=hi:
#         mid=(li+hi)//2
#         if key==l[mid]:
#             return mid
#         elif key>=l[mid]:
#             li=mid+1
#         elif key<=l[mid]:
#             hi=mid-1
# print(binary_search([3,5,9,15,17],15))


#2
# x=[1,3,7,8,9,10,11]
# key=10
# def binary_search(x,key):
#      li=0
#      hi=len(x)-1
#      while li<=hi:
#         mid=(li + hi) // 2
#         if key==x[mid]:
#             return mid
#         elif key>=x[mid]:
#             li=mid+1
#         elif key<=x[mid]:
#             hi=mid-1
# print(binary_search([1,3,7,8,9,10,11],10))