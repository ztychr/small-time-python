import argparse
import time

def isPrime(number):
    if number == 0 or number == 1:
        return False
    for i in range(number):
        if not (i == 0 or i == 1):
            if (number/i)%1 == 0:
                ½return False
    return True

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("range", help="The range to calculate if prime", type=int)
    args = parser.parse_args()

    start = time.time()
    for i in range(args.range):
        if isPrime(i):
            print("{} is a prime.".format(i))

    print("\nTime for calculation: " + str(time.time() - start) + " seconds.")

if __name__ == "__main__":
    Main()
