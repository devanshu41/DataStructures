class queue_class():
    def __init__(self):
        self.a_queue = ["wake up","take a shower","get dressed","breakfast","Go to Office"]
    def viewList(self):
        for x in range(len(self.a_queue)):
            print(self.a_queue[x])

    def push(self, toPush):
        self.a_queue.append(toPush)

    def pop(self):
        popedItem = self.a_queue.pop(0)
        print("The removed item is: ", popedItem)

queue = queue_class()

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
        queue.viewList()

    elif enteredChoice == 2:
        toInsert = raw_input("Enter the sentence you want to insert: ")
        queue.push(toPush = toInsert)
        queue.pop()
    else:
        print("Not a valid choice.")
