with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()


def count_spaces_iter(s):
    count = 0
    for char in s:
        if char == " ":
            count += 1
    return count


def count_spaces_rec(s):
    if len(s) == 0:  # терминальное условие
        return 0
    if s[0] == " ":
        return 1 + count_spaces_rec(s[1:])
    else:
        return count_spaces_rec(s[1:])


print("Количество пробелов (цикл):", count_spaces_iter(text))

try:
    print("Количество пробелов (рекурсия):", count_spaces_rec(text))
except RecursionError:
    print("RecursionError")

print("Количество пробелов (рекурсия):", count_spaces_rec(text[982:])) # len(text) = 1980
