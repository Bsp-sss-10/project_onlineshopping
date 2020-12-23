login_id=""
password_id=""
username="User"

def invalid():
    print("---------------------------------------")
    print("Please Select Valid Option")
    home()
    
def home():
    print("---------------------------------------")
    print("             ONLINE SHOPPING           ")    
    print("---------------------------------------")
    print("---------------------------------------")
    if login_id != "":
        print("Welcome", username)
    else:
        print("[1] LOGIN")
    if login_id == "":    
        print("[2] CREATE NEW ACCOUNT")
        
    print("[3] SEARCH")
    
    if login_id != "":
        print("[4] YOURS ORDERS")
        
    print("[5] BUY ITEMS")
    print("---------------------------------------")
    screen_opt= int(input("Enter Your Choice: "))
    if screen_opt == 1:
        if login_id == "":
            login()
        else:
            invalid()
    elif screen_opt == 2:
        if login_id == "":
            register()
        else:
            invalid()
    elif screen_opt == 3:
        search()
    elif screen_opt == 4:
        if login_id != "":
            order()
        else:
            invalid()
    elif screen_opt == 5:
        items()
    else:
        invalid()

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
    
home()
