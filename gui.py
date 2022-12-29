import function

from PySimpleGUI import *
from PySimpleGUI import __version__

text = Text("Type in a Todo")
input_box = InputText(tooltip="Enter a Todo")
add_button = Button("Add")


window = Window("Your Todos", layout=[[text], [input_box, add_button]])
window.read()
window.close()
