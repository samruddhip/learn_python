num = int(input("Enter a number:"))

def fabinacciSeries(num):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b= c
        print(c)

fabinacciSeries(num)