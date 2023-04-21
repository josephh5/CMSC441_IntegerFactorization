import random
import math
import time
import tracemalloc
from memory_profiler import profile

import logging
# https://github.com/pythonprofilers/memory_profiler/blob/master/examples/reporting_logger.py
# create logger
logger = logging.getLogger('memory_profile_log')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler("memory_profile68.log")
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)

from memory_profiler import LogFile
import sys
sys.stdout = LogFile('memory_profile_log', reportIncrementFlag=False)

"""
Pollard Rho Algorithm provided by GeeksForGeeks:
https://www.geeksforgeeks.org/pollards-rho-algorithm-prime-factorization/
"""
def modular_pow(base, exponent, modulus):
    result = 1
    while (exponent > 0):
        if (exponent & 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def pollardRho(n, recursiveCount):
    recursiveCount += 1
    if (n == 1):
        return n
    if (n % 2 == 0):
        return 2
    x = (random.randint(0, 2) % (n - 2))
    y = x
    c = (random.randint(0, 1) % (n - 1))
    p = 1
    while (p == 1):
        x = (modular_pow(x, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        y = (modular_pow(y, 2, n) + c + n) % n
        p = math.gcd(abs(x - y), n)
        if (p == n):
            return pollardRho(n, recursiveCount)
    print("Function was called " + str(recursiveCount) + " times.")
    return p

def print_time(time):
    hours = 0
    minutes = 0
    curr_time = time
    while curr_time >= 3600:
        curr_time -= 3600
        hours += 1
    while 3600 >= curr_time >= 60:
        curr_time -= 60
        minutes += 1
    seconds = curr_time
    print("The Pollard Rho Algorithm has completed. The running time was ", end="")
    print(str(hours) + " Hours, " + str(minutes) + " Minutes, and " + str(seconds) + " Seconds.")

def pollardRhoHelper(num):
    start_time = time.time()
    tracemalloc.start()
    primeFactorization = []
    primeFactor = pollardRho(num, recursiveCount=0)
    primeFactorization.append(primeFactor)
    num = num // primeFactor
    primeFactorization.append(num)
    print(primeFactorization)
    tracemalloc.stop()
    print("Memory usage:", tracemalloc.get_traced_memory())
    print_time(int(time.time() - start_time))
    return int(time.time() - start_time)


@profile
def mainHelper():
    f = open("68RSA.txt", "r")
    bitSize = int(f.readline())
    print("Testing Values of Size: " + str(bitSize) + " bits.")
    totalTime = 0
    for i in range(5):
        n = int(f.readline())
        print("Number = " + str(n))
        totalTime += pollardRhoHelper(n)
        print("\n")

    print("------------------------Total Time------------------------")
    print_time(totalTime)

if __name__ == '__main__':
    mainHelper()
