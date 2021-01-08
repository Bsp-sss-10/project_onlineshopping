import random
from datetime import date
import sys
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
llog.cart1=[]
llog.cart2=[]
llog.cart3=[]
llog.cart4=[]
llog.cart5=[]
llog.cartp=0
llog.cart_total=0
llog.cart_it=0

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
    print("[6] VIEW CART")
    if llog.login_id != "":
        print("[7] LOGOUT")
    print("[8] EXIT")
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
            cart()
    elif screen_opt == '7':
        if llog.login_id != "":
            logout()
            print("---------------------------------------")
            print("Logout Successfully !")
            print("---------------------------------------")
            home()
        else:
            invalid()
            home()
    elif screen_opt == '8':
        sys.exit()
    else:
        invalid()
        home()

def logout():
    llog.login_id=""
    llog.password_id=""
    llog.username=""
    llog.name2="User"
    
def login():
    cap_cha()
    print("---------------------------------------")
    print("                LOGIN                  ")    
    print("---------------------------------------")
    llog.login_id1=input("Enter Your Email Address: ")
    if llog.login_id1 == '#':
        logout()
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
    log1=0
    for x in cur:
        c=str(x[1])
        if c == llog.login_id2:
            log_passwo=input("Enter your Password: ")
            if log_passwo == '#':
                logout()
                home()
            elif x[3] == log_passwo:
                log1=1
                llog.login_id=x[1]
                llog.password_id=x[3]
                llog.username=x[2]
                llog.name2=x[0]
                print("---------------------------------------")
                print("Logged in Successfully !!")
                print("---------------------------------------")
                home()
                break;
            else:
                print("---------------------------------------")
                print("Incorrect Password")
                print("Please Re enter Password and email")
                print("---------------------------------------")
                log1=1
                login()
    if log1 == 0:
        llog.login_id=""
        print("---------------------------------------")
        print("Your Email not registered")
        print("Please Register First!!")
        print("---------------------------------------")
        home()
          
def register():
    cap_cha()
    print("---------------------------------------")
    llog.name1=input("Enter Your Name: ")
    if llog.name1 == "#":
        logout()
        home()
    llog.name2=llog.name1.lower()
    usern()
    log_cre()
    pass_cre()
    print("---------------------------------------")
    print("Successfully Logged in and Registered!!")
    print("---------------------------------------")
    update_login()
    home()

def log_cre():
    llog.login_id1=input("Enter Your Email Address: ")
    if llog.login_id1 == '#':
        logout()
        home()
    llog.login_id=llog.login_id1.lower()
    log_let = len(llog.login_id)
    log_index= log_let - 1
    log_verify=0
    for i in llog.login_id:
        if i == "@" or i == " ":
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
    llog.password_id=input("Create Your Password (Atleast 4 Letters): ")
    if llog.password_id == '#':
        logout()
        home()
    pass_verify= len(llog.password_id)
    if pass_verify < 4:
        print("Please Create Password alteast4 letters")
        pass_cre()

def usern():
    cur.execute("SELECT * FROM login")
    llog.username1=input("Create your Username: ")
    if llog.username1 == '#':
        logout()
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
    print("")
    if search1 == '#':
        home()
    search2= search1.lower()
    cur.execute("SELECT * FROM items")
    print("--------------------------------------------------------------------")
    print("   Item No.  | Name                                 | Amount       |")
    print("--------------------------------------------------------------------")
    for x in cur:
        word_l = x[0].lower()
        word = word_l.split()
        for i in word:
            w = i.lower()
            if w == search2:
                c=len(x[0])
                d= 35-c
                e=d*' '
                f=str(x[2])
                f1=len(f)
                g=3-f1
                h=g*' '
                w=str(x[1])
                y=len(w)
                z=7-y
                z1=z*' '
                print("    ",x[2],h,'   |',x[0],e,'|','Rs.',x[1],z1,'|')
                llog.it+=1
    print("--------------------------------------------------------------------")
                
    if llog.it == 0:
        print("")
        print("---------------------------------------")
        print("No product Found with this name")
        print("Please try again !!")
        print("or Press # to go Home")
        print("---------------------------------------")
        search()
    else:
        product_int()

