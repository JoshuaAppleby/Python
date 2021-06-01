#Project Euler, Problem 45
#Triangular, pentagonal, and hexagonal

"""Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.
Find the next triangle number that is also pentagonal and hexagonal.
"""

import time

def isitpentagonal(p):
    if (1+(24*p+1)**0.5) % 6 == 0:
        return True
    return False

def is_hexagonal(h):
    if (1+(8*h+1)**0.5) % 4 == 0:
        return True
    return False

def tripenthex(N):
    while True:
        triangle = N*(N+1)/2
        if isitpentagonal(triangle) and is_hexagonal(triangle):
            return int(triangle)
        N += 1

start = time.time()
print(tripenthex(286))
print(time.time() - start)
#1533776805 in 0.02595973014831543 secs