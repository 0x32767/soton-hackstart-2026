from guizero import App, Window, Text, PushButton, TextBox, Box, ListBox, info, question
from soton_hackstart_2026 import run

program_text = ""

def run_code():
    code_box.value
    run(code_box.value, get_input, display_output)



def get_input():
    return question("Program Input", "Please input one character")

def display_output(text):
    global program_text
    program_text += text
    output_box.clear()
    output_box.append(program_text)




app = App(title="Main menu", bg="blue")
window = Window(app, title="Project")


file_box = Box(app, height="fill", align="left")
new_button = PushButton(file_box, text="New", align="top")
open_button = PushButton(file_box, text="Open", align="top")

options_box = Box(window, height="fill", align="left")
run_button = PushButton(options_box, text="Run", align="top", command=run_code)
save_button = PushButton(options_box, text="Save", align="top") #command=save_project)

project_title_box = Box(window, width="fill", align="top", border=True)
project_title = Text(project_title_box, text="Project", align="left")

code_box = TextBox(window, height="15", width="fill", align="top", multiline=True)
output_box = TextBox(window, height="15", width="fill", align="top", multiline=True)

program_text = ""





app.display()