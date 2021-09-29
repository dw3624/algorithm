def  fibonnaci(n):

    if n == 0 or n == 1:
        print(n)
        return n

    before = 0
    current = 1

    i = 2
    while i <= n:
        before, current = current, before + current
        # print(before, current)
        i += 1

    print(current)
    return current

fibonnaci(9)
