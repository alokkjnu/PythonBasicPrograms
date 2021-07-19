import tkinter as tk
from tkinter.font import BOLD
import tkinter.ttk as ttk
import requests
# https://api.exchangeratesapi.io/latest?base=USD&symbols=USD,INR
#http://api.exchangeratesapi.io/v1/latest?access_key=b5c489d672de81399363cd6dff04dc17&base=USD&symbols=USD,INR
base_url = "https://api.exchangeratesapi.io/latest"

def convert_pressed():
    amount = input_text.get()
    from_curr = source_value.get()
    to_curr = target_value.get()
    main_url = base_url + "?access_key=b5c489d672de81399363cd6dff04dc17&base=" +from_curr+"&symbols="+from_curr+"," +to_curr
    print(main_url)
    req = requests.get(main_url)
    result = req.json()
    print(result["rates"][from_curr])
    print(result["rates"][to_curr]) 
    from_result = result["rates"][from_curr]
    to_result = result["rates"][to_curr]
    converted_amount = round(float(amount)*to_result)
    conversion_label.config(text=str(converted_amount)+" "+to_curr)

if __name__ =='__main__':
    main_window = tk.Tk()
    main_window.title("Currency Converter")
    main_window.geometry("500x300")

    intro_lable = tk.Label(main_window,text="Welcome to live currency converter",bg="blue",
    fg="white",relief=tk.RAISED,borderwidth=3)
    intro_lable.config(font=("Courier",15,BOLD))
    main_window.grid_columnconfigure(0,weight = 1 )
    intro_lable.grid(row=1,)

    input_text = tk.StringVar()

    currency_field = tk.Entry(main_window,justify="right",textvariable=input_text)
    currency_field.grid(row=2,padx=5,pady=5)

    country_code = ["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC","BTN","BWP","BYN","BYR","BZD","CAD","CDF","CHF","CLF","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","CUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LDR","LSL","LTL","LVL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TID","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPF","YER","ZAR","ZMK","ZMW","ZWL"]
    source_value = tk.StringVar()

    source_value_selection = ttk.Combobox(main_window,values=country_code,textvariable=source_value)
    source_value_selection.current(0)
    source_value_selection.grid(row=3)
    
    target_value = tk.StringVar()
    
    target_value_selection = ttk.Combobox(main_window,values=country_code,textvariable=target_value)
    target_value_selection.current(1)
    target_value_selection.grid(row=4)

    convert_button = tk.Button(main_window,text="Convert",height=1,width=7,command=lambda:convert_pressed())
    convert_button.grid(row=5)

    conversion_label = tk.Label("")
    conversion_label.grid(row=6)
    
    main_window.mainloop()
