def squareList():
    list6=[]
    for i in range(1,31):
        if (i<6 or i>25):
            list6.append(i**2)
    print(list6)

squareList()