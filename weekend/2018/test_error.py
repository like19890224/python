# try:
#     n = int(input('please input number:'))
#     res = 100/n
#     print(res)
# except ValueError:
#     print('must be a number!!!')
# except ZeroDivisionError:
#     print('0 not allowed!!!')
# except KeyboardInterrupt:
#     print('bye')
#自定义异常
# age = int(input('please input age:'))
# if not 0<age<120:
#     raise ValueError('age out of range!!!')
# else:
#     print("I'm %s years old" % age)
# assert 10<20,'Wrong'
