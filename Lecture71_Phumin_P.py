menuList = []
priceList = []

def showBill():
    print("----- My shop -----")
    print(" Menu             Price")
    for number in range(len(menuList)):
        print("  " + menuList[number] + (" "*15) + priceList[number])
def total():
    total = 0
    for price in priceList:
        total = total + int(price)
    print("total price =  %d   THB"%(total))

while True:
    menu = input("Enter menu (Enter 'exit' to close programe):")
    if menu.lower() == "exit":
        break
    else:
        price = input("Enter Price :")
        menuList.append(menu)
        priceList.append(price)
showBill()
total()