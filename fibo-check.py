
while True:
    try:
        un = int(raw_input("Check if this number is in the fibo. sequence: "))
        break
    except:
        pass


def fibo(p, n):
    if n == un:
        return True
    return fibo(n, n + p)

try:
    print fibo(1, 1)
except RuntimeError:
    print False
