print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
user_input = int(input('Please enter an option: '))


if user_input == 1:
    password = input('Please enter your password to encode: ')
    password1 = ''

    for char in password:
        new_digit = int(char) + 3
        if new_digit >= 10:
            new_digit -= 10
        else:
            pass
        password1 = password1 + str(new_digit)
    print(password1)

elif user_input == 2:
    pass

else:
    pass