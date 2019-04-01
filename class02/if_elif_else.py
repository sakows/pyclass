def spam(a):
    return 42/a
try:
    print(spam(3.0))
    print(spam(0))
    print(spam(6))
    print(spam(12))


except ZeroDivisionError:
    print('great')
    continue
