import pyshorteners
from tkinter import *

#s = pyshorteners.Shortener()
#print(s.tinyurl.short(url))
def shorturl():
    url=e1.get()
    s = pyshorteners.Shortener()
    val=s.tinyurl.short(url)
    e2.delete(0,END)
    e2.insert(0,val)
    e1.delete(0,END)


root=Tk()
root.geometry("400x400")
e1=Entry(root,width=50)
e1.pack()
e2=Entry(root,width=50)
e2.pack()
b1=Button(root,text="Shorten Url",command=shorturl)
b1.pack()

root.mainloop()
