from tkinter import *
from tkinter.messagebox import *
from math import *



root=Tk()
root.title("Calculator By Abhay")
root.geometry("535x600+500+150")
root.resizable(width=False, height=False)
root.configure(bg="purple4")
f=('Helvetica', 20, 'bold')

eq=""
seq=""
flage=0
back="midnight blue"
fc="yellow2"
f1=Frame(root, bg=back, borderwidth=6, relief=SUNKEN)
f1.pack(side=TOP,fill="x", pady=2, padx=5)
l1=Label(f1, text="Calculator                   Scientific calculator", font=('Helvetica', 15, 'bold'), bg=back, fg=fc)
l1.grid(row=0, column=0, pady=5, padx=80)


f2=Frame(root, borderwidth=6, relief=SUNKEN, bg="slategray3")
f2.pack(side=LEFT,fill="y", pady=3, padx=1)
l2=Label(f2, text="Type an eqation", font=("calibry", 20),  bg="lightblue3", borderwidth=1, relief="solid", fg="gray")
l2.grid(row=0, column=0, ipady=20, ipadx=22,columnspan=3, pady=3, padx=3, sticky = 'ew' )

	
	
def c1():
	global eq
	eq=eq+"1"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c2():
	global eq
	eq=eq+"2"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c3():
	global eq
	eq=eq+"3"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c4():
	global eq
	eq=eq+"4"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c5():
	global eq
	eq=eq+"5"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c6():
	global eq
	eq=eq+"6"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c7():
	global eq
	eq=eq+"7"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c8():
	global eq
	eq=eq+"8"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c9():
	global eq
	eq=eq+"9"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c0():
	global eq
	eq=eq+"0"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_dot():
	global eq
	eq=eq+"."
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_dot():
	global eq
	eq=eq+"."
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_dot():
	global eq
	eq=eq+"."
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_dot():
	global eq
	eq=eq+"."
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_plus():
	global eq
	eq=eq+"+"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_min():
	global eq
	eq=eq+"-"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_div():
	global eq
	eq=eq+"/"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))
def c_mul():
	global eq
	eq=eq+"*"
	l2.configure(text=eq, fg="black", font=("calibry", 20, "bold"))


def ac():
	global eq
	global seq
	eq=""
	seq=""
	l2.configure(text=eq)
	l3.configure(text=seq)
def dele():
	global eq
	global seq
	eq=eq[:len(eq)-1]
	seq=seq[:len(seq)-1]
	l2.configure(text=eq)
	l3.configure(text=seq)
def solve():
	global eq
	if eq=="":
		showerror("Error","input cannot be empty")
	else:
		num1=0
		num2=0
		
		l=[".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		if not (eq[0] in l):
			showerror("Error", "Equation is invalid")
	
		else:
			for i in range(0, len(eq)):
				if not eq[i] in l:
					num1=float(eq[:i])
					j=i
					break
			op=eq[j]
			try:
				num2=float(eq[j+1:len(eq)])
			except Exception as e:
				showerror("Error","invalid input")
			
			res=0
			
			if op=="+":
				res=num1+num2
			elif op=="-":
				res=num1-num2
			elif op=="*":
				res=num1*num2
			else:
				if num2==0.0:
				
					showerror("Error", "A number can't be divided by 0")
				else:
					res=num1/num2
			l2.configure(text=str(round(res, 2)))
			eq=str(round(res, 2))
def c_tan():
	global seq
	seq="tan("
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
	
def c_cos():
	global seq
	seq="cos("
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c_sin():
	global seq
	seq="sin("
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c_log():
	global seq
	seq="log("
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c_sqrt():
	global seq
	seq="sqrt("
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c_fact():
	global seq
	seq=seq+"!"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c_raise():
	global seq
	seq=seq+"^"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))

def c21():
	global seq
	seq=seq+"1"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c22():
	global seq
	seq=seq+"2"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c23():
	global seq
	seq=seq+"3"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c24():
	global seq
	seq=seq+"4"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c25():
	global seq
	seq=seq+"5"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c26():
	global seq
	seq=seq+"6"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c27():
	global seq
	seq=seq+"7"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c28():
	global seq
	seq=seq+"8"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c29():
	global seq
	seq=seq+"9"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c20():
	global seq
	seq=seq+"0"
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))
def c2_dot():
	global seq
	seq=seq+"."
	l3.configure(text=seq, fg="black", font=("calibry", 20, "bold"))

	
	

