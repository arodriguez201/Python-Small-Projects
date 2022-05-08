import json

# Reads our Text file
with open('login_data.txt', 'r') as login_file:
    try:
        users = json.load(login_file)
    except:
        users = {}


def main():
    x = True
    # Starts the loop
    while x:
        verification = input('Are you an existing customer or a brand new one? (E/N)  or (q, Q to Quit): ')
        if verification == 'E':
            existing_customer()
        elif verification == 'N':
            new_customer()
        # Quits the program
        elif verification == 'q' or verification == 'Q':
            # Writes new data given
            with open("login_data.txt", "w") as login_file:
                login_file.write(json.dumps(users))
            # Ends the loop
            x = False
        else:
            main()


def existing_customer():
    existing_username = input('Enter your username: ')
    existing_password = input('Enter your password: ')

    if existing_username in users and users[existing_username] == existing_password:
        print('Your login is successful.')

    else:
        print('Your login in unsuccessful. ')


def new_customer():
    create_account = input('Enter your username: ')
    if create_account in users:
        print('The name already exists.')
    else:
        create_password = input('Create your password: ')
        users[create_account] = create_password
        print('Welcome to the club!')


main()
