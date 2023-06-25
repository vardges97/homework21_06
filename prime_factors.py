def primefactors(n):
    i = 2
    nums = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            nums.append(i)
    if n > 1:
        nums.append(n)
    return nums

test=primefactors(90)
print(test)
