# ~~~~~ HELPER FUNCTIONS AND IMPORTS ~~~~~
def loadList():
    return []


def saveList(listIn):
    pass


def addItems(listIn):
    print("\nFunctionality coming soon!")


def removeItems(listIn):
    print("\nFunctionality coming soon!")


def editItems(listIn):
    print("\nFunctionality coming soon!")


def moveItems(listIn):
    print("\nFunctionality coming soon!")        


def printList(listIn):
    if len(listIn) > 0:
        print("\n~~~ LIST ~~~")
        for idx in range(len(listIn)):
            print(f"{idx+1}. {listIn[idx]}")
        print("")
    else:
        print("\nThe list is empty!")


# ~~~~~ MAIN FUNCTION DEFINITION ~~~~~
def main():
    appOn = True
    print("Welcome to the List Manager!")
    while appOn:
        managedList = loadList()
        print("")
        print(" ~~~ Choose an Option Below ~~~")
        print("1. View List")
        print("2. Add Items to List")
        print("3. Remove Items from List")
        print("4. Edit Items on List")
        print("5. Move Items on List")
        print("6. Exit")
        toDo = input(" --> ")
        if toDo == "1":
            printList(managedList)
        elif toDo == "2":
            addItems(managedList)
        elif toDo == "3":
            removeItems(managedList)
        elif toDo == "4":
            editItems(managedList)
        elif toDo == "5":
            moveItems(managedList)
        elif toDo == "6":
            appOn = False
        else:
            print("Invalid option - try again!")
    

    saveList(managedList)



# ~~~~~ MAIN FUNCTION CALL ~~~~~
main()