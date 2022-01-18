def f(x):
    def internal_f(y):
        return x + y

    internal_f.initial_value = x
    return internal_f


f1 = f(1)
print(f(1)(2))

f2 = f(2)

print(f1.initial_value)
print(f2.initial_value)
