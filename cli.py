# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_prompt = input("Type add, show, edit, complete or exit: ")
    user_prompt = user_prompt.strip()

    if user_prompt.startswith('add'):
        todo = user_prompt[4:]  # slicing the input

        todos = functions.get_todos()

        todos.append(todo + '\n')
        functions.write_todos(todos)

    elif user_prompt.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.capitalize()
            row = f"{index + 1}.{item}"
            print(row)

    elif user_prompt.startswith('edit'):
        try:
            number = int(user_prompt[5:])
            print(number)
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("You should've entered the number of the todo.")
            continue

    elif user_prompt.startswith('complete'):
        try:
            number = int(user_prompt[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_prompt.startswith('exit'):
        break

    else:
        print("Hey, you typed a wrong command")

print("Bye!")
