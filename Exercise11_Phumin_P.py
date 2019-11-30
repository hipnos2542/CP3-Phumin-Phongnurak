inputRow = int(input("Enter row : "))
star = 1
space = " "
for i in range(inputRow):
    print(space*(inputRow-(i+1))+"*"*(i+star))
    star += 1
