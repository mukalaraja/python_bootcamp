from tkinter import *

def button_clicked():
  print("I got clicked")
  new_text = input.get()
  my_label.config(text=new_text)

window = Tk()
window.title("My first GUI")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)


my_label = Label(text="I Am Label", font=("arial", 24, "bold"))


#Label
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)


new_button = Button(text="new_button")
new_button.grid(column=2, row=0)

#Entry
input = Entry()
input.grid(column=3, row=2)
