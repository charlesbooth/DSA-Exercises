def three():
    print('three')

def two():
    three()
    print('two')

def one():
    two()
    print('one')

#one()

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(4))