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
llog.name=""
llog.name2="User"
llog.it=0
llog.name=""
llog.id=0
llog.qty=0
llog.am=0

def invalid():
    print("---------------------------------------")
    print("Please Select Valid Option")
    print("---------------------------------------")
    
def home():
    print("---------------------------------------")
    print("             ONLINE SHOPPING           ")    
    print("---------------------------------------")
    if llog.login_id != "":
        print("Welcome", llog.name2)
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
    print("[7] EXIT")
    print("---------------------------------------")
    print(" Press '#' to back to home")
    print(" From anywhere ( without qoutes )")
    print("---------------------------------------")
    screen_opt= input(choice)
    if screen_opt == '1':
        if row.cnt == 0:
            print("---------------------------------------")
            print("No Account Found in Database")
            print("Create new Account first")
            print("---------------------------------------")
            home()
        elif llog.login_id == "":
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
    elif screen_opt == '7':
        quit
    else:
        invalid()
        home()

def logout():
    llog.login_id=""
    llog.password_id=""
    llog.username=""
    llog.name2="User"
    print("---------------------------------------")
    print("Logout Successfully !")
    print("---------------------------------------")
    home()

def login():
    print("---------------------------------------")
    print("                LOGIN                  ")    
    print("---------------------------------------")
    llog.login_id1=input("Enter Your Email Address: ")
    if llog.login_id1 == '#':
        home()
    llog.login_id2=llog.login_id1.lower()
    log_let = len(llog.login_id)
    log_index= log_let - 1
    log_verify=0
    for i in llog.login_id2:
        if i == "@":
            log_verify=1
    if log_verify == 0 or llog.login_id2[log_index] == "@":
        print("Please Enter Valid Email")
        login()
    cur.execute("SELECT * FROM login")
    for x in cur:
        c=str(x[1])
        if c == llog.login_id2:
            log_passwo=input("Enter your Password: ")
            if log_passwo == '#':
                home()
            elif x[3] == log_passwo:
                llog.login_id=x[1]
                llog.password_id=x[3]
                llog.username=x[2]
                llog.name2=x[0]
                print("---------------------------------------")
                print("Loggined Successfully !!")
                print("---------------------------------------")
                home()
                break;
            else:
                print("---------------------------------------")
                print("Incorrect Password")
                print("Please Re enter Password and email")
                print("---------------------------------------")
                login()
                break;
        else:
            llog.login_id=""
            print("---------------------------------------")
            print("Your Email not registered")
            print("Please Register First!!")
            print("---------------------------------------")
            home()
            break;
          
def register():
    llog.name1=input("Enter Your Name: ")
    if llog.name1 == "#":
        home()
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
    if llog.login_id1 == '#':
        home()
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
    if llog.password_id == '#':
        home()
    pass_verify= len(llog.password_id)
    if pass_verify < 4:
        print("Please Create Password greater than 5 letters")
        pass_cre()

def usern():
    cur.execute("SELECT * FROM login")
    llog.username1=input("Create your Username: ")
    if llog.username1 == '#':
        home()
    llog.username=llog.username1.lower()
    for x in cur:
        if x[2] == llog.username:
            print("Username Already Used Please Retry!!")
            usern()
            break;
   
def search():
    print("---------------------------------------")
    search1= input("Enter Name of Product: ")
    print("---------------------------------------")
    if search1 == '#':
        home()
    search2= search1.lower()
    cur.execute("SELECT * FROM items")
    print("Item No.     Name       Amount")
    for x in cur:
        word_l = x[0].lower()
        word = word_l.split()
        for i in word:
            if i == search1:
                print(x[2],"          ",x[0],'  ','Rs.',x[1])
                print("")
                llog.it+=1
                print(llog.it, "Product found")
                
    if llog.it == 0:
        print("")
        print("No product Found with this name")
        print("Please try again !!")
        print("or Press # to go Home")
        search()
    else:
        product_int()

def product_int():
    print("---------------------------------------")
    print("Select Item no to Proceed to buy")
    print("or Press # to go back")
    print("or Press * to research")
    print("---------------------------------------")
    llog.buy_it = input(choice)
    if llog.buy_it =='#':
        llog.it=0
        home()
    elif llog.buy_it == '*':
        llog.it=0
        search()
    else:
        if llog.login_id == '':
            print("Please Login In First !!")
            llog.it=0
            home()
        else:
            verify_pro()


def verify_pro():
    cur.execute("SELECT * FROM items")
    verfy = 0
    for x in cur:
        c = str(x[2])
        if c == llog.buy_it:
            verfy = 1
            llog.name=x[0]
            llog.id=x[2]
            llog.am=x[1]
            break
    if verfy == 0:
        print("Invalid Item No.")
        product_int()
    else:
        print("---------------------------------------")
        print("Are you sure that you want to buy", llog.name)
        vero = input("[Y/N]: ")
        ver = vero.lower()
        if ver == 'y':
            print("---------------------------------------")
            llog.qty = int(input("Enter Qty:"))
            order_det()
            paymentopts()
        if ver == 'n':
            home()
        else:
            print("Please select valid option!!")
            verify_pro()
            
