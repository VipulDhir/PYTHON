#BUBBLE SORT this algorithm repeatedly compares two adjacent elements 
#arr=[]
# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    arr.append(l)
# print(arr)

# arr=[3,5,7,2,1,4]
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]>arr[j]:
#             a =arr[i]
#             arr[i]=arr[j]
#             arr[j]=a
# print(arr) 

# arr=[]
# def bubblesort(arr):
#     for i in range(0,len(arr)):#
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
                # a =arr[i]
                # arr[i]=arr[j]
                # arr[j]=a

# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    arr.append(l)

# bubblesort(arr)

# print(arr)


#Selection Sort 
#This algorithm finds the minimum element and places it in order

# arr=[3,5,7,2,1,4]
# def selectionsort(arr):
#     for i in range(0,len(arr)):
#         min=i
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[min]:
#                 min=j

#         arr[i], arr[min] =arr[min], arr[i]

# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#    l=int(input())
#    arr.append(l)

# selectionsort(arr)
# print(arr)

#-----------------------------------------
# QUICK SORT

# arr= [4,3,2,7,5,1,6] 
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr 
    
#     pivot_element = arr[len(arr)-1]

#     left = []
#     right = []

#     for i in range (0,len(arr)-1):
#         if arr[i] < pivot_element:
#             left.append(arr[i])
#         else:
#             right.append(arr[i])
    
#     return quick_sort(left) + [pivot_element] + quick_sort(right)

# sorted = quick_sort(arr)
# print(sorted)
# -----------------------------------------------------------------------------


# Python Program for Binary Search

# arr=[]
# def binary_search(arr,low,high,x):
    
#     if high>=low:
#         mid=(low+high)//2

#         if arr[mid]==x:
#             print("element found at index ")
#             return mid
#         elif x > arr[mid]:
#             return binary_search(arr,mid+1,high,x)
#         else:
#             return binary_search(arr,low,mid-1,x)
    
#     else:
#         print("element not found")
#         return -1

# n=int(input("Number of elements in array:"))
# for i in range(0,n):
#     l=int(input())
#     arr.append(l)

# x=int(input("Print element to be found"))

# ans=binary_search(arr,0,len(arr)-1,x)
# print(ans)


# COUNT SORT


