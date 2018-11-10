from string import ascii_letters,digits
from random import choice
all_chs = ascii_letters + digits
def rand_pass(n,all_chs):
    res = ''
    for i in range(n):
        ch = choice(all_chs)
        res += ch
    return res
if __name__ == '__main__':
    print(rand_pass(8,all_chs))
    print(rand_pass(4,ascii_letters))
    print(rand_pass(8,digits))