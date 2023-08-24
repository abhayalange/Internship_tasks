from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import re
from requests import *
import matplotlib.pyplot as plt

mw=Tk()
mw.geometry("700x700+350+30")
mw.title("Employee Management System")
mw.configure(bg="PaleGreen3")
f=("Times New Roman", 20, "bold")

def f1():
	mw.withdraw()
	addw.deiconify()

def f2():
	addw.withdraw()
	mw.deiconify()
def f3():
	id=id_ent.get();
	name=name_ent.get();
	salary=salary_ent.get()
	
	if(id==""):
		showerror("Error","Please enter id.")
	elif(id.strip()==""):
		showerror("Error","Id cannot be spaces.")
	elif(not id.isnumeric()):
		showerror("Error","Please only enter numbers in id.")
	elif re.search(r'[^\w\s]', id):
		showerror("Error","Only use numbers in id.")
	elif(int(id)<0):
		showerror("Error","Id cannot be negative.")
	elif(name==""):
		showerror("Error","Please enter name.")
	elif(name.strip()==""):
		showerror("Error","Name cannot be spaces.")
	elif(len(name)<2):
		showerror("Error","Name Should contain atleast 2 letters.")
	elif(not name.isalpha()):
		showerror("Error","Please only enter letters in name.")
	elif re.search(r'[^\w\s]', name):
		showerror("Error","Only use letters in name.")
	elif(salary==""):
		showerror("Error","Please enter salary.")
	elif(salary.strip()==""):
		showerror("Error","salary cannot be spaces.")
	elif(not salary.isnumeric()):
		showerror("Error","Please only enter numbers in salary.")
	elif re.search(r'[^\w\s]', salary):
		showerror("Error","Only use numbers in salary.")
	elif(int(salary)<0):
		showerror("Error","Salary cannot be negative.")
	else:

		con=None
		try:
			con=connect("employee1.db")
			cursor=con.cursor()
			cursor.execute("SELECT COUNT(*) FROM employee WHERE id=?", (id,))
			count = cursor.fetchone()[0]
			if count > 0:
				showerror("Error",f"{id} already exists.")
			else:
				sql="insert into employee values('%d','%s','%d')"

				cursor.execute(sql % (int(id),name,int(salary)))
				con.commit()
				showinfo("Success", "Data inserted ")
   				
			
		except Exception as e:
			con.rollback()
			showerror("Issue ",str(e))
		finally:
			if con is not None:
				con.close()
	id_ent.delete(0,END)
	name_ent.delete(0,END)
	salary_ent.delete(0,END)

def f4():
	mw.withdraw()
	vw.deiconify()
	show_ent.delete(1.0, END)
	con=None
	try:
		con=connect("employee1.db")
		cursor=con.cursor()
		sql="select * from employee"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info + "Id ="+ str(d[0]) + ", \n"+"Name = "+str(d[1]) + ", \n"+"Salary = " + str(d[2]) +  " \n\n"
		show_ent.insert(INSERT, info)
	except Exception as e:
		showerror("Issue ",str(e))
	finally:
		if con is not None:
			con.close()
def f5():
	vw.withdraw()
	mw.deiconify()
def f6():
	mw.withdraw()
	uw.deiconify()
	
def f7():
	id=uw_id_ent.get()
	


	if(id==""):
		showerror("Error","Please enter id.")
	elif(id.strip()==""):
		showerror("Error","Id cannot be spaces.")
	elif(not id.isnumeric()):
		showerror("Error","Please only enter numbers in id.")
	elif re.search(r'[^\w\s]', id):
		showerror("Error","Only use numbers in id.")
	elif(int(id)<0):
		showerror("Error","Id cannot be negative.")
	else:
		con=None
		try:
			con=connect("employee1.db")
			cursor=con.cursor()
			cursor.execute("SELECT COUNT(*) FROM employee WHERE id=?", (id,))
			count = cursor.fetchone()[0]
			if count > 0:
				submit_btn.destroy();
				
				uw_name_lab.place(x=270, y=230)
				uw_name_ent.place(x=150, y=280)
				uw_salary_lab.place(x=270, y=360)
				uw_salary_ent.place(x=150, y=410)
				uw_save_btn.place(x=170, y=490)
				uw_back_btn.place(x=370, y=490)

				

				
			else:
				showerror("Error","There is no record is present with this id.")
   				
			
		except Exception as e:
			con.rollback()
			showerror("Issue ",str(e))
		finally:
			if con is not None:
				con.close()

