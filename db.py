import sqlite3
import os
from auth import hash_pw
#Database file lives next to this script, so the app works
#Regardless form which folder you run "python main.py" from.
db_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"jee.db") #the folder in which the code exists, this line's main aim is to define a path to the file
def get_connection():
    # Opens the db file, creating it if it doesn't exist yet
    return sqlite3.connect(db_file)

def init_db():
    #Called once at startup. Creates the Register table
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("""create table if not exists Register (App_no integer primary key,Candidate_name text,Mother_name text,Father_name text, DOB text,Category text,Gender text,Aadhaar text,Email text,Mobile text,Address text,City text,State text, Pincode text,Paper text,Exam_city text,Password_ text)""")
    #Predefined records for testing
    set_records=[(10000001, "Aarav Sharma", "Sunita Sharma", "Rajesh Sharma", "2007-03-15", "GEN", "M", "234567890123","aarav.sharma@gmail.com","9876543210", "12 MG Road", "Bhopal","Madhya Pradesh", "462001", "B.Tech", "Bhopal", "Aarav@101"),
                 (10000002, "Priya Verma", "Meena Verma", "Anil Verma", "2006-11-02", "OBC", "F","345678901234", "priya.verma@zoho.com", "9123456780", "45 Civil Lines", "Indore","Madhya Pradesh", "452001", "B.E", "Indore", "Priya@102"),
                 (10000003, "Rohan Meena", "Kavita Meena", "Mahesh Meena", "2007-07-21", "ST", "M","456789012345", "rohan.meena@gmail.com", "9988776655", "8 Station Road", "Jaipur","Rajasthan", "302001", "B.Arch", "Jaipur", "Rohan@103"),
                 (10000004, "Ananya Iyer", "Lakshmi Iyer", "Venkat Iyer", "2006-05-30", "EWS", "F","567890123456", "ananya.iyer@proton.me", "9012345678", "22 Anna Nagar", "Chennai","Tamil Nadu", "600040", "B.Planning", "Chennai", "Ananya@104"),
                 (10000005, "Mohit Jatav", "Rekha Jatav", "Suresh Jatav", "2007-01-09", "SC", "M","678901234567", "mohit.jatav@vitbhopal.ac.in", "8899001122", "5 Gandhi Nagar", "Lucknow","Uttar Pradesh", "226001", "B.Tech", "Lucknow", "Mohit@105"),]
    for record in set_records:
        cur.execute("insert or ignore into Register values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",rec[:16] + (hash_pw(rec[16]),))
    conn.commit() #makes the changes permanent
    conn.close()
