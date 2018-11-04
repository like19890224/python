stack = []
def push_it():
    data = input('请输入内容：')
    stack.append(data)
def pop_it():
    if stack:
        print('poped is %s:'% stack.pop())
    else:
        print('empty stack')
def show_it():
    print(stack)
def menu():
    prompt = '''
    0:push_it
    1:pop_it
    2:show_it
    3:quit
    Please input your choice(0,1,2,3)
    '''
    while True:
        choice = input(prompt)
        zidian = {'0':push_it,'1':pop_it,'2':show_it,}
        if choice not in '0123':
            continue
        if choice == '3':
            break
        zidian[choice]()

if __name__ == '__main__':
    menu()