def f8():
	id=uw_id_ent.get()
	name=uw_name_ent.get()
	salary=uw_salary_ent.get();
	if(name==""):
		showerror("Error","Please enter name.")
	elif(name.strip()==""):
		showerror("Error","Name cannot be spaces.")
	elif(not name.isalpha()):
		showerror("Error","Please only enter letters in name.")
	elif(len(name)<2):
		showerror("Error","Name Should contain atleast 2 letters.")
	elif re.search(r'[^\w\s]', name):
		showerror("Error","Only use letters in name.")
	elif(salary==""):
		showerror("Error","Please enter salary.")
	elif(salary.strip()==""):
		showerror("Error","salary cannot be spaces.")
	elif(not salary.isnumeric()):
		showerror("Error","Please only enter numbers in salary.")
	elif re.search(r'[^\w\s]', salary):
		showerror("Error","Only use numbers in salary.")
	elif(int(salary)<0):
		showerror("Error","Salary cannot be negative.")
	else:
		con=None
		try:
			con=connect("employee1.db")
			cursor=con.cursor()
		
			cursor.execute("UPDATE employee SET name = ?, salary = ? WHERE id = ?", (name, int(salary), int(id)))
			con.commit()
			showinfo("Success", "Data updated. ")
		
		except Exception as e:
			showerror("Issue ",str(e))
		finally:
			if con is not None:
				con.close()
	uw_id_ent.delete(0,END)
	uw_name_ent.delete(0,END)
	uw_salary_ent.delete(0,END)

def f9():
	uw.withdraw()
	mw.deiconify()

def f13():
	mw.withdraw()
	dw.deiconify()
def f10():
	id=dw_id_ent.get()

	if(id==""):
		showerror("Error","Please enter id.")
	elif(id.strip()==""):
		showerror("Error","Id cannot be spaces.")
	elif(not id.isnumeric()):
		showerror("Error","Please only enter numbers in id.")
	elif re.search(r'[^\w\s]', id):
		showerror("Error","Only use numbers in id.")
	elif(int(id)<0):
		showerror("Error","Id cannot be negative.")
	else:
		con=None
		try:
			con=connect("employee1.db")
			cursor=con.cursor()
			cursor.execute("SELECT COUNT(*) FROM employee WHERE id=?", (id,))
			count = cursor.fetchone()[0]
			if count > 0:
				sql="Delete from employee Where id = '%s'"
				cursor.execute(sql%(id))
				con.commit()
				showinfo("success","Data deleted")
				

				
			else:
				showerror("Error","There is no record is present with this id.")
   				
			
		except Exception as e:
			con.rollback()
			showerror("Issue ",str(e))
		finally:
			if con is not None:
				con.close()
	dw_id_ent.delete(0,END)

	
	
def f11():
	dw.withdraw()
	mw.deiconify()	

def f12():
	con=None
	try:
		con=connect("employee1.db")
		cursor=con.cursor()
		cursor.execute("SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 5")
		data = cursor.fetchall()
		names, salaries = zip(*data)
		colors = ['red', 'blue', 'green', 'yellow', 'purple']
		plt.bar(names, salaries, color=colors)
		plt.xlabel('Names')
		plt.ylabel('Salaries')
		plt.title('Top 5 Highest Salaries')
		plt.show()
				
	except Exception as e:
		showerror("Issue ",str(e))
	finally:
		if con is not None:
			con.close()

   	
	




		

add_btn=Button(mw, font=f, text="Add", width=12, bg="PaleGreen4", fg="Yellow", height=1, command=f1)
add_btn.place(x=260, y=70)

view_btn=Button(mw, font=f, text="View", width=12, bg="PaleGreen4", fg="Yellow", height=1, command=f4)
view_btn.place(x=260, y=170)

update_btn=Button(mw, font=f, text="Update", width=12, bg="PaleGreen4", fg="Yellow", height=1, command=f6)
update_btn.place(x=260, y=270)

delete_btn=Button(mw, font=f, text="Delete", width=12, bg="PaleGreen4", fg="Yellow", height=1, command=f13)
delete_btn.place(x=260, y=370)

chart_btn=Button(mw, font=f, text="Charts", width=12, bg="PaleGreen4", fg="Yellow", height=1, command=f12)
chart_btn.place(x=260, y=470)

a1 = "https://api.openweathermap.org/data/2.5/weather"
a2 = "?q=" + "mumbai" 
a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
a4 = "&units=" + "metric"
wa=a1+a2+a3+a4;
try:
	res=get(wa)
	
	data=res.json()
	
