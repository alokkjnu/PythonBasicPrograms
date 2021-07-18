import tkinter as tk

main_window= tk.Tk()
main_window.geometry("500x300")

for i in range(4):
    for j in range(4):
        lable = tk.Label(main_window,text="Hello Python",bg= "blue", fg= "white")
        lable.grid(row=i,column=j,padx=2,pady=2)

main_window.mainloop()
