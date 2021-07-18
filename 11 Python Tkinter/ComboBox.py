import tkinter as tk
import tkinter.ttk as ttk

def on_click(a):
    print(combo_box1.get())
    

main_window = tk.Tk()
main_window.geometry("500x300")
combo_box1 = ttk.Combobox(main_window,values=[1,2,3,4])
combo_box1.bind("<<ComboboxSelected>>", on_click)
combo_box1.current(0)
#combo_box1['value']= [5,6,7]
combo_box1.pack()
main_window.mainloop()