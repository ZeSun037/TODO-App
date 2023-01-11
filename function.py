import os

file_path = 'todos.txt'

mode = 'a' if os.path.exists(file_path) else 'w'
with open(file_path, mode) as f:
    pass

def getListTodos(file=file_path):
    with open(file, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def writeListTodos(todos_arg, fileDest=file_path):
    with open(fileDest, 'w+') as file:
        file.writelines(todos_arg)
