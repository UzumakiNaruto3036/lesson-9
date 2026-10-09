n=int(input("Enter a number of terms: "))
sum=1
i=1
while i<=n:
    sum=sum*i
    i=i+1
print("The factorial of first",n,"terms is:",sum)