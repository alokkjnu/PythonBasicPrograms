import tkinter as tk
main_window = tk.Tk()
main_window.geometry("500x300")
label_1 = tk.Label(main_window,text="Hello Python",bg="green",fg="white")
label_1.grid(row=0, column=0, padx= 10, pady=10)

label_2 = tk.Label(main_window,text="Hello Python2",bg="green",fg="white")
label_2.grid(row=0, column=1, padx= 10, pady=10)

label_3 = tk.Label(main_window,text="Hello Python3",bg="green",fg="white")
label_3.grid(row=0, column=2, padx= 10, pady=10)

label_4 = tk.Label(main_window,text="Hello Python4",bg="green",fg="white")
label_4.grid(row=1, column=0, padx= 10, pady=10, columnspan=2)

label_5 = tk.Label(main_window,text="Hello Python5",bg="green",fg="white")
label_5.grid(row=1, column=2, padx= 10, pady=10, rowspan=2)



main_window.mainloop()