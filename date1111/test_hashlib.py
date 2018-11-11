import hashlib
# m = hashlib.md5()
# print(m)
# m.update(b'hello world')
# print(m.hexdigest())
# def check_md5(fname):
#     m = hashlib.md5()
#     with open(fname,'rb') as f:
#         while True:
#             data = f.read(4096)
#             if not data:
#                 break
#             m.update(data)
#         return m.hexdigest()
# if __name__ == '__main__':
#     print(check_md5('/etc/passwd'))
import tarfile
# tar = tarfile.open('/tmp/demo.tar.gz','w:gz')
# tar.add('/etc/hosts')
# tar.add('/etc/passwd')

tar = tarfile.open('/tmp/demo.tar.gz','r:gz')
tar.extractall()
tar.close()