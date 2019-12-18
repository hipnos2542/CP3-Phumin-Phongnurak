menuList = []
def showBill():
    print("----- My shop -----")
    print(" Menu              Price")
    for number in range(len(menuList)):
        print("  " + menuList[number][0] + " "*15 + menuList[number][1])
def total():
    total = 0
    for price in menuList:
        total = total + int(price[1])
    print("total price =  %d   THB"%(total))

while True:
    menu = input("Enter menu (Enter 'exit' to close programe):")
    if menu.lower() == "exit":
        break
    else:
        price = input("Enter Price :")
        menuList.append([menu,price])

showBill()
total()