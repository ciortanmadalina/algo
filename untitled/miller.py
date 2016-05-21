import random

def my_pow(a,e):
    if e == 1 :
        return a
    if e == 2 :
        return a * a
    prefix_a = a
    if e %2 == 0:
        prefix_a = 1
    new_exp = e//2
    return prefix_a * my_pow ( a * a, new_exp)
'''
2 ^ 4 %5
(2 * 2)^2
(2%5 * 2 %5)2


'''
def my_pow_modulo(a, e, modulo):

    if e == 1 :
        return a % modulo
    if e == 2 :
        return ((a % modulo )*(a% modulo)) % modulo
    prefix_a = a % modulo
    if e %2 == 0:
        prefix_a = 1 % modulo
    new_exp = e//2
    return (prefix_a * (my_pow ( (a% modulo) * (a% modulo), new_exp)% modulo)) % modulo
# pgcd(a,b) = pgcd(b, a%b) (euclid)
def pgcd(a,b):
    if b == 0 :
        return a
    return pgcd(b, a % b)

# n = m * 2^i
def calculateM(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return calculateM(n //2)
    else:
        return n


def runMiller(a, n):
    w = my_pow_modulo(a, n-1, n)
    if(w != 1):
        print('n = %s pas premier' % n)
        return False

    m = calculateM(n-1)
    term = my_pow(a,m)
    my_pgcd = pgcd(term - 1, n)

    if(my_pgcd < n and my_pgcd > 1):
        print('pgcd n = %s pas premier' % n)
        return False

    #probablement c'est true mais acec une probabilite d'erreur <1/2
    print('n = %s Premier' % n)
    return True


def certainMiller(a, n):
    if runMiller(a, n) == False:
        return False # we are sure

    #on va iterer 50 fois
    for i in range (20) :
        a = random.randrange(2,n) #generer un autre a
        if runMiller(a, n) == False:
            return False # we are sure

    return True

def isPrime( n):
    a = random.randrange(2,n)
    return certainMiller(a, n)

def input():
    n = random.randrange(3,100)

    print("Number n %s is Prime %s" % (n, isPrime(n)))

    '''
    a = random.randrange(2,n)
    print('a = %s, n = %s ' %(a,n))
    runMiller(a,n)
    '''
    #print (calculateM(1))
    #print (pgcd(12,20))

    #x = my_pow(a, n-1)
    #modulo = my_pow_modulo(3,3, 5)
    #print('a = %s, n = %s, pow = %s, modulo = %s ' %(a,n, x , modulo))


input()