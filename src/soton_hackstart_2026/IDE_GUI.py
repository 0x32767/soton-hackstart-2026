from guizero import App, Window, Text, PushButton, TextBox, Box, ListBox






app = App(title="Main menu", bg="blue")
window = Window(app, title="Project")


file_box = Box(app, height="fill", align="left")
new_button = PushButton(file_box, text="New", align="top")
open_button = PushButton(file_box, text="Open", align="top")

options_box = Box(window, height="fill", align="left")
save_button = PushButton(options_box, text="Save", align="top") #command=save_project)

project_title_box = Box(window, width="fill", align="top", border=True)
project_title = Text(project_title_box, text="Project", align="left")

TextBox(window, height="fill", width="fill", align="top", multiline=True)





app.display()