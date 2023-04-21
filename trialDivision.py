import time
import tracemalloc
from memory_profiler import profile

import logging
# https://github.com/pythonprofilers/memory_profiler/blob/master/examples/reporting_logger.py
# create logger
logger = logging.getLogger('memory_profile_log')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler("trial_memory_profile16.log")
fh.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)

from memory_profiler import LogFile
import sys
sys.stdout = LogFile('memory_profile_log', reportIncrementFlag=False)

def trialDivision(n):
    i = 2
    k = int(n ** 0.5)
    while (i <= k):
        if (n % i == 0):
                return i
        i += 1
    return n

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
    print("The Trial Division Algorithm has completed. The running time was ", end="")
    print(str(hours) + " Hours, " + str(minutes) + " Minutes, and " + str(seconds) + " Seconds.")

def trialDivisionHelper(num):
    start_time = time.time()
    tracemalloc.start()
    primeFactorization = []
    primeFactor = trialDivision(num)
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
    f = open("16RSA.txt", "r")
    bitSize = int(f.readline())
    print("Testing Values of Size: " + str(bitSize) + " bits.")
    totalTime = 0
    for i in range(5):
        n = int(f.readline())
        print("Number = " + str(n))
        totalTime += trialDivisionHelper(n)
        print("\n")

    print("------------------------Total Time------------------------")
    print_time(totalTime)

if __name__ == '__main__':
    mainHelper()
