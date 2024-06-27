
def register():
    with open("st.txt", "r") as red:
        username = input("username: ")
        password = input("password: ")
        username == password
        if (username not in red.read()):
            app = open("st.txt", "a")
            print(username and password ,file= app)
            print("success")
        else:
            print("Unavailable")

def login():
    with open("st.txt", "r") as red:
        username = input("Username: ")
        password = input("Password: ")
        if (username and password in red.read()):
            print(f"hello {username} ")
        else:
            print("login failed")

def change():
    with open("st.txt", "r") as red:
        username = input("Username: ")
        password = input("Password: ")
        if (username and password in red.read()):
            changes = input("Ok new password: ")
            password.replace(changes)
            print("Password Changed: ")
        else:
            print("Retigga")




while True:
    user = input("command: ")

    if user == "help":
        print("reg = register\n")
        print("log = login\n")
        print("change = change password\n")

    elif user == "reg":
        register()
    elif user == "log":
        login()
    elif user == "change":
        change()
