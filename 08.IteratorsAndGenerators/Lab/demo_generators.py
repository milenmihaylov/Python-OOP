from math import sqrt


def is_primes(number):
    for x in range(2, int(sqrt(number))+1):
        if number%x==0:
            return False
    return True

def primes_gen(max_number):
    number = 2
    while number <= max_number:
        if is_primes(number):
            yield number
        number+=1

def custom_range(start, end):
    for i in range(end):
        yield i
        # start += 1


gen_1 = custom_range(1, 8)
for j in gen_1:
    print(j)
