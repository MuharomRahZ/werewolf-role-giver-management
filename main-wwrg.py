
def mainMenu():
    try:
        print(f"WELCOME TO WEREWOLF ROLE GIVER MANAGEMENT")
        print(f"This program will help you manage your roles")
        print(f"---CHOOSE MENU---\n1. MANAGE PLAYERS\n2. MANAGE ROLES\n3. ASSIGN ROLES TO PLAYERS\n4. EXIT")
        menu = int(input("Enter your choice: "))
        opsiMainMenu(menu)
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

def opsiMainMenu(menu):
    if menu == 1:
        managePlayers()
    elif menu == 2:
        manageRoles()
    elif menu == 3:
        assignRoles()
    elif menu == 4:
        exit()
    else:
        print("Invalid choice!\n")
        mainMenu()

def managePlayers():
    print()
    # try:
    #     print(f"---MANAGE PLAYERS---\n1. ADD PLAYER\n2. REMOVE PLAYER\n3. VIEW PLAYERS\n4. BACK")
    #     menu = int(input("Enter your choice: "))
    #     opsiManagePlayers(menu)
    # except Exception as exception:
    #     print("Error: %s!\n\n" % exception)

def manageRoles():
    print()
    # try:
    #     print(f"---MANAGE ROLES---\n1. ADD ROLE\n2. REMOVE ROLE\n3. VIEW ROLES\n4. BACK")
    #     menu = int(input("Enter your choice: "))
    #     opsiManageRoles(menu)
    # except Exception as exception:
    #     print("Error: %s!\n\n" % exception)

def assignRoles():
    print()
    # try:
    #     print(f"---ASSIGN ROLES TO PLAYERS---\n1. ASSIGN ROLES\n2. BACK")
    #     menu = int(input("Enter your choice: "))
    #     opsiAssignRoles(menu)
    # except Exception as exception:
    #     print("Error: %s!\n\n" % exception)