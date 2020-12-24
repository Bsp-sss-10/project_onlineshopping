import random
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="shivan",
  password="shivan999",
  database="shopping",
)
cur = mydb.cursor(buffered=True)

choice="Enter your Choice: "

def llog():
    print("")

llog.login_id=""
llog.password_id=""
llog.username=""
llog.name="User"

def invalid():
    print("---------------------------------------")
    print("Please Select Valid Option")
    print("---------------------------------------")
    
def home():
    print("---------------------------------------")
    print("             ONLINE SHOPPING           ")    
    print("---------------------------------------")
    if llog.login_id != "":
        print("Welcome", llog.name)
        print("---------------------------------------")
    else:
        print("---------------------------------------")
        print("[1] LOGIN")
    if llog.login_id == "":    
        print("[2] CREATE NEW ACCOUNT")

    if llog.login_id != "":
        print("[3] YOUR ORDERS")
        
    print("[4] SEARCH ITEMS")
        
    print("[5] VIEW ALL ITEMS")
    if llog.login_id != "":
        print("[6] LOGOUT")
    print("---------------------------------------")
    screen_opt= input(choice)
    if screen_opt == '1':
        if llog.login_id == "":
            login()
        else:
            invalid()
            home()
    elif screen_opt == '2':
        if llog.login_id == "":
            register()
        else:
            invalid()
            home()
    elif screen_opt == '4':
        search()
    elif screen_opt == '3':
        if llog.login_id != "":
            order()
        else:
            invalid()
            home()
    elif screen_opt == '5':
        items()
    elif screen_opt == '6':
        if llog.login_id != "":
            logout()
        else:
            invalid()
            home()
    else:
        invalid()
        home()

def logout():
    llog.login_id=""
    llog.password_id=""
    llog.username=""
    llog.name="User"
    print("---------------------------------------")
    print("Logout Successfully !")
    print("---------------------------------------")
    home()

def login():
    print("---------------------------------------")
    print("                LOGIN                  ")    
    print("---------------------------------------")
    llog.login_id1=input("Enter Your Email Address: ")
    llog.login_id2=llog.login_id1.lower()
    log_let = len(llog.login_id)
    log_index= log_let - 1
    log_verify=0
    for i in llog.login_id2:
        if i == "@":
            log_verify=1
    if log_verify == 0 or llog.login_id2[log_index] == "@":
        print("Please Enter Valid Email")
        log_cre()    
    cur.execute("SELECT * FROM login")
    for x in cur:
        c=str(x[1])
        if c == llog.login_id2:
            log_passwo=input("Enter your Password: ")
            if x[3] == log_passwo:
                llog.login_id=x[1]
                llog.password_id=x[3]
                llog.username=x[2]
                llog.name=x[0]
                print("---------------------------------------")
                print("Loggined Succesfully !!")
                print("---------------------------------------")
                home()
            else:
                print("---------------------------------------")
                print("Incorrect Password")
                print("Please Re enter Password and email")
                print("---------------------------------------")
                login()
            break;
        else:
            llog.login_id=""
            print("Your Email not registered")
            print("Please Register First!!")
            home()
          
def register():
    llog.name1=input("Enter Your Name: ")
    llog.name=llog.name1.lower()
    usern()
    log_cre()
    pass_cre()
    print("---------------------------------------")
    print("successfully Login in and Registered!!")
    print("---------------------------------------")
    update_login()
    home()

def log_cre():
    llog.login_id1=input("Enter Your Email Address: ")
    llog.login_id=llog.login_id1.lower()
    log_let = len(llog.login_id)
    log_index= log_let - 1
    log_verify=0
    for i in llog.login_id:
        if i == "@":
            log_verify=1
    if log_verify == 0 or llog.login_id[log_index] == "@":
        print("Please Enter Valid Email")
        log_cre()
    cur.execute("SELECT * FROM login")
    for x in cur:
        c=str(x[1])
        if c == llog.login_id:
            print("---------------------------------------")
            print("Email Already Registered !!")
            print("Please Login from Here")
            print("---------------------------------------")
            login()
            break;
        
def pass_cre():
    llog.password_id=input("Create Your Password (Atleast 5 Letters): ")
    pass_verify= len(llog.password_id)
    if pass_verify < 4:
        print("Please Create Password greater than 5 letters")
        pass_cre()

def usern():
    cur.execute("SELECT * FROM login")
    llog.username1=input("Create your Username: ")
    llog.username=llog.username1.lower()
    for x in cur:
        if x[2] == llog.username:
            print("Username Already Used Please Retry!!")
            usern()

    
def search():
    print("")

def order():
    print("")

def items():
    print("")

def paymentopts():
    print("Select Payment Method")
    print("[1] UPI")
    print("[2] Debit Card / Credit Card")
    print("[3] Cash On Delivery")
    print("[4] Go back to Home")

    payment_method = "none"
    pay_opt = input(choice)
    if pay_opt == '1':
        paymentopts.payment_method = "UPI"
        upi()
    elif pay_opt == '2':
        paymentopts.payment_method = "Debit Card / Credit Card"
        card_num()
    elif pay_opt == '3':
        paymentopts.payment_method = "Cash on Delivery"
        order_placed()
    elif pay_opt == '4':
        home()
    else:
        invalid()
        paymentopts()

def card_num():
    card_no = int(input("Enter 16 Digit Card Number: "))
    card_verify = card_no / 10**15
    if card_verify < 10 and card_verify >= 1:
        card_month()        
    else:
        print("Please re enter Correct Card Details")
        card_num()
    
def card_month():
    card_mon = int(input("Enter Expiry Month in MM format: "))
    if card_mon < 13 and card_mon != 0:
        card_year()        
    else:
        print("Please re enter Correct Expiry Month")
        card_month()

def card_year():
    card_yr = int(input("Enter Expiry Year in YY format: "))
    if card_yr >= 21:
        card_cvv()
    else:
        print("Please re enter Correct Expiry Year")
        card_year()

def card_cvv():
    card_cv = int(input("Enter 3/4 Digit Card CVV: "))
    card_verify = card_cv / 10**2
    if card_verify < 100 and card_verify >= 1:
        order_placed()        
    else:
        print("Please re enter Correct CVV")
        card_cvv()

def upi():
    upi_id = input("Enter Your UPI id: ")
    upi_let = len(upi_id)
    upi_index= upi_let - 1
    upi_verify=0
    for i in upi_id:
        if i == "@":
            upi_verify=1
    if upi_verify == 1 and upi_id[upi_index] != "@":
        order_placed()
    else:
        print("Please Enter Correct UPI id")
        upi()

def order_placed():
    print("")
    print("Hurray !!")
    print("Order Placed")
    print("")
    order_no= random.randint(10000, 99999)
    order_date= date.today()
    #order_amount= amount * qty
    print("Your Order number is", order_no)
    print("Payment mode is", paymentopts.payment_method)
    print("Ordered on", order_date)
    #print("Total Amount is", order_amount)
    
def update_login():    
    sql = "INSERT INTO login (Name, Email, Username, Password) VALUES (%s, %s, %s, %s)"
    val = (llog.name, llog.login_id,llog.username,llog.password_id)
    cur.execute(sql, val)
    mydb.commit()
    
def cleardb_login():
    sql = "DELETE FROM login"
    cur.execute(sql)
    mydb.commit()

def seedb_login():
    sql = "SELECT * FROM login"
    cur.execute(sql)
    for x in cur:
        print(x)

home()
