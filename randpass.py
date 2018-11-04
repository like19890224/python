from string import ascii_letters,digits
from random import choice

all_chs = ascii_letters+digits

def rand_pass(n,chrs):
    #n代表循环的次数,chrs代表从哪个字符串中随机抽取字符
    res = ''
    for i in range(0,n):
        ch = choice(chrs)
        res += ch
    return res
if __name__ == '__main__':
    print(rand_pass(8,all_chs))
    print(rand_pass(4,ascii_letters))