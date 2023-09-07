#alternative code
from functools import lru_cache

#fibonacci_cache = {}
@lru_cache(maxsize=1000)
def fibonacci (n):
    #if n in fibonacci_cache :
    #    return fibonacci_cache[n]
    if n <= 1 :
        #value = 1
        return 1
    elif n == 2 :
        #value = 1
        return 1
    elif n > 2 :
        #value = fibonacci (n-1) + fibonacci(n-2)
        return fibonacci (n-1) + fibonacci(n-2)
    
    #fibonacci_cache [n] = value
    #return value

for i in range(1,101):
    print( i ," : ",fibonacci(i))