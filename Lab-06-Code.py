# Patrick Gawienczuk

def encode():
    password = input("Please enter your password to encode: ")
    encrypted_pass = int(password) + 33333333
    print("Your password has been encoded and stored!")
    print("")
    return encrypted_pass




def main():
    # your main code belongs here
    while True:
        menu()
        option = input("Please enter an option: ")
        option = int(option)
        if option == 1:
            encrypted_pass = encode()
        if option == 2:
            decoded_pass = decode(encrypted_pass)
            print(f"The encoded password is {encrypted_pass}, and the original password is {decoded_pass}.")
            print("")
        if option == 3:
            break

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")

if __name__ ==  "__main__":
    main()


