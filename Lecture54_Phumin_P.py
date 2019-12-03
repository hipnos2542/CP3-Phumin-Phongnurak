def login(): # โปรแกรมล็อกอิน
    usernameInput = input("Username :")
    passwordInput = input("Password :")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu(): #โชว์เมนู
    print("_____iShop_____")
    print("1. Vat calculator")
    print("2. Price calculator")

def menuSelect(): # เลือกเมนู
    userSelected = int(input(">>> "))
    return userSelected

def vatCalculate(totallPrice): # คำนวนภาษีมูลค่าเพิ่ม
    vat = 7
    result = totallPrice + (totallPrice * vat / 100)
    return result

def priceCalculate(): #คำนวนราคาสินค้า
    price1 = int(input("First Product Price :"))
    price2 = int(input("Second Product Price :"))
    return vatCalculate(price1 + price2)

#ส่วนของการทำงาน
while True:
    if login() == True:
        showMenu()
        select = menuSelect()
        if select == 1:
            price = int(input("Enter you price :"))
            print(vatCalculate(price))
            break
        elif select == 2:
            print(priceCalculate())
            break
        else:
            print(">>>>>    Pleas select number 1 or number 2 <<<<<<")
            continue

    else:
        print("_______________________________________")
        print("Wrong!!!")
        print("Username or Password is incorrect")
        print("Try again")
        print("_______________________________________")
        continue