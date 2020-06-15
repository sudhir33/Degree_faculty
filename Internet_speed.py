#import speedtest as ST
from speedtest import *
from tkinter import *
from tkinter import messagebox

def download():
    st=Speedtest()
    ds=str(st.download())
    e1.delete(0,END)
    e1.insert(0,"Download Speed "+ds[0:2]+'MBPS')
    val="Upload Speed "+ds[0:2]+'MBPS'
    l1.config(text=val)
    #print(ds[0:2]+'MBPS')
    #msg=messagebox.showinfo("Download Speed",ds[0:2]+'MBPS')

def upload():
    st=Speedtest()
    ds=str(st.upload())
    #print(ds[0:2]+'MBPS')
    e2.delete(0,END)
    e2.insert(0,"Upload Speed "+ds[0:2]+'MBPS')
    val="Upload Speed "+ds[0:2]+'MBPS'
    l2.config(text=val)
    #msg=messagebox.showinfo("Upload Speed",ds[0:2]+'MBPS')

root=Tk()
root.geometry("400x400")
b1=Button(root,text="Dowdload",command=download)
e1=Entry(root,width=40)
l1=Label(root)
l1.pack()
l2=Label(root)
l2.pack()
e1.pack()
e2=Entry(root,width=40)
e2.pack()
b1.pack()
b2=Button(root,text="Upload",command=upload)
b2.pack()
root.mainloop()
