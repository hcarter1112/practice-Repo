def login_menu():
    users = {}
    keepGoing = True
    repeat = True
    while repeat:
        status = input("Do you already have an account?? y/n? or 'q' to quit: ")
        if status == "y":
            while keepGoing:
                keepGoing = oldUser(users)
        elif status == "n":
            while keepGoing:
                keepGoing = newUser(users)
                if keepGoing:
                    break
        elif status == "q":
            return "Application Closed"
        else:
            print("Invalid Entry")


def oldUser(users):
    user = input("Username: ")
    psw = input("Password: ")
    if user in users and users[user] == psw:
        print("Login Successful!!")
        return False
    else:
        print("Username or Password is incorrect. Please create an account or log in.")
        return False


def newUser(users):
    print("Please create your new account")
    nuser = input("Username: ").strip()
    if nuser in users:
        print("Username already exists")
        newUser(users)
    else:
        npsw = input("Password: ").strip()
        users[nuser] = npsw
        print("User Created!")
    return True


if __name__ == "__main__":
    login_menu()
