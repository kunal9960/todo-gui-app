import functions
import PySimpleGUI as sg
import time

sg.theme("DarkBlue17")

clock = sg.Text('', key="Clock")
label = sg.Text("Type in a to-do")  # creates a label in the window
input_box = sg.InputText(tooltip="Enter todo", key="todo", size=46)
add_button = sg.Button("ADD", size=10)  # creates a button as an event
list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(56, 10),
                      highlight_background_color='#2a325d')
edit_button = sg.Button("EDIT", size=10)
complete_button = sg.Button("DELETE", size=10)
exit_button = sg.Button("EXIT", size=10)

layout = [
    [clock],
    [label],
    [input_box, add_button],
    [list_box],
    [edit_button, complete_button, exit_button]
]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Consolas', 14))
# inner list represents that all items are in the same row

while True:
    event, values = window.Read(timeout=200)  # Displays the window
    window["Clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
#    print(event)   event is the label of the button
#    print(values)   values is whole dictionary
    match event:
        case "ADD":
            todos = functions.get_todos()  # gets the list from todos.txt
            new_todo = values['todo'] + "\n"
            new_todo = new_todo.title()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)  # updating listbox in real time

        case "EDIT":
            try:
                todo_to_edit = values['todos'][0]  # [0] = to convert list value of todos into str
                new_todo = values['todo']
                new_todo = new_todo.title()
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)  # updating listbox in real time
            except IndexError:
                sg.popup("Please select an item first", font=("Consolas", 13))

        case "DELETE":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)  # updating listbox in real time
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Consolas", 13))

        case "EXIT":
            break

        case "todos":  # case when we only select something from the list box
            window['todo'].update(value=values['todos'][0])  # updating the input box when we select list

        case sg.WIN_CLOSED:
            break

window.close()
