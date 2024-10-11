def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact added'

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return 'Contact updated.' 

def show_phone(args, contacts):
    name = args[0]
    if not contacts:
        return('Contact list is empty')
    else:
        if name in contacts:
            phone = contacts[name]
            return f'Phone number for contact "{name}": {phone}'
        else:
            return('The contact was not found')

def show_all(contacts):
    if not contacts:
        return('Contact list is empty')
    else:
        return(f'Here are all your contacts: {contacts}')

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command == 'close' or command == 'exit':
            print('Good bye!')
            break
        elif command == 'hello':
            print("Hello, how can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == '__main__':
    main()