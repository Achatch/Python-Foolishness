passwordsArray = ['123456', '123456789', 'qwerty', '12345678', '111111', '1234567890', '1234567', 'password', '123123',
                  '987654321']  # List of the top 10 most common passwords found here:https://techviral.net/common-passwords-might-surprise/

''' Password checker, loops through the array checking each value against the user password
    Returns false if password is in array, true if not'''
def PasswordChecker(userPassword):
    for password in passwordsArray:
        if password == userPassword:
            print('Password is too common, please enter another password')
            return False
    return True


''' Main; calls PasswordChecker against user input, exits if PasswordChecker returns true.'''
if __name__ == '__main__':
    print('Please enter your password')
    userPassword = input()
    while not PasswordChecker(userPassword):
        userPassword = input()
    if PasswordChecker(userPassword):
        print('Password is accepted')
        exit()
