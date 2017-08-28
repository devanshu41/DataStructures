queue = ["wake up","take a shower","get dressed","breakfast","Go to Office"]

def viewList():
    for x in range(len(queue)):
        print(queue[x])

def push(toPush):
    queue.append(toPush)

def pop():
    popedItem = queue.pop(0)
    print("The removed item is: ", popedItem)

while True:

    print("")
    print("Python basic queue implementation")
    print("########################################")
    print("1. View list")
    print("2. Insert into the list")
    print("If you add any item the code will insert an item in the bottom of the array and will pop off the first item.")
    print("########################################")
    print("")
    print("")
    enteredChoice = int(input("Enter what you want to do: "))
    print("")
    print("")

    if enteredChoice == 1:
        viewList()

    elif enteredChoice == 2:
        toInsert = raw_input("Enter the sentence you want to insert: ")
        push(toPush = toInsert)
        pop()
    else:
        print("Not a valid choice.")
