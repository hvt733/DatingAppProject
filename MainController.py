from GUI import *

def main():
    status = "none"
    while status != "done":
        start = login.Login()
        start.login_screen()
        user_id = start.get_user_id()
        status = start.get_status()
    user = user_profile.User(user_id, "profile") 
    user.Profile_screen()

if __name__ == "__main__":
    main()