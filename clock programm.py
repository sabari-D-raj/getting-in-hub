from tkinter import*
from time import*
def sabariclocktime():
    timestring=strftime("%H:%M:%S %p")
    timelabel.configure(text=timestring)
    datestring=strftime("%B %d,%Y")
    date.configure(text=datestring)
    #daystring=strftime("%")
    #day.configure(text=datestring)
    window.after(1000,sabariclocktime)

window=Tk()
timelabel=Label(window,font=("Arial",50),fg="green",bg="black")
timelabel.pack()
date=Label(window,font=("Ink free",25))
date.pack()
#day=Label(window,font=("Ink free",25))
#day.pack()
sabariclocktime()
window .mainloop()
