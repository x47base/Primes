TESTSTEP=4
def main():
    sieve = list(range(0))
    start_limit = int(input("Start Limit: "))
    end_limit = int(input("End Limit: "))
    sieve = list(range(0, end_limit+1)) 
    prime = 2
    while prime <= end_limit:
        if sieve[prime] > 0:
            if prime >= start_limit:
                print(prime)
            multiples_of_the_number = prime * 2
            while multiples_of_the_number <= end_limit:
                sieve[multiples_of_the_number] = 0
                multiples_of_the_number += prime
        prime += 1
    return sieve

if __name__ == '__main__':
    main()
