def reverse_text_v1(text):
    for i in range(-1, len(text) * (-1) - 1, -1):
        ch = text[i]
        yield ch


def reverse_text_v2(text):
    for i in range(1, len(text) + 1):
        ch = text[i * (-1)]
        yield ch


def reverse_text_v3(text):
    return (text[i] for i in range(len(text) - 1, - 1, -1))


for char in reverse_text_v3("step"):
    print(char, end='')
