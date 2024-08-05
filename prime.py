

def prime(n):
    if n==1:
        print("not a prime")
    if n > 1:
        for i in range(2,n):
            if n%i == 0:
                print("not prime")
                break
        else :
            print("prime")

prime(1)
