import mysql.connector
myconn=mysql.connector.connect(host="localhost",user="root",password="",database="adc")
mycur=myconn.cursor()

def insert(details):
    global mycur
    query="insert into faculty (name,empid,phno,email)values(%s,%s,%s,%s)"
    mycur.execute(query,details)
    myconn.commit()
def view():
    pass
def delete():
    pass
def update():
    pass


while True:
    ch=int(input("1.insert 2.display 3.delete 4.update 5.exit"))
    if ch==1:
        name=input("Enter name")
        empid=input("Enter empid")
        phno=input("Enter Phno")
        email=input("Enter email")
        details=[name,empid,phno,email]
        insert(details)#fun call
        
    
    









