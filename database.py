import sqlite3 as sql

# email TEXT

def create_emails():
    #Create database file/connect to it
    conn = sql.connect("emails.db")

    #Create table
    conn.execute("""CREATE TABLE emails (email TEXT)""")

    print("table created")

    conn.close()

def new_email(email): #Pass in an array of info (email, interest) like this

    #Connect to database
    conn = sql.connect("emails.db")
    cur = conn.cursor()

    #Load all rows
    insert_query = """INSERT INTO emails (email) VALUES (?)"""
    cur.execute(insert_query, (email,))

    #Save changes
    conn.commit()

    conn.close()

    print("Loading completed")

# ---- DEBUGGING ---------
def list_emails(): 
    conn = sql.connect("emails.db")
    cur = conn.cursor()

    cur.execute("select * from emails")
    
    rows = list(cur.fetchall())

    conn.close()

    emails = []

    for i in rows:
        emails.append(i[0])

    return emails

def create_new_emails():
    create_emails()
    
    print(list_emails())
# -------------------------


