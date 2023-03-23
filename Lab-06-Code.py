# Patrick Gawienczuk

def encode():
    password = input("Please enter your password to encode: ")
    encrypted_pass = int(password) + 33333333
    return encrypted_pass
def main():
    # your main code belongs here
    menu()
    option = input("Please enter an option: ")
    if option == 1:
        encrypted_pass = encode()
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

if __name__ ==  "__main__":
    main()



