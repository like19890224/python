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
# print(func(5))
# print(func(6))
# def color(func):
#     def red():
#         return '\033[31;1m%s\033[0m' % func()
#     return red
# @color
# def hello():
#     return 'hello world'
# @color
# def welcome():
#     return 'Welcome to China!'
# print(hello())
# print(welcome())
# def choice_color(c):
#     def color(func):
#         def red(*args):
#             return '\033[31;1m%s\033[0m' % func(*args)
#         def green(*args):
#             return '\033[32;1m%s\033[0m' % func(*args)
#         adict = {'red':red,'green':green}
#         return adict[c]
#     return color
# @choice_color('red')
# def hello(word):
#     return 'hello %s' % word
# print(hello('like'))
# @choice_color('green')
# def welcome():
#     return 'what about you?'
# print(welcome())
def mygen():
    yield 'hello'
    a = 10+20
    yield a
    yield [1,2,3]
print(mygen())
m = mygen()
for i in m:
    print(i)