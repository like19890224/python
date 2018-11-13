from random import choice
from string import ascii_letters,digits
from functools import partial
all_chs = ascii_letters + digits

def gen_pass(n,all_chs):  #n=8默认参数时报错
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result
default = partial(gen_pass,n=8)
if __name__ == '__main__':
    print(default(all_chs=all_chs))
    print(gen_pass(4,ascii_letters))