except Exception as e:
	showerror("Issue",e)
loc=data["name"]
temp=data["main"]["temp"]
loc_lab=Label(mw, font=f, text=f"Location : {loc}", bg="PaleGreen4")
loc_lab.place(x=30, y=630)

temp_lab=Label(mw, font=f, text=f"Temp : {temp}", bg="PaleGreen4", fg="orangered4")
temp_lab.place(x=520, y=630)

addw=Tk()
addw.geometry("700x700+350+30")
addw.title("Employee Management System")
addw.configure(bg="SlateGray3")
id_lab=Label(addw,font=f, text="Enter id : ", bg="SlateGray3")
id_lab.place(x=280, y=100)

id_ent=Entry(addw, font=f, width=30,bg="SlateGray1")
id_ent.place(x=150, y=150)

name_lab=Label(addw, font=f, text="Enter name : ", bg="SlateGray3")
name_lab.place(x=270, y=230)

name_ent=Entry(addw, font=f, width=30,bg="SlateGray1")
name_ent.place(x=150, y=280)

salary_lab=Label(addw, font=f, text="Enter salary : ", bg="SlateGray3")
salary_lab.place(x=270, y=360)

salary_ent=Entry(addw, font=f, width=30,bg="SlateGray1")
salary_ent.place(x=150, y=410)

save_btn=Button(addw, font=f, text="Save", width=10, bg="SeaGreen1", command=f3)
save_btn.place(x=170, y=490)

back_btn=Button(addw, font=f, text="Back", width=10, bg="Orangered", command=f2)
back_btn.place(x=370, y=490)


	


addw.withdraw()

vw=Tk()
vw.geometry("700x700+350+30")
vw.title("Employee Management System")
vw.configure(bg="Wheat1")


show_ent=ScrolledText(vw, font=f, height=17, width=42, bg="lightyellow")
show_ent.place(x=45, y=40)

vw_back=Button(vw, text="Back", font=f, bg="red2",width=10, command=f5)
vw_back.place(x=280, y=600)


vw.withdraw()


uw=Tk()
uw.geometry("700x700+350+30")
uw.title("Employee Management System")
uw.configure(bg="bisque")
uw_id_lab=Label(uw,font=f, text="Enter your id : ", bg="bisque")
uw_id_lab.place(x=280, y=100)

uw_id_ent=Entry(uw, font=f, width=30,bg="linen")
uw_id_ent.place(x=150, y=150)



uw_name_lab=Label(uw, font=f, text="Enter name : ", bg="bisque")


uw_name_ent=Entry(uw, font=f, width=30,bg="linen")


uw_salary_lab=Label(uw, font=f, text="Enter salary : ", bg="bisque")


uw_salary_ent=Entry(uw, font=f, width=30,bg="linen")


uw_save_btn=Button(uw, font=f, text="Save", width=10, bg="SeaGreen1", command=f8)


uw_back_btn=Button(uw, font=f, text="Back", width=10, bg="Orangered", command=f9)

submit_btn=Button(uw, font=f, text="Submit", width=12, bg="PaleGreen4", fg="Yellow", height=1, command=f7)

submit_btn.place(x=260, y=220)
uw.withdraw()

dw=Tk()
dw.geometry("700x700+350+30")
dw.title("Employee Management System")
dw.configure(bg="salmon1")

dw_id_lab=Label(dw,font=f, text="Enter your id : ", bg="salmon1")
dw_id_lab.place(x=280, y=100)

dw_id_ent=Entry(dw, font=f, width=30,bg="tan1")
dw_id_ent.place(x=150, y=150)

dw_delete_btn=Button(dw, font=f, text="Delete", width=12, bg="tomato", fg="black", height=1, command=f10)
dw_delete_btn.place(x=260, y=220)

dw_back_btn=Button(dw, font=f, text="Back", width=12, bg="tomato", fg="black", height=1, command=f11)
dw_back_btn.place(x=260, y=300)
dw.withdraw()


def on_closing():
	if askyesno("Exit", "Do you want to exit ? "):
		mw.destroy()
		addw.destroy()
		vw.destroy()
		uw.destroy()
		dw.destroy()
		




mw.protocol("WM_DELETE_WINDOW", on_closing)
addw.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)
uw.protocol("WM_DELETE_WINDOW", on_closing)
dw.protocol("WM_DELETE_WINDOW", on_closing)


mw.mainloop()