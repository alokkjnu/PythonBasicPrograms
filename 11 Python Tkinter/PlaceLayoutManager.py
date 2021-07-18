import tkinter as tk
main_window=tk.Tk()
main_window.geometry("500x300")

lable = tk.Label(main_window,text="Python",bg="grey")
lable.place(x= 200, y=30)
lable.mainloop()