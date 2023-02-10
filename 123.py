def printStar(n):
    if n >0:
        print('별'*n)
        printStar(n-1)

printStar(5)
