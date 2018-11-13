def blocks(fobj):
    block = []
    counter = 0
    for i in  fobj:
        block.append(i)
        counter+=1
        if counter == 10:
            yield block
            block = []
            counter = 0
    if block:
        yield block
if __name__ == '__main__':
    fobj = open('/tmp/passwd')
    for i in blocks(fobj):
        print(i)