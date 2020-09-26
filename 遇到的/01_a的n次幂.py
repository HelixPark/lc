
def pow(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    tmp = 1
    while n > 1:
        if n % 2 != 0:
           tmp *= a
        a *= a
        n = n // 2

    return a*tmp

a, n = 2, 13
print(pow(a, n))