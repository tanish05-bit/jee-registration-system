import random
from db import get_connection
from auth import hash_pw, check_pw
from validators import (valid_dob, valid_category, valid_gender, valid_aadhaar,valid_email, valid_mobile, valid_pincode, valid_paper)

def generate_app_no(cur):
    #Keep generating random 8-digit numbers until we find
    #one that's not already used (App_no is the primary key).
    while True:
        app_no=random.randint(10000000, 99999999)
        cur.execute("select App_no from Register where App_no=?",(app_no,))
        if cur.fetchone() is None:
            return app_no

def register():
    #Collects all candidate fields, validating each one before moving on.
    conn=get_connection()
    cur=conn.cursor()

    print("Your Application Number is Computer Generated")
    a=generate_app_no(cur)
    print("Your Application Number is:", a)

    b=input("Candidate's Name: ")
    c=input("Mother's Name: ")
    d=input("Father's Name: ")

    while True:
        e=input("DOB(YYYY-MM-DD): ")
        if valid_dob(e):
            break
        print("Enter DOB in correct format YYYY-MM-DD")

    while True:
        f=input("Category (GEN/OBC/SC/ST/EWS): ").upper()
        if valid_category(f):
            break
        print("Invalid category. Choose GEN/OBC/SC/ST/EWS")

    while True:
        g= input("Gender (M/F/T): ").upper()
        if valid_gender(g):
            break
        print("Invalid gender. Enter M,F or T")

    while True:
        h=input("Aadhaar Number: ")
        if valid_aadhaar(h):
            break
        print("Aadhaar must be 12 digits")

    while True:
        i=input("Email: ")
        if valid_email(i):
            break
        print("Email must contain @gmail.com/@zoho.com")

    while True:
        j=input("Mobile: ")
        if valid_mobile(j):
            break
        print("Mobile must be 10 digits")

    k =input("Address: ")
    l =input("City: ")
    m =input("State: ")

    while True:
        n = input("Pincode: ")
        if valid_pincode(n):
            break
        print("Pincode must be 6 digits")

    while True:
        o = input("Paper (B.E/B.Tech/B.Arch/B.Planning): ")
        if valid_paper(o):
            break
        print("Choose from B.E / B.Tech / B.Arch / B.Planning")

    p =input("Preferred Examination City: ")
    pw =input("Create Password: ")
    hashed =hash_pw(pw)

    try:
        #iMPORTANT NOTE_ --> ? placeholders keep this safe from SQL injection
        cur.execute("insert into Register values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, hashed))
        conn.commit()
        print("Congratulations! Registration Successful")
        print("Your Application Number is -->", a)
        print("Your Password is -->",pw)
    except Exception as err:
        print("Registration failed, please try again. Error:",err)
    finally:
        conn.close() #always release the connection, even on failure


def update():
    #Requires Application number + password before allowing any edit 
    #acts as a simple ownership check.
    conn=get_connection()
    cur=conn.cursor()

    while True:
        app_input=input("Enter Your Application Number: ")
        if app_input.isdigit():
            jk=int(app_input)
            break
        print("Digits only!")

    pw =input("Enter Password: ")
    cur.execute("select * from Register where App_no=?", (jk,))
    row = cur.fetchone()

    if not row or not check_pw(pw, row[16]):
        print("Invalid Application No. or Password")
        conn.close()
        return

    print("Candidate's Name (1)")
    print("Mother's Name (2)")
    print("Father's Name (3)")
    print("DOB (4)")
    print("Category (5)")
    print("Gender (6)")
    print("Aadhaar Number (7)")
    print("Email (8)")
    print("Mobile (9)")
    print("Address (10)")
    print("City (11)")
    print("State (12)")
    print("Pincode (13)")
    print("Exam Paper (14)")
    print("Exam City (15)")
    print("Password (16)")

    try:
        op = int(input("Choice: "))
    except ValueError:
        print("Sorry! Invalid Choice")
        conn.close()
        return

    if op==1:
        mn = input("New Candidate's Name: ")
        cur.execute("update Register set Candidate_name=? where App_no=?",(mn,jk))
    elif op==2:
        mn=input("New Mother's Name: ")
        cur.execute("update Register set Mother_name=? where App_no=?",(mn,jk))
    elif op==3:
        mn=input("New Father's Name: ")
        cur.execute("update Register set Father_name=? where App_no=?",(mn,jk))
    elif op==4:
        while True:
            mn=input("New DOB (YYYY-MM-DD): ")
            if valid_dob(mn):
                break
            print("Invalid DOB format")
        cur.execute("update Register set DOB=? where App_no=?",(mn,jk))
    elif op==5:
        while True:
            mn = input("New Category: ").upper()
            if valid_category(mn):
                break
            print("Invalid category")
        cur.execute("update Register set Category=? where App_no=?",(mn,jk))
    elif op== 6:
        while True:
            mn=input("New Gender: ").upper()
            if valid_gender(mn):
                break
            print("Invalid gender")
        cur.execute("update Register set Gender=? where App_no=?",(mn,jk))
    elif op==7:
        while True:
            mn=input("New Aadhaar Number: ")
            if valid_aadhaar(mn):
                break
            print("Aadhaar must be 12 digits")
        cur.execute("update Register set Aadhaar=? where App_no=?",(mn,jk))
    elif op==8:
        while True:
            mn=input("New Email: ")
            if valid_email(mn):
                break
            print("Email must contain @gmail.com/@zoho.com")
        cur.execute("update Register set Email=? where App_no=?",(mn,jk))
    elif op==9:
        while True:
            mn=input("New Mobile: ")
            if valid_mobile(mn):
                break
            print("Mobile must be 10 digits")
        cur.execute("update Register set Mobile=? where App_no=?",(mn,jk))
    elif op==10:
        mn=input("New Address: ")
        cur.execute("update Register set Address=? where App_no=?",(mn,jk))
    elif op==11:
        mn = input("New City: ")
        cur.execute("update Register set City=? where App_no=?",(mn,jk))
    elif op==12:
        mn=input("New State: ")
        cur.execute("update Register set State=? where App_no=?",(mn,jk))
    elif op==13:
        while True:
            mn=input("New Pincode: ")
            if valid_pincode(mn):
                break
            print("Pincode must be 6 digits")
        cur.execute("update Register set Pincode=? where App_no=?",(mn,jk))
    elif op==14:
        while True:
            mn=input("New Exam Paper: ")
            if valid_paper(mn):
                break
            print("Choose from B.E / B.Tech / B.Arch / B.Planning")
        cur.execute("update Register set Paper=? where App_no=?",(mn,jk))
    elif op==15:
        mn=input("New Exam City: ")
        cur.execute("update Register set Exam_city=? where App_no=?",(mn,jk))
    elif op==16:
        mn=input("New Password: ")
        cur.execute("update Register set Password_=? where App_no=?",(hash_pw(mn),jk))
    else:
        print("Sorry! Invalid Choice")
        conn.close()
        return
    
    conn.commit()
    conn.close()
    print("Updated Successfully")

def delete():
    # Application number and password are both checked directly in the SQL WHERE clause.
    conn=get_connection()
    cur=conn.cursor()

    while True:
        del_record=input("Enter Application Number To Delete: ")
        if del_record.isdigit():
            del_record=int(del_record)
            break
        print("Digits only!")

    pw=input("Enter Password: ")
    cur.execute("select * from Register where App_no=? and Password_=?",(del_record, hash_pw(pw)))
    check = cur.fetchone()

    if check:
        cur.execute("delete from Register where App_no=?",(del_record,))
        conn.commit()
        print("Record Deleted Successfully.")
    else:
        print("Invalid Deletion. DELETION DENIED.")
    conn.close()
