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
    print("3. Pop first itma on the list")
    print("########################################")
    print("")
    print("")
    enteredChoice = int(input("Enter what you want to do: "))
    print("")
    print("")

    if enteredChoice == 1:
        viewList()

    if enteredChoice == 2:
        toInsert = raw_input("Enter the sentence you want to insert: ")
        push(toPush = toInsert)
        
    if enteredChoice == 3:
        pop()
    
