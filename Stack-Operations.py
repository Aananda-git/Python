# implementation of stack in python 
# creating a stack
stack=[]

# push function
def push_func(stack):

    def append(stack, items):
        stack.append(items)
        print("Inserted items: ", items)

    # initalizing number of data to be inserted
    print("Enter the number of data to be inserted: ")
    global n 
    n = int(input())

    print("Enter the items to be inserted into the stack: ")
    for i in range(n):
        items = str(input())
        append(stack,items)
    print("\nItems in Stack: ",stack)

# pop function

def pop_func(stack):
    if(len(stack) == 0):
        print("The stack is empty. Nothing to Pop!")
    else:
        print("Popped item is: ",stack.pop())
            
def tos(stack):
    if(len(stack) == 0):
        print("The stack is empty. No Top of the stack")
    else:
        print("The top of the stack is: ", stack[-1]) 

while True:
    print("........STACK OPERATIONS..........")
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.isEmpty")
    print("5.isFull")
    print("6.EXIT")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        push_func(stack)
    if choice == 2:
        pop_func(stack)
    if choice == 3:
        tos(stack)
    if choice == 4:
        if(len(stack) == 0):
            print("The Stack is empty.") 
        else:
            print("The Stack is not empty.")
    if choice == 5:
        if len(stack) == n:
            print("The stack is full.")
        else:
            print("The stack is not full.")
    elif choice == 6:
        break