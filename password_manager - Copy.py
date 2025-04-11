from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)





def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fr = Fernet(key)


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(f"{name}|{fr.encrypt(password.encode()).decode()}\n")


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print(
                f"User: {name}, Password: {fr.decrypt(password.encode()).decode()}")


while True:
    mode = input(
        "Whould you like to add or view passwords, press q to quit? (add, view): ")

    if mode == "q":
        break

    elif mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Invalid Mode!")
        continue
