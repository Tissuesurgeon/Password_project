import random
import sqlite3

conn = sqlite3.connect('password_database.db')
c = conn.cursor()

#defining a function to create the table for the database
def table():
  c.execute("""CREATE TABLE data_info (
          Account_name text,
          Password_generated text
      )""")
#data_base = {}
#creating the main programme
def main_element():
  global key

  key = input("Enter the Account name (Public Key): ")
  
  global length
  length = int(input("Enter the length of the password: "))
  
# this part generates the password and stores it in data_base{}
def generator():
  
  
  raw = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*0123654789"
  global password

  password = random.sample(raw,length)
  password = ''.join(password)
  Data_Base = [key,password]
  c.execute("INSERT INTO data_info VALUES(?,?)",Data_Base)

  #data_base.update({key:password})
  #return password

def next_page():
  global next
  next =  input("Do you wish to generate another password? (Yes/No): ")
  global persmission
  persmission = ["Yes","YES","yes"]
  global deny
  deny = ["No","no","NO"]
  

def data():
  c.execute("SELECT * FROM data_info")

  items = c.fetchall()

  print("Accounts" +"\t Generated Password")
  print("_________" +"\t ____________________")

  for item in items:
    print(item[0] + " \t\t" + item[1] )
        

#table()
main_element()

generator()
next_page()

if next in persmission:
    main_element()
    generator()
    next_page()

elif next in deny:
  

    print("Details Below...... ")
    
      
    data()
conn.commit()
conn.close()
