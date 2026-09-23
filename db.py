import sqlite3
import os
#Database file lives next to this script, so the app works
#Regardless form which folder you run "python main.py" from.
db_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"jee.db") #the folder in which the code exists
def get_connection():
    # Opens the db file, creating it if it doesn't exist yet
    return sqlite3.connect(db_file)

def init_db():
    #Called once at startup. Creates the Register table
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("""
        create table if not exists Register (
            App_no integer primary key,
            Candidate_name text,
            Mother_name text,
            Father_name text,
            DOB text,
            Category text,
            Gender text,
            Aadhaar text,
            Email text,
            Mobile text,
            Address text,
            City text,
            State text,
            Pincode text,
            Paper text,
            Exam_city text,
            Password_ text
        )
    """)
    conn.commit() #makes the changes permanent
    conn.close()
