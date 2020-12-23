import random
from datetime import date

choice="Enter your Choice: "

def invalid():
    print("---------------------------------------")
    print("Please Select Valid Option")
    print("---------------------------------------")
    
def home():
    home.login_id=""
    home.password_id=""
    home.username=""
    home.name="User"
    print("---------------------------------------")
    print("             ONLINE SHOPPING           ")    
    print("---------------------------------------")
    if home.login_id != "":
        print("Welcome", home.name)
        print("---------------------------------------")
    else:
        print("---------------------------------------")
        print("[1] LOGIN")
    if home.login_id == "":    
        print("[2] CREATE NEW ACCOUNT")

    if home.login_id != "":
        print("[3] YOUR ORDERS")
        
    print("[4] SEARCH ITEMS")
        
    print("[5] VIEW ALL ITEMS")
    print("---------------------------------------")
    screen_opt= input(choice)
    if screen_opt == '1':
        if home.login_id == "":
            login()
        else:
            invalid()
            home()
    elif screen_opt == '2':
        if home.login_id == "":
            register()
        else:
            invalid()
            home()
    elif screen_opt == '4':
        search()
    elif screen_opt == '3':
        if home.login_id != "":
            order()
        else:
            invalid()
            home()
    elif screen_opt == '5':
        items()
    else:
        invalid()
        home()

def login():
    print("")
    
def register():
    print("")
    
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
    

home()
