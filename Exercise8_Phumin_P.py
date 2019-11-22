usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "customer" and passwordInput == "1234":
    print("Welcome to PhumShop")
    print("-- List fo Produce --")
    print("1. Milk  : 10 THB")
    print("2. Water :  7 THB")
    print("3. Juice : 15 THB")
    userSelected = int(input(">>> "))
    if userSelected == 1:
        numProduce = int(input("Number of products to buy :"))
        calculator1 = 10 * numProduce
        print("You are buying Milk " + str(numProduce) + " Piece")
        print("Total price : " + str(calculator1) + " THB")
    elif userSelected == 2:
        numProduce = int(input("Number of products to buy :"))
        calculator2 = 7 * numProduce
        print("You are buying Watere " + str(numProduce) + "Piece")
        print("Total price : " + str(calculator2) + " THB")
    elif userSelected == 3:
        numProduce = int(input("Number of products to buy :"))
        calculator3 = 15 * numProduce
        print("You are buying Juice " + str(numProduce) + "Piece")
        print("Total price : " + str(calculator3) + " THB")
    else:
        print(">>> Incorrect information(Selected 1,2 and 3 number)")
else:
    print("_____>>> Username or Password is incorrect <<<_____")