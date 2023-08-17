from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.title("Calculator by Abhay")
root.geometry("500x500+150+50")
root.configure(bg="purple4")

def solve():
	res=0
	eq=eq_ent.get()
	if eq=="":
		showerror("Error", "input cannot be empty.")
	elif eq.strip()=="":
		showerror("Error", "cannot be spaces.")
	else:
		try:
			if "+" in eq:
				num1, num2=eq.split("+")
				res=float(num1)+float(num2)
			elif "-" in eq:
				num1, num2=eq.split("-")
				res=float(num1)-float(num2)
			elif ("*" in eq):
				num1, num2=eq.split("*")
				res=float(num1)*float(num2)
			elif ("x" in eq):
				num1, num2=eq.split("x")
				res=float(num1)*float(num2)
			elif "/" in eq:
				num1,num2= eq.split("/")
				if num2=="0":
					showerror("Error", "A number can't be divided by 0.")
				else:
					res=float(num1)/float(num2)
			elif eq.isalpha():
				showerror("Error","letters are not allowed.")
			else:
				showerror("Error", "cannot preform.")
		except Exception as e:
			showerror("Error", "cannot perform.")
		finally:
			eq_ent.delete(0, END)
			ans_lab.configure(text=str(round(res,2)), font=('Helvetica', 20, 'bold'))
		
				
			 

f=('Helvetica', 20, 'bold')
tit_lab=Label(root, text="Calculator", font=('Helvetica', 25, 'bold'), bg="purple4", fg="yellow2")
tit_lab.place(x=180, y=10)

eq_ent=Entry(root, font=('Helvetica',20 , 'bold'),bg="purple1",  fg="yellow2")
eq_ent.place(x=110, y=80)

solve_btn=Button(root, text="Solve", font=f, relief=SUNKEN, bg="lightgreen", width=7, height=1, command=solve)
solve_btn.place(x=200, y=150)

ans_lab=Label(root, text="Answer will come here.", font=('Helvetica', 15, 'bold'), bg="purple2", fg="yellow2")
ans_lab.place(x=150, y=250)



def on_closing():
	if askyesno("Exit", "Do you want to exit ? "):
		root.destroy()



root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()