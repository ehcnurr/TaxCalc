from tkinter import *

#backend code

def calculate():
    try:
        gross_amount = float(entry.get())
        vat = (gross_amount * 0.05) / 1.12
        ewt = vat / 5
        net = gross_amount - (vat + ewt)

        vat_result.delete(0, END)
        vat_result.insert(0, format(vat, ".2f"))

        ewt_result.delete(0, END)
        ewt_result.insert(0, format(ewt, ".2f"))
        
        net_entry.delete(0, END)
        net_entry.insert(0, format(net, ".2f"))
        
    except ValueError:  
        vat_result.delete(0, END)
        vat_result.insert(0, "Invalid input.")

        ewt_result.delete(0, END)
        ewt_result.insert(0, "Invalid input.")

        net_entry.delete(0, END)
        net_entry.insert(0, "Invalid input.")

#frontend code
window = Tk()
window.title("VAT Calculator")
window.geometry("700x500")
window.resizable(False, False)

#icon = PhotoImage(file="calc.png")
#window.iconphoto(True, icon)

text = Label(window, text = "Enter gross amount:", font = ("Arial", 20))
text.pack()

entry = Entry(window, font=("Arial", 20), justify=CENTER)
entry.pack()
entry.bind("<Return>", calculate)

submit_button = Button(window, text="Calculate", command=calculate).pack()

vat_label = Label(window, text="VAT: ", font=("Arial", 20))
vat_label.pack(pady=(30,0))

vat_result = Entry(window, font=("Arial", 20), justify=CENTER)
vat_result.pack()

ewt_label = Label(window, text="EWT: ", font=("Arial", 20))
ewt_label.pack(pady=(30, 0))

ewt_result = Entry(window, font=("Arial", 20), justify=CENTER)
ewt_result.pack()

net_amount = Label(window, text="Net Amount: ", font=("Arial", 20))
net_amount.pack(pady=(30, 0))

net_entry = Entry(window, font=("Arial", 20), justify=CENTER)
net_entry.pack()

window.mainloop()