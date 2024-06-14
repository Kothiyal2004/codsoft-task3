import customtkinter
from tkinter import*
from tkinter import messagebox

app=customtkinter.CTk()
app.title("to do list")
app.geometry("350x450")
app.config(bg="#09112e")

font1=('arial',30,'bold')
font2=('arial',18,'bold')
font3=('arial',10,'bold')
def add_task():
    task=task_entry.get()
    if task:
        task_list.insert(0,task)
        task_entry.delete(0,END)
        save_tasks()
    else:
        messagebox.showerror('Error','enter a task.')
def remove_task():
    selected=task_list.curselection()
    if selected:
        task_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror('error','choose a task to delete.')
def save_tasks():
    with open("tasks.txt","w") as f:
        tasks=task_list.get(0,END)
        for task in tasks:
            f.write(task+"\n")

def load_tasks():
    try:
        with open("tasks.txt","r") as f:
            tasks=f.readline()
            for task in tasks:
                task_list.insert(0,tasks.strip())
    except FileNotFoundError:
     pass
title_label= customtkinter.CTkLabel(app,font=font1,text='to-Do- list',text_color='#fff',bg_color='#09112e')
title_label.place(x=100,y=20)

add_button=customtkinter.CTkButton(app,command=add_task,font=font2,text_color="#fff",text='Add task',fg_color='#06911f',hover_color='#06911f',bg_color='#09112f',cursor='hand2',corner_radius=5,width=120)
add_button.place(x=40,y=80)

remove_button=customtkinter.CTkButton(app,command=remove_task,font=font2,text_color='#fff',text='remove task',fg_color='#96061c',hover_color='#09112c',cursor='hand2',corner_radius=5)
remove_button.place(x=180,y=80)

task_entry=customtkinter.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',width=280)
task_entry.place(x=40,y=160)

task_list=Listbox(app,width=57,height=15,font=font3)
task_list.place(x=60,y=300)
load_tasks()
app.mainloop()