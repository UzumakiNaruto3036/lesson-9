n=int(input("Enter a number : "))
if n>=0 and n<=9:
    print(n,"is a single digit number")
elif n>=10 and n<=99:
    print(n,"is a two digit number")
elif n>=100 and n<=999:
    print(n,"is a three digit number")
elif n>=1000 and n<=9999:
    print(n,"is a four digit number")
elif n>=10000 and n<=99999:
    print(n,"is a five digit number")
elif n>=100000 and n<=999999:
    print(n,"is a six digit number")
else:
    print(n,"is a 7 digit or more number")