from lab2.task6_1 import memoize

@memoize
def count_paths(m, n):
    if m == 1 or n == 1:
        return 1

    return count_paths(m - 1, n) + count_paths(m, n - 1)


print(count_paths(3, 3))

# O(2^(m+n)) и O(m * n)