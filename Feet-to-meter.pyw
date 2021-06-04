from tkinter import Tk, Button,Label, DoubleVar , Entry

window=Tk()
window.title("feet 2 meter app")
window.configure(background="#0be881")
window.geometry("320x225")
window.resizable(width=False,height=False)


def convert():
    value=float(ft_entry.get())
    meter=value * 0.3048
    mt_val.set("%.4f"%meter)

def clear():
    ft_value.set("")
    mt_val.set('')


ft_lb1= Label(window,text="Feet",bg="purple",fg="white",width=14)
ft_lb1.grid(column=0,row=0,padx=15,pady=15)

ft_value=DoubleVar()
ft_entry= Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,"end")


mt_lb= Label(window,text="Meter",bg="orange",fg="black",width=12)
mt_lb.grid(column=0,row=2,padx=15,pady=15)

mt_val=DoubleVar()
mt_entry= Entry(window,textvariable=mt_val,width=12)
mt_entry.grid(column=1,row=2)
mt_entry.delete(0,'end')


cnvert_btn= Button(window,text="Convert",bg="white",fg="black",width=10,command=convert)
cnvert_btn.grid(column=0,row=4,padx=15)


clear_btn= Button(window,text="Clear",bg="grey",fg="red",width=8,command=clear)
clear_btn.grid(column=1,row=4,padx=15)





window.mainloop()
