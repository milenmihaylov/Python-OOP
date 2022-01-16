def get_primes(nums: list):
    for n in nums:
        if n > 1:
            for d in range(2, n):
                if n % d == 0:
                    break
            else:
                yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
