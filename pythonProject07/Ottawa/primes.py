
def is_prime(num):
    if num<2:
        return False

    if num==2:
        return True

    for i in range(2,num+1):
        if num%i==0:
            return False

    return True


def all_primes(n1,n2):
    for i in range(n1,n2):
        if is_prime(i):
            print(i,end=" ")



num1=int(input("Enter First No:"))
num2=int(input("Enter Last No:"))

all_primes(num1,num2)



