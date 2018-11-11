# from functools import partial
# def foo(a,b,c,d,e):
#     return a+b+c+d+e
# add = partial(foo,a=10,b=20,c=30,d=40)
# print(add(e=5))
def func(n):
    if n == 1:
        return n
    return n*func(n-1)
#func(5) 5*func(4)
#5*4*func(3)
#5*4*3*func(2)
#5*4*3*2*func(1)
print(func(5))
print(func(6))