def order():
    print("---------------------------------------")
    print("                ORDERS")
    print("---------------------------------------")
    cur.execute("SELECT * FROM orders")
    for x in cur:
        if x[4] == llog.login_id:
            print("---------------------------------------")
            print("Order number :", x[0])
            print("Email        :", x[4])
            print("Item name    :", x[2])
            print("Amount       :", x[3])
            print("Quantity     :", x[6])
            print("Payment mode :", x[5])
            print("Order Date   :", x[1])
            print("Total Amount :", x[7])
            print("---------------------------------------")
    end=input("Press Enter to back")
    home()
        
def items():
    cur.execute("SELECT * FROM items")
    print("Item No.     Name       Amount")
    for x in cur:
        print(x[2],"          ",x[0],'  ','Rs.',x[1])
    product_int()
    
def paymentopts():
    print("Select Payment Method")
    print("[1] UPI")
    print("[2] Debit Card / Credit Card")
    print("[3] Cash On Delivery")
    print("[4] Go back to Home")

    payment_method = "none"
    pay_opt = input(choice)
    if pay_opt == '#':
        home()
    elif pay_opt == '1':
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
    if card_no == '#':
        home()
    card_verify = card_no / 10**15
    if card_verify < 10 and card_verify >= 1:
        card_month()        
    else:
        print("Please re enter Correct Card Details")
        card_num()
    
def card_month():
    card_mon = int(input("Enter Expiry Month in MM format: "))
    if card_mon == '#':
        home()
    if card_mon < 13 and card_mon != 0:
        card_year()        
    else:
        print("Please re enter Correct Expiry Month")
        card_month()

def card_year():
    card_yr = int(input("Enter Expiry Year in YY format: "))
    if card_yr == '#':
        home()
    elif card_yr >= 21:
        card_cvv()
    else:
        print("Please re enter Correct Expiry Year")
        card_year()

def card_cvv():
    card_cv = int(input("Enter 3/4 Digit Card CVV: "))
    if card_cv == '#':
        home()
    card_verify = card_cv / 10**2
    if card_verify < 100 and card_verify >= 1:
        order_placed()        
    else:
        print("Please re enter Correct CVV")
        card_cvv()

def upi():
    upi_id = input("Enter Your UPI id: ")
    if upi_id == '#':
        home()
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

def order_no():
    if row_or.cnt == 0:
        llog.order_no= random.randint(10000, 99999)
    else:
        llog.order_no= random.randint(10000, 99999)
        cur.execute("SELECT * FROM orders")
        for x in cur:
            if x[0] == llog.order_no:
                order_no()

def order_det():
    print("---------------------------------------")
    order_no()    
    llog.order_date= date.today()
    llog.order_amount = llog.am * llog.qty
    print("Your Order number is", llog.order_no)
    print("Item name is", llog.name)
    #print("Payment mode is", paymentopts.payment_method)
    print("Order Date is", llog.order_date)
    print("Total Amount is", llog.order_amount)
    print("---------------------------------------")

def order_placed():
    print("---------------------------------------")
    print("              Order Placed")
    print("---------------------------------------")
    print("Order number :", llog.order_no)
    print("Email        :", llog.login_id)
    print("Item name    :", llog.name)
    print("Amount       :", llog.am)
    print("Quantity     :", llog.qty)
    print("Payment mode :", paymentopts.payment_method)
    print("Order Date   :", llog.order_date)
    print("Total Amount :", llog.order_amount)
    print("---------------------------------------")
    update_order()
    reset_order()
    end=input("Write any thing to go home: ")
    home()
    
def update_login():    
    sql = "INSERT INTO login (Name, Email, Username, Password) VALUES (%s, %s, %s, %s)"
    val = (llog.name2, llog.login_id,llog.username,llog.password_id)
    cur.execute(sql, val)
    mydb.commit()

def update_order():    
    sql = "INSERT INTO orders (order_no, date, item, amount, email, pay_method, qty, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (llog.order_no, llog.order_date,llog.name,llog.am,llog.login_id,paymentopts.payment_method,llog.qty,llog.order_amount)
    cur.execute(sql, val)
    mydb.commit()

def reset_order():
    llog.order_no = 0
    llog.order_date= ''
    llog.name=''
    llog.am=0
    paymentopts.payment_method=''
    llog.qty=0
    llog.order_amount=0

def update_item():    
    sql = "INSERT INTO items (name, amount, item_no, category) VALUES (%s, %s, %s, %s)"
    val = ('Yonex Gr 300',500,1,'Sports')
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

def seedb_items():
    sql = "SELECT * FROM items"
    cur.execute(sql)
    for x in cur:
        print(x)
        
def row():
    sql = "SELECT * FROM login"
    cur.execute(sql)
    row.cnt=cur.rowcount

def row_or():
    sql = "SELECT * FROM login"
    cur.execute(sql)
    row_or.cnt=cur.rowcount

row()
row_or()
home()
