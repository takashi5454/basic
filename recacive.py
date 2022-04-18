#n! = n * (n-1) * (n-2) * 1

def fibonacchi_re(n):
    if n < 2:
        return n
    else:
        return fibonacchi(n-1) + fibonacchi(n-2)


# print(fibonacchi(3))

def fibonacchi(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


for i in range(50):
    print(i, fibonacchi(i))