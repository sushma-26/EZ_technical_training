#Magical Prime
#reverse of prime number is also a prime number then it is magical prime
#17 prime 71 prime so both magical prime 
def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return 0
    return 1
def magical_prime(n1):
    n=n1
    n2 = 0
    while n > 0:
        digit = n % 10
        n2 = n2 * 10 + digit
        n = n // 10
    if prime(n2)==1 and prime(n1)==1:
        print("Yes")
    else:
        print("No")
n=int(input())   
magical_prime(n)