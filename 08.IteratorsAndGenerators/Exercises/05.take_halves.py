def solution():
    def integers():
        start = 1
        while True:
            yield start
            start += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        ll = []
        for _ in range(n):
            ll.append(next(seq))
        return ll

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
