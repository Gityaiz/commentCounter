import tkinter

from module import windowwidget as ww

root = tkinter.Tk()
root.geometry("700x500")
app = ww.Application(master=root)
app.mainloop()
