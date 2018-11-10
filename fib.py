def gen_fib(l):
    fib = [0,1]
    for i in range(l - len(fib)):
        fib.append(fib[-1] + fib[-2])
    return fib
n = int(input('length:'))
if __name__ == '__main__':
    print(gen_fib(n))

