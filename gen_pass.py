from random import choice
from string import ascii_letters,digits

all_chs = ascii_letters + digits

def gen_pass(n,all_chs):  #n=8默认参数时报错
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    print(gen_pass(8,all_chs))
    print(gen_pass(4,ascii_letters))