import tkinter
from tkinter import *
def calculate_bill():
    fries_qty=int(fries_entry.get()or 0)
    lunch_qty=int(lunch_entry.get()or 0)
    burger_qty=int(burger_entry.get()or 0)
    drinks_qty=int(drinks_entry.get()or 0)
    total=(fries_qty*2+lunch_qty*2+burger_qty*2.5+drinks_qty*1)
    bill_window=Toplevel(root)
    bill_window.title('Bill Details')
    Label(bill_window,text='Bill Amount',font=('Arial',16,'bold')).pack(pady=10)
    bill_details=(
        f'Fries Meal:{fries_qty} x $2 = ${fries_qty*2}\n'
        f'Lunch Meal:{lunch_qty} x $2 = ${lunch_qty*2}\n'
        f'Buger Meal:{burger_qty} x $2.5 = ${burger_qty*2.5}\n'
        f'Drinks Meal:{drinks_qty} x $1 = ${drinks_qty*1}\n'
        F'\n Total : ${total:.2f}'
    )
    Label(bill_window,text=bill_details,font=('Arial',16),justify='left').pack(pady=10)
    Button(bill_window,text="close",command=bill_window.destroy).pack(pady=10)
root=Tk()
root.title("restaurant Management App")
root.geometry('400x400')
header_label=Label(root,text="Maneet'sr Restaurant",font=('Arial',16,'bold'))
header_label.pack(pady=10)
frame=Frame(root)
frame.pack(pady=10)
Label(frame,text="Fries Meal ($2) : ").grid(row=0,column=0,pady=5,sticky='w')
fries_entry=Entry(frame)
fries_entry.grid(row=0,column=1,pady=5)

Label(frame,text="Lunch Meal ($2) : ").grid(row=1,column=0,pady=5,sticky='w')
lunch_entry=Entry(frame)
lunch_entry.grid(row=1,column=1,pady=5)

Label(frame,text="Burger Meal ($2.5) : ").grid(row=2,column=0,pady=5,sticky='w')
burger_entry=Entry(frame)
burger_entry.grid(row=2,column=1,pady=5)

Label(frame,text="Drinks ($1) : ").grid(row=3,column=0,pady=5,sticky='w')
drinks_entry=Entry(frame)
drinks_entry.grid(row=3,column=1,pady=5)
place_order_button=Button(root,text="Place Order",command=calculate_bill)
place_order_button.pack(pady=20)
root.mainloop()