def product_int():
    print("---------------------------------------")
    print("Select Item no to Add to Cart")
    print("or Press # to go back")
    print("or Press $ to go cart")
    print("or Press * to search again")
    print("---------------------------------------")
    llog.buy_it = input(choice)
    if llog.buy_it =='#':
        llog.it=0
        home()
    elif llog.buy_it == '*':
        llog.it=0
        search()
    elif llog.buy_it == '$':
        llog.it=0
        cart()
    else:
        if llog.cartp != 0:
            for i in range (0,llog.cartp):
                x_12 = str(llog.cart5[i]) 
                if x_12 == llog.buy_it:
                    print("---------------------------------------")
                    print("Item Already Added to cart")
                    print("---------------------------------------")
                    print("Do you want to edit quantity of",llog.cart1[i],"?")
                    print("Writing other Y/N will be considered as N")
                    print("---------------------------------------")
                    kkk = input("[Y/N] : ")
                    print("---------------------------------------")
                    kkkk = kkk.lower()
                    if kkkk == 'y':
                        llog.qty0 = int(input("Enter quantity :"))
                        if llog.qty0 <= 0:
                            print("Please select valid quantity !!")
                            product_int()
                        llog.qty=llog.qty0    
                        print("---------------------------------------")
                        print("Quantity Edited Successfully !!")
                        print("---------------------------------------")
                        llog.cart4[i] = llog.qty
                        llog.order_amount = llog.am * llog.qty
                        llog.cart3[i] = llog.order_amount
                        product_int()
                    else:
                        product_int()
        verify_pro()


def captcha():
    cap=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','U','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9,0]
    cap0 = random.choice(cap)
    cap1 = random.choice(cap)
    cap2 = random.choice(cap)
    cap3 = random.choice(cap)
    cap4 = random.choice(cap)
    capp0 = str(cap0)
    capp1 = str(cap1)
    capp2 = str(cap2)
    capp3 = str(cap3)
    capp4 = str(cap4)
    capt = capp0 + capp1 +capp2 + capp3 + capp4
    print("---------------------------------------")
    print("PLEASE SOLVE CAPTCHA BELOW TO PROCEED")
    print("---------------------------------------")
    print("             ",cap0,cap1,cap2,cap3,cap4)
    print("---------------------------------------")
    print("Please Write Captcha Without Space")
    print("Press # to go back to home")
    print("Press * to Change Captcha")
    print("---------------------------------------")
    cape = input("Type Captcha or Select Options:")
    if cape == '#':
        home()
    elif cape == '*':
        captcha()
    elif cape == capt:
        print("---------------------------------------")
        print("             CAPTCHA SOLVED")
        print("---------------------------------------")
    else:
        print("---------------------------------------")
        print("      CAPTCHA INCORRECT PLEASE RETRY")
        print("---------------------------------------")
        captcha()

def cap_cha():
    capq = [0,0,0,1,1]
    capq1 = random.choice(capq)
    if capq1 == 1:
        captcha()

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
        print("Product Name:", llog.name)
        print("Price       :", llog.am)
        vero = input("Are you sure that you want to Add to cart? [Y/N]: ")
        ver = vero.lower()
        if ver == 'y':
            print("---------------------------------------")
            llog.qty0 = int(input("Enter quantity :"))
            if llog.qty0 <= 0:
                print("Please select valid quantity !!")
                product_int()
            llog.qty=llog.qty0
            llog.order_amount = llog.am * llog.qty
            llog.cart1.append(llog.name)
            llog.cart2.append(llog.am)
            llog.cart3.append(llog.order_amount)
            llog.cart4.append(llog.qty)
            llog.cart5.append(llog.id)
            print(llog.name, 'is Added successfully !!')
            llog.cartp+=1
            product_int()
        elif ver == 'n':
            product_int()
        else:
            print("Please select valid option!!")
            verify_pro()

