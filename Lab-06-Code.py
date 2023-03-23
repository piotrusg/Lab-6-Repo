# Patrick Gawienczuk

def encode():
    password = input("Please enter your password to encode: ")
    password = str(password)
    encrypted_pass = ""
    for digit in password:
        encrypted_pass = str(encrypted_pass) + str(((int(digit) + 3) % 10))
    # this takes the user submitted password, and then adds 3 to each digit in the password
    print("Your password has been encoded and stored!")
    print("")
    return encrypted_pass


def decode(encrypted_pass):
    # Emilio Sierra
    decoded_pass = ""
    for digit in encrypted_pass:
        decoded_pass = str(decoded_pass) + str((int(digit) - 3) % 10)
    return decoded_pass

def main():
    # your main code belongs here
    while True:
        menu()
        option = input("Please enter an option: ")
        option = int(option)
        if option == 1:
            encrypted_pass = encode()
            # this takes the password provided by the user, and puts it through the encoder, the result of which is
            # then stored by the program
        if option == 2:
            decoded_pass = decode(encrypted_pass)
            print(f"The encoded password is {encrypted_pass}, and the original password is {decoded_pass}.")
            print("")
            # this puts the encoded password into the decoder provided by Emilio Sierra, and then states the encoded
            # and decoded password to the user
        if option == 3:
            break
            # quits the program

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
# this prints the menu for the user


if __name__ ==  "__main__":
    main()

