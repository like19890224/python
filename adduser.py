import subprocess
from randpass import all_chs,rand_pass
def useradd(username,passwd,fname):
    subprocess.call('useradd %s'% username,shell=True)
    subprocess.call('echo %s |passwd --stdin %s'% (passwd,username),shell=True)
    info = '''userinfo:
    username:%s
    userpass:%s
    '''
    with open(fname,'a') as fobj:
        fobj.write(info % (username,passwd))
if __name__ == '__main__':
    useradd('like',rand_pass(8,all_chs),'/tmp/userinfo.txt')