def cart():
    print("---------------------------------------")
    print("                CART")
    print("---------------------------------------")
    if llog.cartp == 0:
        print("")
        print("              Cart is empty")
        print("")
        print("---------------------------------------")
        end=input("Press Enter to go back")
        home()
    else:
        llog.cart_total=0
        print("-----------------------------------------------------------------------------------------------")
        print("   Item No.  | Name                                    |    Price     |  Qty  |  Amount       |")
        print("-----------------------------------------------------------------------------------------------")
        for c in range (0,llog.cartp):
            c1=len(llog.cart1[c])
            d= 35-c1
            e=d*' '
            f=str(llog.cart2[c])
            f1=len(f)
            g=7-f1
            h=g*' '
            w=str(llog.cart4[c])
            y=len(w)
            z=3-y
            z1=z*' '
            z2=str(llog.cart3[c])
            z3=len(z2)
            z4=11-z3
            z5=z4*' '
            z6=str(llog.cart5[c])
            z7=len(z6)
            z8=10-z7
            z9=z8*' '
            print("",llog.cart5[c],z9,"|",llog.cart1[c],e,'   | Rs.',llog.cart2[c],h,'| ',llog.cart4[c],z1,'| ',llog.cart3[c],z5,'|')
            llog.cart_total+=llog.cart3[c]
        print("-----------------------------------------------------------------------------------------------")
        print("Total :", llog.cart_total)
        print("-----------------------------------------------------------------------------------------------")
        print("---------------------------------------")
        print(" Type 'b' to proceed to buy")
        print(" Type 'e' to edit cart")
        print(" Type 'c' to clear cart")
        print(" Type '#' to go back to home")
        print("---------------------------------------")
        cart_opt=input(choice)
        cart_opt2=cart_opt.lower()
        if cart_opt2 == 'b':
            if llog.login_id == '':
                print("---------------------------------------")
                print("Please Login In First !!")
                print("---------------------------------------")
                home()
            else:
                order_det()
                paymentopts()
        elif cart_opt2 == 'e':
            cart_edit()
        elif cart_opt2 == '#':
            home()
        elif cart_opt2 == 'c':
            are_sure = input("Are you Sure? [Y/N]:")
            if are_sure.lower() == 'y':
                llog.cart1=[]
                llog.cart2=[]
                llog.cart3=[]
                llog.cart4=[]
                llog.cart5=[]
                llog.cartp=0
                print("Cart Cleared Successfully !!")
                home()
            else:
                cart()
        else:
            print("Please Select valid Option !!")
            cart()

def cart_edit2():
    print("---------------------------------------")
    print("Please Select Options from below")
    print("---------------------------------------")
    print("type '1' to edit quantity")
    print("type '2' to remove item")
    print("type '3' to reselect item")
    print("type '#' to go to Home")
    print("type 'c' to go to Cart")
    print("---------------------------------------")
    carted = input(choice)
    carted1=carted.lower()
    if carted1 == '1':
        for i in range (0,llog.cartp): 
            if llog.cart5[i] == llog.cart_it:
                llog.qty0 = int(input("Enter quantity :"))
                if llog.qty0 <= 0:
                    print("Please select valid quantity !!")
                    cart()
                llog.qty=llog.qty0
                print("---------------------------------------")
                print(" Quantity Edited Successfully !!")
                print("---------------------------------------")
                llog.cart4[i] = llog.qty
                llog.order_amount = llog.am * llog.qty
                llog.cart3[i] = llog.order_amount
                llog.cartp = len(llog.cart5)
                llog.cart_total=0
                cart()
    elif carted1 == '2':
        for i in range (0,llog.cartp):
            if llog.cart5[i] == llog.cart_it:
                print("---------------------------------------")
                print(" Item Removed Successfully !!")
                print("---------------------------------------")
                llog.cart1.pop(i)
                llog.cart2.pop(i)
                llog.cart3.pop(i)
                llog.cart4.pop(i)
                llog.cart5.pop(i)
                llog.cartp = len(llog.cart5)
                llog.cart_total=0
                if llog.cartp == 0:
                    home()
                else:
                    cart()
    elif carted1 == '3':
        llog.cart_it=0
        cart_edit()
    elif carted1 == '#':
        llog.cart_it=0
        home()
    elif carted1 == 'c':
        llog.cart_it=0
        cart()
    else:
        print("---------------------------------------")
        print("Please Select valid option")
        cart_edit2()
        
def cart_edit():
    print("---------------------------------------")
    print("type '#' to go to Home")
    print("type 'c' to go to Cart")
    print("---------------------------------------")
    cart_edo = input("Select item no. you want to edit: ")
    cart_edo2= cart_edo.lower()
    if cart_edo2 == '#':
        home()
    elif cart_edo2 == 'c':
        cart()
    item_verc = 0
    for i in range (0,llog.cartp):
        c = str(llog.cart5[i])
        if c == cart_edo:
            item_verc = 1
            llog.cart_it=llog.cart5[i]
    if item_verc == 0:
        print("Please Select valid Item !!")
        print("---------------------------------------")
        cart_edit()
    cart_edit2()    
           
