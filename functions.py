import os

file_path = 'todos.txt'

def get_todos(file=file_path):
    with open(file, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_arg, fileDest=file_path):
    with open(fileDest, 'w+') as file:
        file.writelines(todos_arg)
