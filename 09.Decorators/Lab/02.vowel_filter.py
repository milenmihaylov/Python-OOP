import functools


def is_vowel(c: str):
    vowels = 'aeiouy'
    if c.lower() in vowels:
        return True
    return False


def vowel_filter(function):
    @functools.wraps(function)
    def wrapper():
        return [x for x in function() if is_vowel(x)]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
