import function

from PySimpleGUI import *
from PySimpleGUI import __version__

text = Text("Type in a Todo")
input_box = InputText(tooltip="Enter a Todo", key='todo')
add_button = Button("Add")


window = Window("Your Todos", layout=[[text],
                [input_box, add_button]],
                font=('Helvetica', 20))
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = function.getListTodos()
            todos.append(values['todo'] + '\n')
            function.writeListTodos(todos)
        case WIN_CLOSED:
            break

window.close()
