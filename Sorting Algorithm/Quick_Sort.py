# Quick Sort
# Time Complexity =  n(log n)

# def Sorting(l,low,high):
#     pivot=l[0]
#     i=low+1
#     j=high
#     while i<=j:
#         while l[i]<pivot and i<=j:
#             i+=1
#         while l[j]>pivot and i<=j:
#             j-=1
#         if i<=j:
#             l[i],l[j]=l[j],l[i]
#     l[low],l[j]=l[j],l[low]
#     return j
# def Quick_sort(l,low,high):
#     if low>high:
#         return
#     j=Sorting(l,low,high)
#     Quick_sort(l,low,j-1)
#     Quick_sort(l,j+1,high)
# l=[5,8,4,3,6,7,1]
# Quick_sort(l,0,len(l)-1)
# print(l)