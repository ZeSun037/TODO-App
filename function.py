def getListTodos(file='todos.txt'):
    with open(file, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def writeListTodos(todos_arg, fileDest='todos.txt'):
    with open(fileDest, 'wr') as file:
        file.writelines(todos_arg)
