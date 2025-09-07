Storage = []

def add_friends():
    user_input = input("Enter a friends name!:").strip().title()
    if user_input:
        Storage.append(user_input)
        print(F"Your friend {user_input} has been added to the list!")
    

def remove_friend():
    user_input = input("Enter a name you would like to remove.:").strip().title()
    if user_input in Storage:
        Storage.remove(user_input)
        print(F"Your friend {user_input} has been removed from the list.")
    else:
        print("Couldn't find the user",user_input)


def view_list():
    print("--Invite list--")
    print(Storage) # can change format.


def wipe_whole_list():
    user_input = input("Enter Y to wipe the list and N to not:").upper().strip()
    if user_input.upper() == "Y":
        Storage.clear()
        print("List Successfully deleted.")
    else: 
        print("List has been spared.")

while True:
        try:
                print("--Menu--")
                print("1. Add friend.")
                print("2. Remove friend.")
                print("3. View invite list.")
                print("4. Wipe list.")
                print("5. Exit")

                user_input = int(input("Enter a number from 1-5:"))

                match user_input:
                    case 1:
                        add_friends()
                    case 2:
                        remove_friend()
                    case 3:
                        view_list()
                    case 4:
                        wipe_whole_list()
                    case 5:
                        print("Thank you for using this program!")
                        break
                    case _:
                        print("Invaild, please type number from 1-5")
        except ValueError:
            print("Invaild, please type a whole number!")
