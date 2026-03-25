# ~~~~~ HELPER FUNCTIONS AND IMPORTS ~~~~~
def loadList():
    try:
        with open("savedList.txt", "r") as listIn:
            loadedList = listIn.readlines()
            for idx in range(len(loadedList)):
                loadedList[idx] = loadedList[idx].replace("\n", "")
        return loadedList
    except FileNotFoundError:
        return []


def saveList(listIn):
    with open("savedList.txt", "w") as newSave:
        for idx in range(len(listIn)):
            if idx < len(listIn) - 1:
                newSave.write(f"{listIn[idx]}\n")
            else:
                newSave.write(f"{listIn[idx]}")


def addItems(listIn):
    addMore = True
    while addMore:
        printList(listIn)
        print("Enter an item to add (or 'done' to exit)")
        toAdd = input(" --> ")
        if toAdd == "done":
            addMore = False
        else:
            listIn.append(toAdd)
    saveList(listIn)


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
    options = {"1": printList,
               "2": addItems,
               "3": removeItems,
               "4": editItems,
               "5": moveItems}
    
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

        try:
            if toDo == "6":
                appOn = False
            else:
                options[toDo](managedList)
        except KeyError:
            print("")
            print("Invalid option - try again!")
    

    saveList(managedList)



# ~~~~~ MAIN FUNCTION CALL ~~~~~
main()