# A stack is a linear data structure that stores items in a  
# First-In/Last-Out (FILO) 

stack = []

n =int(input("Enter the no of elements "))
for i in range(0,n):
    element=int(input())
    stack.append(element)

print("Inital stack",stack)

print(stack.pop())

print("stack after popping" , stack)

print("size of stack is ", stack.size())



# stack.append('a')
# stack.append('b')
# stack.append('c')

# print('Initial stack')
# print(stack)

# print('\nElements popped from stack:')
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# print('\nStack after elements are popped:')
# print(stack)


