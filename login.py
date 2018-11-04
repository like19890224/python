userdb = {}
def register():
    username = input('input username:')
    if username not in userdb:
        userpwd = input('input userpwd')
        userdb[username] = userpwd
    else:
        print('username already exists')
def login():
    username = input('input username:')
    userpwd = input('input userpwd')
    if userdb.get(username) != userpwd:
        print('incorrect')
    else:
        print('login successfully')
def menu():
    cmds = {'0':register,'1':login}
    prompt = '''
    0:register
    1:login
    2:quit
    Please input your choice(0/1/2)
    '''
    while True:
        choice = input(prompt)
        if choice not in '012':
            continue
        elif choice == '2':
            break
        cmds[choice]()
if __name__ == '__main__':
    menu()
