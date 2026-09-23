import random
from db import get_connection
from auth import check_pw, hash_pw

def records():
    #Admin-only view: requires a fixed password before listing all candidates.
    #Stored as a hash (like candidate passwords) rather than in plaintext.
    admin_password= hash_pw("VITBhopal@123")
    pw =input("Enter Admin Password To View All Records: ")
    if hash_pw(pw) != admin_password:
        print("Incorrect Password! Access Denied.")
        return
    #Deliberately leaves Password_ out of the SELECT so hashes are never listed.
    conn =get_connection()
    cur =conn.cursor()
    cur.execute("""
        select App_no, Candidate_name, Mother_name, Father_name, Category,
               Gender, Aadhaar, Email, Mobile, Address, City, State,
               Pincode, Paper, Exam_city
        from Register
    """)
    rows =cur.fetchall()
    conn.close()

    if not rows:
        print("No records found.")
        return
    for row in rows:
        print(row)


def search():
    while True:
        app_input =input("Enter Application Number: ")
        if app_input.isdigit():
            ind_record =int(app_input)
            break
        print("Digits only!")

    pw =input("Enter Password: ")

    conn = get_connection()
    cur =conn.cursor()
    cur.execute("select * from Register where App_no=?", (ind_record,))
    row =cur.fetchone()
    conn.close()

    if row and check_pw(pw, row[16]):
        print(row[:16])
    else:
        print("Incorrect Application No. or Password")


def login():
    print("\n--- LOGIN TO VIEW YOUR EXAM DETAILS ---")
    while True:
        app= input("Enter Application Number: ")
        if app.isdigit():
            app =int(app)
            break
        print("Digits only!")

    pw =input("Please Enter Your Password: ")

    conn =get_connection()
    cur =conn.cursor()
    cur.execute("select * from Register where App_no=?", (app,))
    x =cur.fetchone()
    conn.close()

    if x and check_pw(pw,x[16]):
        # prints selected fields with labels, plus made-up exam logistics
        print("\nLogin Successful!")
        print("\n--- YOUR JEE EXAM DETAILS ---")
        print("Application Number:",x[0])
        print("Candidate Name:",x[1])
        print("Mother's Name:",x[2])
        print("Father's Name:",x[3])
        print("DOB:",x[4])
        print("Category:",x[5])
        print("Gender:",x[6])
        print("Email:",x[8])
        print("Mobile:",x[9])
        print("Address:",x[10])
        print("City:",x[11])
        print("State:",x[12])
        print("Pincode",x[13])
        print("Exam Paper:",x[14])
        print("Exam City:",x[15])
        print("Exam Date: 2025-12-24 (Shift 1)")
        print("Reporting Time: 2:00 PM")
        print("Closing Time: 3:00 PM\n")
        bp =random.randint(1,25)
        print("Center Name: NTA JEE EXAMINATION CENTER ->",bp,"iON digital zone",x[15])
    else:
        print("Invalid Login!")
