from random import choice, randint
from string import digits

cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}

nums = [randint(0, 100) for i in range(2)]
nums.sort(reverse=True)
op = choice('-+')
result = cmds[op](*nums)
prompt = 'please input result: %d %s %d' % (nums[0], op, nums[1])
answer = int(input(prompt))
if answer == result:
    print('you won!')
else:
    print('you lose!')
