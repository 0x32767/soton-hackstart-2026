from tkinter.messagebox import askyesno

from guizero import App, Window, Text, PushButton, TextBox, Box, ListBox, info, question, error, select_file
from soton_hackstart_2026 import run

program_text = ""
save_program_text = ""
save_file = None
code_box = None

def run_code():
    code_box.value
    run(code_box.value, get_input, display_output)

def open_project():
    global save_file
    open_window()
    save_file = select_file()
    with open(save_file, "r") as file:
        code_box.clear()
        code_box.append(file.read())

def save_project():
    global save_file
    with open(save_file, "w") as file:
        file.write(code_box.value)

def get_input():
        return question("Program Input", "Please input one character")

def display_output(text):
        global program_text
        program_text += text
        output_box.clear()
        output_box.append(program_text)

def open_window():
    window = Window(app, title="Project")

    options_box = Box(window, height="fill", align="left")
    global run_button
    run_button = PushButton(options_box, text="Run", align="top", command=run_code)
    global save_button
    save_button = PushButton(options_box, text="Save", align="top", command=save_project)

    project_title_box = Box(window, width="fill", align="top", border=True)
    project_title = Text(project_title_box, text="Project", align="left")

    global code_box
    code_box = TextBox(window, height="15", width="fill", align="top", multiline=True)
    global output_box
    output_box = TextBox(window, height="15", width="fill", align="top", multiline=True)

app = App(title="Main menu", bg="blue")

file_box = Box(app, height="fill", align="left")
new_button = PushButton(file_box, text="New", align="top", command=open_window)
open_button = PushButton(file_box, text="Open", align="top", command=open_project)

about_text = Text(app, text="Bramble", align="top")
about_text.text_color = "white"
about_text.text_size = "60"
more_about = Text(app, text="Twisting your code", align="top")
more_about.text_color = "white"


app.display()