def solve2():
	if seq=="":
		showerror("Error","input cannot be empty")
	else:
		res2=0
		if seq[:3]=="tan":
			res2=round(tan(float(seq[4:])),2)
		elif seq[:3]=="sin":
		
			res2=round((sin(float(seq[4:]))),2)
		elif seq[:3]=="cos":
			res2=round(cos(float(seq[4:])),2)
		elif seq[:3]=="log":
			res2=round(log(float(seq[4:])),2)
		elif seq[:4]=="sqrt":
			res2=round(sqrt(float(seq[5:])),2)
		elif seq[len(seq)-1]=="!":
		
			res2=factorial(int(seq[:len(seq)-1]))
		elif "^" in seq:
			x,y=seq.split("^")
			res2=round(pow(float(x), float(y)),2)
		
		else:
			showerror("Error", "Something went wrong! ")
			res=0
		l3.configure(text=str(res2))
		
		


b7=Button(f2, text="7", font=f, bg=back, fg=fc, width=4, command=c7)
b7.grid(row=1, column=0, pady=3, padx=3)

b8=Button(f2, text="8", font=f, bg=back, fg=fc, width=4, command=c8)
b8.grid(row=1, column=1, pady=3, padx=3)

b9=Button(f2, text="9", font=f, bg=back, fg=fc, width=4, command=c9)
b9.grid(row=1, column=2, pady=3, padx=3)

b4=Button(f2, text="4", font=f, bg=back, fg=fc, width=4, command=c4)
b4.grid(row=2, column=0, pady=3, padx=3)

b5=Button(f2, text="5", font=f, bg=back, fg=fc, width=4, command=c5)
b5.grid(row=2, column=1, pady=3, padx=3)

b6=Button(f2, text="6", font=f, bg=back, fg=fc, width=4, command=c6)
b6.grid(row=2, column=2, pady=3, padx=3)

b1=Button(f2, text="1", font=f, bg=back, fg=fc, width=4, command=c1)
b1.grid(row=3, column=0, pady=3, padx=3)

b2=Button(f2, text="2", font=f, bg=back, fg=fc, width=4, command=c2)
b2.grid(row=3, column=1, pady=3, padx=3)

b3=Button(f2, text="3", font=f, bg=back, fg=fc, width=4, command=c3)
b3.grid(row=3, column=2, pady=3, padx=3)


b0=Button(f2, text="0", font=f, bg=back, fg=fc, width=9, command=c0)
b0.grid(row=4, column=1, pady=3, padx=3,  columnspan=2)

b_dot=Button(f2, text=".", font=f, bg=back, fg=fc, width=4, command=c_dot)
b_dot.grid(row=4, column=0, pady=3, padx=3)

b_del=Button(f2, text="DEL", font=f, bg="orange red", fg=fc, width=9, command=dele)
b_del.grid(row=5, column=0, pady=3, padx=3, columnspan=2)

b_ac=Button(f2, text="AC", font=f, bg="lightblue", fg=fc, width=4, command=ac)
b_ac.grid(row=5, column=2, pady=3, padx=3)

b_mul=Button(f2, text="x", font=f, bg=back, fg=fc, width=4, command=c_mul)
b_mul.grid(row=6, column=0, pady=3, padx=3)

b_div=Button(f2, text="÷", font=f, bg=back, fg=fc, width=4, command=c_div)
b_div.grid(row=6, column=1, pady=3, padx=3)

b_add=Button(f2, text="+", font=f, bg=back, fg=fc, width=4, command=c_plus)
b_add.grid(row=6, column=2, pady=3, padx=3)

b_sub=Button(f2, text="-", font=f, bg=back, fg=fc, width=4, command=c_min)
b_sub.grid(row=7, column=0, pady=3, padx=3)

b_equal=Button(f2, text="=", font=f, bg="lightgreen", fg=fc, width=9, command=solve)
b_equal.grid(row=7, column=1, pady=3, padx=3, columnspan=2)

f3=Frame(root, borderwidth=6, relief=SUNKEN, bg="slategray3")
f3.pack(side=RIGHT,fill="y", pady=3, padx=2)
l3=Label(f3, text="Type an eqation", font=("calibry", 20),  bg="lightblue3", borderwidth=1, relief="solid", fg="gray")
l3.grid(row=0, column=0, ipady=20, ipadx=22,columnspan=3, pady=3, padx=3, sticky = 'ew' )

b_tan=Button(f3, text="tan", font=f, bg=back, fg=fc, width=4, command=c_tan)
b_tan.grid(row=1, column=0, pady=3, padx=3)

b_cos=Button(f3, text="cos", font=f, bg=back, fg=fc, width=4, command=c_cos)
b_cos.grid(row=1, column=1, pady=3, padx=3)

