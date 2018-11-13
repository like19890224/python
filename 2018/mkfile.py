import os


def get_fname():
    while True:
        fname = input('filename: ')
        if not os.path.exists(fname):
            break
        print('%s already exists,try again' % fname)
    return fname


def get_content():
    content = []
    print('输入数据，输入end结束')
    while True:
        data = input('>>>')
        if data == 'end':
            break
        content.append(data)
    return content


def wfile(fname,content):
    with open(fname,'w') as fobj:
        fobj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname, content)
