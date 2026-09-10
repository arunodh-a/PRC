import tkinter as tk
import time
def update_time():
    current_time=time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000,update_time)
root=tk.Tk()
root.title("clock")
label=tk.Label(root,font=('Arial',60,"bold"),bg="black",fg="cyan")
label.pack(padx=20,pady=20)
update_time()
root.mainloop()
