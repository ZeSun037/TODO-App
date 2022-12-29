import time
import function
# Press the green button in the gutter to run the script.
now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
        user_action = input("Type show, add, edit, complete or exit")

        if user_action.startswith("add"):
            todo = user_action[4:]

            todos = function.getListTodos()

            todos.append(todo + '\n')

            function.writeListTodos()

        elif user_action.startswith('show'):
            todos = function.getListTodos()

            for ind, item in enumerate(todos):
                item = item.strip('\n')
                row = f'{ind + 1}-{item}'
                print(row)

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:]) - 1

                todos = function.getListTodos()

                newTodo = input("Enter new todo: ")
                todos[number] = newTodo + '\n'

                function.writeListTodos()

            except ValueError:
                print("Invalid argument. Format: \'edit num\'")
                continue
        elif user_action.startswith("exit"):
            print("Finishing operation.")
            break

        else:
            print("Invalid input, aborting.")
            continue




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
