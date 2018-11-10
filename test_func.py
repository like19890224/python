# def foo(name,age):
#     print('%s is %d years old' % (name,age))
# foo(age=23,name='like')
#
# def foo(a,b,*c):
#     print('a is: ',a)
#     print('b is: ',b)
#     print('c is: ',c)
# foo('a','b','c',669798,'daf')
# def foo(a,b,*c,**d):
#     print('a is: ', a)
#     print('b is: ',b)
#     print('c is: ',c)
#     print('d is: ',d)
# foo(1,2,name='bob',age=18)
# def foo(x,y):
#     print(x,y)
# foo(*[1,2])
# def foo(name,age):
#     print('%s is %d years old' %(name,age))
#
# foo(**{'name':'like','age':23})
# fun = lambda x,y:x+y
# print(fun(3,4))
# print(fun)
# data = filter(lambda x:x%2,[i for i in range(11)])
# for num in data:
#     print(num,end=' ')

# data = map(lambda x:x+2,[i for i in range(11)])
# for num in data:
#     print(num,end=' ')
from functools import reduce
data = reduce(lambda x,y:x+y,[i for i in range(101)])
print(data)