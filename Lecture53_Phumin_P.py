def vatCalculator(totallPrice):
    result = totallPrice+(totallPrice * 7/100)
    return result
price = int(input("Enter product price : "))
print(vatCalculator(price))