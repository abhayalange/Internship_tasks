#Digital Clock 

from tkinter import *
from tkinter.messagebox import *
from datetime import *
from time import *

root=Tk()
root.geometry("800x600+150+150")
root.configure(bg="steelblue3")
root.title("Digital Clock by Abhay")
f=("Times New Roman", 35, "bold")


tit_lab=Label(root, text="DIGITAL CLOCK", font=f, bg="steelblue3")
tit_lab.place(x=215, y=30)

canvas = Canvas(root, highlightbackground="black", highlightthickness=2, width=750, height=450, bg= "lightslategray")
canvas.place(x=20,y=120)
rectangle1 = canvas.create_rectangle(95, 150, 170, 275, fill='lightgoldenrod')
rectangle2 = canvas.create_rectangle(185, 150, 260, 275, fill='lightgoldenrod')

canvas.create_oval(265,175,285,195,outline = "black",fill = "black")
canvas.create_oval(265,230,285,250 ,outline = "black",fill = "black")

rectangle3 = canvas.create_rectangle(290, 150, 365, 275, fill='lightgoldenrod')
rectangle4 = canvas.create_rectangle(380, 150, 455, 275, fill='lightgoldenrod')

canvas.create_oval(460,175,480,195,outline = "black",fill = "black")
canvas.create_oval(460,230,480,250 ,outline = "black",fill = "black")

rectangle5 = canvas.create_rectangle(485, 150, 560, 275, fill='lightgoldenrod')
rectangle6 = canvas.create_rectangle(575, 150, 650, 275, fill='lightgoldenrod')

rectangle7 = canvas.create_rectangle(500,25,725, 75, fill='lightgoldenrod')
rectangle8 = canvas.create_rectangle(25,365, 275, 425, fill='lightgoldenrod')


d=('Lucida Console', 80, 'bold')
d1=('Lucida Console', 27, 'bold')
var1=canvas.create_text(132.5, 212.5, text="0", fill="black", font=d)
var2=canvas.create_text(222.5, 212.5, text="0", fill="black", font=d)
var3=canvas.create_text(327.5, 212.5, text="0", fill="black", font=d)
var4=canvas.create_text(417.5, 212.5, text="0", fill="black", font=d)
var5=canvas.create_text(522.5, 212.5, text="0", fill="black", font=d)
var6=canvas.create_text(612.5, 212.5, text="0", fill="black", font=d)
var7=canvas.create_text(612.5, 50, text="Monday", fill="black", font=d1)
var8=canvas.create_text(150, 395, text="abhay", fill="black", font=d1)


h1=""
h2=""
m1=""
m2=""
s1=""
s2=""

def clock():
	d=datetime.now()
	h=d.hour
	m=d.minute
	s=d.second
	weekday=d.weekday()
	day=d.day
	month=d.month
	year=d.year
	
	
	if h >9:
		h1=str(h)[0]
		h2=str(h)[1]
	
	else:
		h1=str(0)
		h2=str(h)
	canvas.itemconfig(var1, text=h1)
	canvas.itemconfig(var2, text=h2)
	
	if m >9:
		m1=str(m)[0]
		m2=str(m)[1]
	
	else:
		m1=str(0)
		m2=str(m)
	canvas.itemconfig(var3, text=m1)
	canvas.itemconfig(var4, text=m2)
	
	if s >9:
		s1=str(s)[0]
		s2=str(s)[1]
	
	else:
		s1=str(0)
		s2=str(s)
	canvas.itemconfig(var5, text=s1)
	canvas.itemconfig(var6, text=s2)
	canvas.itemconfig(var7, text=weekday)
	wday=""
	if weekday==0:
		wday="Monday"
	elif weekday==1:
		wday="Tuesday"
	elif weekday==2:
		wday="Wednesday"
	elif weekday==3:
		wday="Thursday"
	elif weekday==4:
		wday="Friday"
	elif weekday==5:
		wday="Saturday"
	else:
		wday="Sunday"
	canvas.itemconfig(var7, text=wday)
	date=f"{day}/{month}/{year}"
		
	canvas.itemconfig(var8, text=date)
	canvas.after(200,clock)

clock()

def on_closing():
	if askyesno("Exit", "Do you want to exit ? "):
		root.destroy()



root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

