from db import init_db
from registration import register, update, delete
from view import records, search, login

def main():
    #init_db() runs once before the loop starts, so the table always exists.
    init_db()
    while True:
        #main menu
        print("\n--- JEE REGISTRATION SYSTEM ---")
        print("New Registration (1)")
        print("All Records (2)")
        print("Search Candidate (3)")
        print("Update Record (4)")
        print("Delete Candidate (5)")
        print("Login To View Your Details (6)")
        print("Exit (7)")
        print()

        try:
            hello = int(input("Please Enter Your Choice: "))
        except ValueError:
            print("Sorry! Invalid Choice")
            continue

        if hello==1:
            register()
        elif hello==2:
            records()
        elif hello==3:
            search()
        elif hello==4:
            update()
        elif hello==5:
            delete()
        elif hello==6:
            login()
        elif hello==7:
            break
        else:
            print("Sorry! Invalid Choice")
main()
