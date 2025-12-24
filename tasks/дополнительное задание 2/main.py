def main(contacts: dict):
    while 1:
        print("1. add contact")
        print("2. delete contact")
        print("3. show contacts")
        print("4. change number")
        print("5. exit")
        ch = int(input())
        if ch == 1:
            name = input("name: ")
            name = name.lower().capitalize()
            number = input("number: ")
            if number[0] == 7:
                number = "+" + number
            if number[0] == 8:
                number = "+7" + number[1:]
            contacts[name] = number
        if ch == 2:
            name = input("name: ")
            contacts.pop(name.lower().capitalize(), print("DNE"))
        if ch == 3:
            for i in list(contacts.items()):
                print(f"{i[0]} : {i[1]}")
        if ch == 4:
            name = input(name).lower().capitalize()
            if name in list(contacts.keys()):
                number =  input("new number: ")
                if number[0] == 7:
                    number = "+" + number
                if number[0] == 8:
                    number = "+7" + number[1:]
                contacts[name] = number
        if ch == 5:
            return
    
if __name__ == "__main__":
    contacts = {}
    main(contacts)
