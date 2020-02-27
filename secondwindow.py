from tkinter import *
from tkinter import messagebox, ttk
import time
import os
# import login1


class data:
    def __init__(self,root):
        self.main = root
        self.main.title("Employment Manager")
        self.main.geometry("1920x1080+0+0")

        top = Label(self.main,text="Employee Registration",fg="white",bd=10,relief=GROOVE,pady=10,font=("Arial",35),bg="brown").pack(fill=X)

        employerframe = Frame(self.main,bd=10,bg="grey",relief=GROOVE)
        employerframe.place(x=800,y=100,width=750,height=700)

        #Saving_Variables
        self.id = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.address = StringVar()
        self.contact = StringVar()
        self.department = StringVar()

        #Labels
        Saurav1=Label(employerframe,text="EMPLOYEE'S DETAILS",bg="grey",fg="White",font=("Gadugi",20)).grid(row=0,column=1,pady=0)
        Saurav2=Label(employerframe, text="ID:",fg="white",bg="grey", font=("Gadugi", 20)).grid(row=1, column=0, pady=20,padx=10,sticky="w")
        Saurav3=Label(employerframe,text="NAME:",fg="White",bg="grey",font=("Gadugi",20)).grid(row=2,column=0,pady=20,padx=10,sticky="w")
        Saurav4=Label(employerframe,text="AGE:",fg="White",bg="grey",font=("Gadugi",20)).grid(row=3,column=0,pady=20,padx=10,sticky="w")
        Saurav5=Label(employerframe,text="ADDRESS:",fg="White",bg="grey",font=("Gadugi",20)).grid(row=4,column=0,pady=20,padx=10,sticky="w")
        Saurav7=Label(employerframe,text="CONTACT:",fg="White",bg="grey",font=("Gadugi",20)).grid(row=5,column=0,pady=20,padx=10,sticky="w")
        Saurav8=Label(employerframe,text="DEPARTMENT:",fg="White",bg="grey",font=("Gadugi",20)).grid(row=6,column=0,pady=20,padx=10,sticky="w")

        #Entries_for_the_above_Labels

        Chhetri1=Entry(employerframe,bd=7,textvariable=self.id,relief=GROOVE,width=20,font="Gadugi 16").grid(row=1,column=1,padx=10,pady=10)
        Chhetri2=Entry(employerframe,bd=7,textvariable=self.name,relief=GROOVE,width=20,font="Gadugi 16").grid(row=2,column=1,padx=10,pady=10)
        Chhetri3=Entry(employerframe,bd=7,textvariable=self.age,relief=GROOVE,width=20,font=("Gadugi 16")).grid(row=3,column=1,padx=10,pady=10)
        Chhetri4=Entry(employerframe,bd=7,textvariable=self.address,relief=GROOVE,width=20,font=("Gadugi 16")).grid(row=4,column=1)
        Chhetri6=Entry(employerframe,bd=7,textvariable=self.contact,relief=GROOVE,width=20,font=("Gadugi 16")).grid(row=5,column=1)
        Chhetri7=Entry(employerframe,bd=7,textvariable=self.department,relief=GROOVE,width=20,font=("Gadugi 16")).grid(row=6,column=1)

        #Buttons
        btn=Button(employerframe,text="Exit",height=2,width=20,font="Gadugi 11  bold",command=self.exit).place(x=500,y=530)
        btn1=Button(employerframe,text="Reset",height=2,width=20,font="Gadugi 11  bold",command=self.clear).place(x=270,y=530)
        btn2=Button(employerframe,text="Register",height=2,width=20,font="Gadugi 11 bold",command=self.save_file).place(x=45,y=530)
        # btn3=Button(employerframe,text="Logout",height=2,width=20,font="Gadugi 11  bold",command=self.logout).place(x=45,y=590)
        btn4=Button(employerframe,text="Delete",height=2,width=20,font="Gadugi 11 bold",command=self.delete).place(x=270,y=590)

        #Registered_data_Window

        data = Frame(self.main,bd=10,relief=GROOVE,bg="Black")
        data.place(x=20,y=100,width=712,height=700)

        datatitle = Label(data,text="REGISTERED DATA",bg="grey",fg="White",font="Gadugi 22",bd=5,relief=GROOVE).pack(side=TOP,fill=X)

        scroll=Scrollbar(data,orient=VERTICAL)
        self.datalist = Listbox(data,yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        self.datalist.pack(fill=BOTH,expand=5)
        scroll.config(command=self.datalist.yview)
        self.datalist.bind("<ButtonRelease-1>",self.getdata)
        self.showfiles()

    def save_file(self):
        if self.id.get()=="":
            messagebox.showerror("error","data should be filled")
        else:
            f= open("files/" + self.id.get() + ".txt", "w")
            f.write(
                str(self.id.get()) + "," +
                str(self.name.get()) + "," +
                str(self.age.get()) + "," +
                str(self.address.get()) + "," +
                str(self.contact.get()) + "," +
                str(self.department.get()) + ","
                )
            f.close()
            messagebox.showinfo("Saved","Your information has been saved")
            self.showfiles()


    def showfiles(self):
        files=os.listdir("files/")
        self.datalist.delete(0,END)
        if len(files)>0:
            for i in files:
                self.datalist.insert(END,i)


    def delete(self):
        present = "no"
        if self.id.get=="":
            messagebox.showerror("Error","id must be required")
        else:
            f = os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Delete","Do you really want to delete?")
                    if ask>0:
                        os.remove("files/"+ self.id.get()+".txt")
                        messagebox.showinfo("Done","Deleted successfully")
                        self.showfiles()
                else:
                    messagebox.showerror("Error","File not found")

    def getdata(self,ev):
        get_cursor=self.datalist.curselection()

        o1 = open("files/"+self.datalist.get(get_cursor))
        value=[]
        for f in o1:
            value=f.split(",")

        self.id.set(value[0])
        self.name.set(value[1])
        self.age.set(value[2])
        self.address.set(value[3])
        self.contact.set(value[4])
        self.department.set(value[5])

    def clear(self):
        self.id.set("")
        self.name.set("")
        self.age.set("")
        self.address.set("")
        self.contact.set("")
        self.department.set("")

    def exit(self):
         option = messagebox.askyesno("Exit", "Do you want to exit?")
         if option > 0:
            self.main.destroy()
         else:
            return
    #
    # def logout(self):
    #     self.main.quit()
    #     a=login1.Management(Toplevel(main))
