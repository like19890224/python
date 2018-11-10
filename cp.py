import sys
def copy(src_fname,des_fname):
    src_fobj = open(src_fname,'rb')
    des_fobj = open(des_fname,'wb')
    while True:
        data = src_fobj.read(4096)
        if not data:
            break
        des_fobj.write(data)
    src_fobj.close()
    des_fobj.close()
copy(sys.argv[1],sys.argv[2])
#执行方式 cp.py  /etc/passwd /tmp/123.txt