b_sin=Button(f3, text="sin", font=f, bg=back, fg=fc, width=4, command=c_sin)
b_sin.grid(row=1, column=2, pady=3, padx=3)

b_sr=Button(f3, text="√", font=f, bg=back, fg=fc, width=4, command=c_sqrt)
b_sr.grid(row=2, column=0, pady=3, padx=3)

b_raise=Button(f3, text="^", font=f, bg=back, fg=fc, width=4, command=c_raise)
b_raise.grid(row=2, column=1, pady=3, padx=3)

b_fact=Button(f3, text="!", font=f, bg=back, fg=fc, width=4, command=c_fact)
b_fact.grid(row=2, column=2, pady=3, padx=3)



b_log=Button(f3, text="ln", font=f, bg=back, fg=fc, width=4, command=c_log)
b_log.grid(row=3, column=0, pady=3, padx=3)

b_open=Button(f3, text="(", font=f, bg=back, fg=fc, width=4, command=c8)
b_open.grid(row=3, column=1, pady=3, padx=3)

b_close=Button(f3, text=")", font=f, bg=back, fg=fc, width=4, command=c9)
b_close.grid(row=3, column=2, pady=3, padx=3)



b27=Button(f3, text="7", font=f, bg=back, fg=fc, width=4, command=c27)
b27.grid(row=4, column=0, pady=3, padx=3)

b28=Button(f3, text="8", font=f, bg=back, fg=fc, width=4, command=c28)
b28.grid(row=4, column=1, pady=3, padx=3)

b29=Button(f3, text="9", font=f, bg=back, fg=fc, width=4, command=c29)
b29.grid(row=4, column=2, pady=3, padx=3)

b24=Button(f3, text="4", font=f, bg=back, fg=fc, width=4, command=c24)
b24.grid(row=5, column=0, pady=3, padx=3)

b25=Button(f3, text="5", font=f, bg=back, fg=fc, width=4, command=c25)
b25.grid(row=5, column=1, pady=3, padx=3)

b26=Button(f3, text="6", font=f, bg=back, fg=fc, width=4, command=c26)
b26.grid(row=5, column=2, pady=3, padx=3)

b21=Button(f3, text="1", font=f, bg=back, fg=fc, width=4, command=c21)
b21.grid(row=6, column=0, pady=3, padx=3)

b22=Button(f3, text="2", font=f, bg=back, fg=fc, width=4, command=c22)
b22.grid(row=6, column=1, pady=3, padx=3)

b23=Button(f3, text="3", font=f, bg=back, fg=fc, width=4, command=c23)
b23.grid(row=6, column=2, pady=3, padx=3)


b20=Button(f3, text="0", font=f, bg=back, fg=fc, width=4, command=c20)
b20.grid(row=7, column=1, pady=3, padx=3)

b2_dot=Button(f3, text=".", font=f, bg=back, fg=fc, width=4, command=c2_dot)
b2_dot.grid(row=7, column=0, pady=3, padx=3)

b_equal2=Button(f3, text="=", font=f, bg="lightgreen", fg=fc, width=4, command=solve2)
b_equal2.grid(row=7, column=2, pady=3, padx=3)






def changeOnHover(button, colorOnHover='SeaGreen1', colorOnLeave=back):

    button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover, foreground= "black"))

    button.bind("<Leave>", func=lambda e: button.config(background= colorOnLeave, foreground=fc ))

def on_enter(e):
	b1.config(background='OrangeRed3', foreground= fc)
	print(b1)


def on_leave(e):
	b1.config(background= back, foreground= fc)

changeOnHover(b1)
changeOnHover(b2)
changeOnHover(b3)
changeOnHover(b4)
changeOnHover(b5)
changeOnHover(b6)
changeOnHover(b7)
changeOnHover(b8)
changeOnHover(b9)
changeOnHover(b0)
changeOnHover(b_dot)
changeOnHover(b_sub)
changeOnHover(b_add)
changeOnHover(b_mul)
changeOnHover(b_div)
changeOnHover(b_equal, 'green', "lightgreen")
changeOnHover(b_del,'red', "orange red")
changeOnHover(b_ac, 'blue', "lightblue")
changeOnHover(b_tan)
changeOnHover(b_cos)
changeOnHover(b_sin)
changeOnHover(b_sr)
changeOnHover(b_raise)
changeOnHover(b_fact)
changeOnHover(b_log)
changeOnHover(b_open)
changeOnHover(b_close)
changeOnHover(b_equal2, 'green', "lightgreen")

def on_closing():
	if askyesno("Exit", "Do you want to exit ? "):
		root.destroy()



root.protocol("WM_DELETE_WINDOW", on_closing)




root.mainloop()