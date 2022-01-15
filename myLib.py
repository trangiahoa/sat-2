def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n // 2):
            if n % i == 0:
                return False
        return True


def factorial(n):
    if n == 0: return 1
    return n * factorial(n-1)


    
            
        

