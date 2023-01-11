import function

from PySimpleGUI import *
from PySimpleGUI import __version__

text = Text("Type in a Todo")
input_box = InputText(tooltip="Enter a Todo", key='todo')
add_button = Button("Add")
list_box = Listbox(values=function.getListTodos(),
                   key='todos', enable_events=True, size=[45, 10])

edit_button = Button("Edit")

delete_button = Button("Delete")

window = Window("Your Todos", layout=[[text],
                [input_box, add_button, edit_button, delete_button], [list_box]],
                font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = function.getListTodos()
            todos.append(values['todo'] + '\n')
            function.writeListTodos(todos)
            window['todo'].update(value="")
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = function.getListTodos()
            ind = todos.index(todo_to_edit)
            todos[ind] = new_todo + '\n'
            function.writeListTodos(todos)

            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Delete':
            todo_to_delete = values['todo']
            todos = function.getListTodos()

            ind = todos.index(todo_to_delete)
            if todos[ind]:
                del todos[ind]

            window['todo'].update(value="")
            window['todos'].update(values=todos)

        case WIN_CLOSED:
            break

window.close()
