import tkinter as tk
from tkinter.constants import COMMAND

def click_now():
    print("pressed radio button ",var.get())

main_winndow = tk.Tk()
main_winndow.title("Radio Button")
var = tk.IntVar()
radiao_button_1 = tk.Radiobutton(main_winndow,text = "Red", command = click_now, variable=var, value=1)
radiao_button_1.pack()
radiao_button_2 = tk.Radiobutton(main_winndow,text = "yellow", command = click_now,variable=var, value=2)
radiao_button_2.pack()
radiao_button_3 = tk.Radiobutton(main_winndow,text = "green", command = click_now,variable=var, value=3)
radiao_button_3.pack()
main_winndow.mainloop()