def order():
    print("---------------------------------------")
    print("                ORDERS")
    print("---------------------------------------")
    cur.execute("SELECT * FROM orders")
    or_vet = 0
    for x in cur:
        if x[4] == llog.login_id:
            print("---------------------------------------")
            print("Order number :", x[0])
            print("Item name    :", x[2])
            print("Amount       :", x[3])
            print("Quantity     :", x[6])
            print("Payment mode :", x[5])
            print("Order Date   :", x[1])
            print("Total Amount :", x[7])
            print("---------------------------------------")
            print("")
            or_vet+=1
    if or_vet == 0:
        print("")
        print("                Opps !!")
        print("        No Orders Were Found")
        print("")
        print("---------------------------------------")
    end=input("Press Enter to go back")
    home()
        
def items():
    cur.execute("SELECT * FROM items")
    print("--------------------------------------------------------------------")
    print("   Item No.  | Name                                 | Amount       |")
    print("--------------------------------------------------------------------")
    for x in cur:
        c=len(x[0])
        d= 35-c
        e=d*' '
        f=str(x[2])
        f1=len(f)
        g=3-f1
        h=g*' '
        w=str(x[1])
        y=len(w)
        z=7-y
        z1=z*' '
        print("    ",x[2],h,'   |',x[0],e,'|','Rs.',x[1],z1,'|')
        llog.it+=1
    print("--------------------------------------------------------------------")
    print("")
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
    print("Your Order number is", llog.order_no)
    print("---------------------------------------")
    print("Total Items x Qty")
    print("---------------------------------------")
    for i in range (0,llog.cartp):
        oo1=str(llog.cart4[i])
        oo2='x'+oo1
        print(llog.cart1[i],oo2)
    print("---------------------------------------")
    print("Order Date is", llog.order_date)
    print("Total Amount is", llog.cart_total)
    print("---------------------------------------")

def order_placed():
    print("----------------------------------------------------------------------")
    print("                            Order Placed")
    print("----------------------------------------------------------------------")
    print(" Order number                  :", llog.order_no)
    print(" Email                         :", llog.login_id)
    print("----------------------------------------------------------------------")
    print(" Item                         |    Price     |  Qty  |  Amount       |")
    print("----------------------------------------------------------------------")
    for c in range (0,llog.cartp):
        c1=len(llog.cart1[c])
        d= 25-c1
        e=d*' '
        f=str(llog.cart2[c])
        f1=len(f)
        g=7-f1
        h=g*' '
        w=str(llog.cart4[c])
        y=len(w)
        z=3-y
        z1=z*' '
        z2=str(llog.cart3[c])
        z3=len(z2)
        z4=11-z3
        z5=z4*' '
        print(llog.cart1[c],e,'   | Rs.',llog.cart2[c],h,'| ',llog.cart4[c],z1,'| ',llog.cart3[c],z5,'|')
    print("----------------------------------------------------------------------")
    print(" Payment mode                  :", paymentopts.payment_method)
    print(" Order Date                    :", llog.order_date)
    print(" Total Amount                  :", llog.cart_total)
    print("----------------------------------------------------------------------")
    update_order()
    reset_order()
    end=input("Press Enter to go home: ")
    home()
    
def update_login():    
    sql = "INSERT INTO login (Name, Email, Username, Password) VALUES (%s, %s, %s, %s)"
    val = (llog.name2, llog.login_id,llog.username,llog.password_id)
    cur.execute(sql, val)
    mydb.commit()

def update_order():
    for i in range (0,llog.cartp):        
        sql = "INSERT INTO orders (order_no, date, item, amount, email, pay_method, qty, total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (llog.order_no, llog.order_date,llog.cart1[i],llog.cart2[i],llog.login_id,paymentopts.payment_method,llog.cart4[i],llog.cart3[i])
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
    llog.cart1=[]
    llog.cart2=[]
    llog.cart3=[]
    llog.cart4=[]
    llog.cart5=[]
    llog.cartp=0
    
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
