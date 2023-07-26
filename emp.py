from tkinter import*
from tkinter import ttk
from tkcalendar import*
from tkcalendar import DateEntry
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1450x790+0+0")
        self.root.title("Employee Management System")

        # Variables
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_mail = StringVar()
        self.var_phone = StringVar()
        self.var_sereport = StringVar()
        self.var_gender = StringVar()
        self.var_id = StringVar()
        self.var_doj= StringVar()
        self.var_pata = StringVar()
        self.var_eid = StringVar()
        
        lbltitle = Label(self.root, text='Employee Management', font=('arial', 30, 'bold'), fg='blue', bg='lightblue')
        lbltitle.place(x=0, y=0, width=1350, height=50)

        # main
        Main_f= Frame(self.root, bd=2, relief=RIDGE, bg='lightblue')
        Main_f.place(x=10, y=60, width=1250, height=560)

        # Up
        up_f= LabelFrame(Main_f, bd=2, relief=RIDGE, bg='lightgray', text='INFORMATION', font=('Arial', 10), fg='blue')
        up_f.place(x=20, y=10, width=1200, height=270)

        # entry (Label)
        # Department
        lbl_dep=Label(up_f, text="Department : ", font=('Bell MT', 14),bg="lightgray")
        lbl_dep.grid(row=0, column=0, sticky=W, padx=30)

        combo_dep= ttk.Combobox(up_f,textvariable=self.var_dep, font=('arial', 10), width=23, state='readonly')
        combo_dep['value']=('Select Department', 'HR', 'Software Enginner', 'Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=35,pady=10, sticky=W)

        # Name
        lbl_Name= Label(up_f, font=('Bell MT', 14), text= 'Name : ', bg='lightgray')
        lbl_Name.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_name= ttk.Entry(up_f,textvariable=self.var_name, width=22, font=('arial', 11))
        txt_name.grid(row=0, column=3, padx=5, pady=7 )

        # Dob
        lbl_dob= Label(up_f, font=('Bell MT', 14), text= 'Date Of Birth : ', bg='lightgray')
        lbl_dob.grid(row=1, column=0, sticky=W, padx=30, pady=7)

        txt_dob= DateEntry(up_f,textvariable=self.var_dob, width=27, background='darkblue', foreground='white', borderwidth=2)
        txt_dob.grid(row=1, column=1, padx=35, pady=7 )

        # email
        lbl_mail= Label(up_f, font=('Bell MT', 14), text= 'Mail : ', bg='lightgray')
        lbl_mail.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_mail= ttk.Entry(up_f, textvariable=self.var_mail,  width=22, font=('arial', 11))
        txt_mail.grid(row=1, column=3, padx=5, pady=7 )

        #phone 
        def validate_integer(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    
         if value_if_allowed == '':
             return True
         try:
             int(value_if_allowed)
             return True
         except ValueError:
             return False
         
        lbl_phn= Label(up_f, font=('Bell MT', 14), text= 'Phone : ', bg='lightgray')
        lbl_phn.grid(row=2, column=0, sticky=W, padx=30, pady=7)
         
        validate_cmd = (up_f.register(validate_integer), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        txt_phn= ttk.Entry(up_f,textvariable=self.var_phone, width=22, font=('arial', 11) ,validate="key", validatecommand=validate_cmd)
        txt_phn.grid(row=2, column=1, padx=35, pady=7 )

        # Seniour reporting

        lbl_dep=Label(up_f, text="Seniour Reporting : ", font=('Bell MT', 14),bg="lightgray")
        lbl_dep.grid(row=2, column=2, sticky=W)

        combo_dep= ttk.Combobox(up_f,textvariable=self.var_sereport, font=('arial', 10), width=23, state='readonly')
        combo_dep['value']=('Select Department', 'HR', 'Software Enginner', 'Manager', 'F. Manager', 'I.T. Manager')
        combo_dep.current(0)
        combo_dep.grid(row=2, column=3, padx=5,pady=10, sticky=W)

        # Gender 

        lbl_dep=Label(up_f, text="Gender : ", font=('Bell MT', 14),bg="lightgray")
        lbl_dep.grid(row=3, column=0, sticky=W, padx=30)

        combo_dep= ttk.Combobox(up_f,textvariable=self.var_gender, font=('arial', 10), width=23, state='readonly')
        combo_dep['value']=('Select', 'Male', 'Female','Other')
        combo_dep.current(0)
        combo_dep.grid(row=3, column=1, padx=35,pady=10, sticky=W)

        # ID Proof
        txt_proof= ttk.Entry(up_f,textvariable=self.var_id, width=22, font=('arial', 11))
        txt_proof.grid(row=3, column=3, padx=5, pady=7 )

        combo_dep= ttk.Combobox(up_f, font=('Bell MT', 14), width=23, state='readonly')
        combo_dep['value']=('Select ID proof', 'Aadhar card', 'Voter id', 'Driving Licence')
        combo_dep.current(0)
        combo_dep.grid(row=3, column=2, padx=5,pady=10, sticky=W)

        # Doj
        lbl_doj= Label(up_f, font=('Bell MT', 14), text= 'Date Of Join : ', bg='lightgray')
        lbl_doj.grid(row=4, column=0, sticky=W, padx=30, pady=7)

        doj = DateEntry(up_f,textvariable=self.var_doj, width=27, background='darkblue', foreground='white', borderwidth=2)
        doj.grid(row=4, column=1, padx=35, pady=7 )

        # ADD
        lbl_add= Label(up_f, font=('Bell MT', 14), text= 'Address : ', bg='lightgray')
        lbl_add.grid(row=4, column=2, sticky=W, padx=2, pady=7)

        txt_add= ttk.Entry(up_f, textvariable=self.var_pata,  width=22, font=('arial', 11))
        txt_add.grid(row=4, column=3, padx=5, pady=7 )

        # Eid
        lbl_eid= Label(up_f, font=('Bell MT', 14), text= 'Employee ID : ', bg='lightgray')
        lbl_eid.grid(row=5, column=0, sticky=W, padx=30, pady=7)

        txt_eid= ttk.Entry(up_f, textvariable=self.var_eid,  width=22, font=('arial', 11))
        txt_eid.grid(row=5, column=1, padx=35, pady=7 )
        
         # Button Frame
        button_f= Frame(up_f, bd=5, relief=RIDGE, bg='#033E3E')
        button_f.place(x=980, y=10, width=190, height=210)

        btn_add= Button(button_f, text="SAVE",command=self.add_data, font=('Time new roman', 12), width=18,bg='green', fg='black')
        btn_add.grid(row=0, column=0, padx=5, pady=10)

        btn_update= Button(button_f, text="UPDATE", command=self.update_data, font=('Timwe new roman', 12), width=18,bg='yellow', fg='black')
        btn_update.grid(row=1, column=0, padx=5, pady=10)

        btn_delete= Button(button_f, text="DELETE", command=self.delete_data , font=('Timwe new roman', 12), width=18,bg='red', fg='black')
        btn_delete.grid(row=2, column=0, padx=5, pady=10)

        btn_clear= Button(button_f, text="CLEAR", command=self.reset_data , font=('Timwe new roman', 12), width=18,bg='lightpink', fg='black')
        btn_clear.grid(row=3, column=0, padx=5, pady=10)

        # down
        down_f= LabelFrame(Main_f, bd=2, relief=RIDGE, bg='lightgray', text='INFORMATION LIST', font=('Arial', 10), fg='blue')
        down_f.place(x=20, y=280, width=1200, height=270)

        # Search Frame
        search_f= LabelFrame(down_f, bd=2, relief=RIDGE, bg='lightblue', text='Search', font=('Arial', 10), fg='blue')
        search_f.place(x=8, y=0, width=1180, height=60)

        search_by=Label(search_f, font=('arial', 10), text='Search', fg='white', bg='black')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # Search
        self.var_com_search= StringVar()
       
        com_txt_search= ttk.Combobox(search_f, textvariable=self.var_com_search ,state="readonly" , font=('arial', 10), width=20)
        com_txt_search['value']= ("select Option", "phone", "id_proof", "name", "mail")
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)
       
        self.var_search= StringVar()
        txt_search= ttk.Entry(search_f, textvariable=self.var_search , width=30, font=('arial', 10))
        txt_search.grid(row=0, column=2, padx=30)

        btn_search= Button(search_f, text="search", command=self.search_data ,  font=('arial', 10), width=14, bg='green', fg='white')
        btn_search.grid(row=0, column=3, padx=60)

        btn_showAll= Button(search_f, text='Show All',command=self.fetch_data, font=('arial', 10), width=14, bg='green', fg='white')
        btn_showAll.grid(row=0, column=4, padx=100)

        # Table Frame

        table_f= LabelFrame(down_f, bd=2, relief=RIDGE, bg='lightblue')
        table_f.place(x=8, y=70, width=1180, height=170)

        scroll_x= ttk.Scrollbar(table_f, orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_f, orient=VERTICAL)

        self.employee_table= ttk.Treeview(table_f,column=('dep', 'name', 'dob', 'mail', 'phone', 'se.re', 'gender', 'id', 'doj', 'add', 'empid'),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('dob', text='Date Of Birth')
        self.employee_table.heading('mail', text='Mail')
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('se.re', text='Senior Report')
        self.employee_table.heading('gender', text='Gender')
        self.employee_table.heading('id', text='Id Proof')
        self.employee_table.heading('doj', text='Date Of Join')
        self.employee_table.heading('add', text="Address")
        self.employee_table.heading('empid', text="Employee_id")

        self.employee_table['show']= 'headings'

        self.employee_table.column("dep", width=150)
        self.employee_table.column("name", width=150)
        self.employee_table.column("dob", width=150)
        self.employee_table.column("mail", width=150)
        self.employee_table.column("phone", width=150)
        self.employee_table.column("se.re", width=150)
        self.employee_table.column("gender", width=150)
        self.employee_table.column("id", width=150)
        self.employee_table.column("doj", width=150)
        self.employee_table.column("add", width=150)
        self.employee_table.column("empid", width=150)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.get_cursor)
        #Buttonm Has Been relias Hear We vcant app lay fot Auto re Set

        # hear We R declair The Fetching Data

        self.fetch_data()

       # Declaration    

    def add_data(self):
        if self.var_dep.get()=="" or self.var_mail.get()=="":
            messagebox.showerror('Error', 'All Fields Are Impotant To Fill')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='$@Gar0788', database='mydata')  
                my_cursor= conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                                self.var_dep .get(),
                                                                                                self.var_name .get(),
                                                                                                self.var_dob .get(),
                                                                                                self.var_mail .get(),
                                                                                                self.var_phone .get(),
                                                                                                self.var_sereport .get(),
                                                                                                self.var_gender .get(),
                                                                                                self.var_id .get(),
                                                                                                self.var_doj.get(),
                                                                                                self.var_pata.get(),
                                                                                                self.var_eid.get()


                                                                                            ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success', 'Employee Has Been Added', parent =self.root )
            except Exception as es:
                messagebox.showerror('Error', f'Due To: {str(es)}', parent=self.root)

    # fetch Data From My Sql (Show the Data In list Form)
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='$@Gar0788', database='mydata')  
        my_cursor= conn.cursor()
        my_cursor.execute('select * from employee')
        data= my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END, values=i)
            conn.commit()
        conn.close()
    # Fill Data Automatically
    # Get cursur

    def get_cursor(self,event= ""):
        cursor_row = self.employee_table.focus()
        content= self.employee_table.item(cursor_row)
        data= content['values']
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_dob.set(data[2])
        self.var_mail.set(data[3])
        self.var_phone.set(data[4])
        self.var_sereport.set(data[5])
        self.var_gender.set(data[6])
        self.var_id.set(data[7])
        self.var_doj.set(data[8])
        self.var_pata.set(data[9])
        self.var_eid.set(data[10])

# Update Field
    #  Department  Name  DOB  Mail  Phone  Senior Reporting  Gender  ID_proof  DOJ  6,Senior Reporting,mydata,employee,VARCHAR,utf8mb4,45,17,0

    def update_data(self):
        if self.var_dep.get()=="" or self.var_mail.get()=="":
            messagebox.showerror('Error', 'All Fields Are Impotant To Fill')
        else:
            try:
                update = messagebox.askyesno('update','Are You Sure To Update')
                if update>0:
                    conn = mysql.connector.connect(host='localhost', username='root', password='$@Gar0788', database='mydata')  
                    my_cursor= conn.cursor()
                    my_cursor.execute('update employee set Department=%s,Name=%s,DOB=%s,Mail=%s,Phone=%s,Sreport=%s, Gender=%s,DOJ=%s, pata=%s, empid=%s where ID_proof=%s',(

                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                    self.var_mail.get(),
                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                    self.var_sereport.get(),
                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                    self.var_doj.get(),
                                                                                                                                                                    self.var_pata.get(),
                                                                                                                                                                    self.var_eid.get(),
                                                                                                                                                                    self.var_id .get()
                                                                                                                                                                    
                                                                                                                                                                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Succes','Employee Succesfully Updated',parent= self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent= self.root)


    # delete 
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror('Error','All Fields Are required')
        else:
            try:
                Delete= messagebox.askyesno('Delete','Are You Sure To Delete',parent=self.root)
                if Delete>0:
                   conn = mysql.connector.connect(host='localhost', username='root', password='$@Gar0788', database='mydata')  
                   my_cursor= conn.cursor()
                   sql= 'delete from employee where ID_proof= %s'
                   value= (self.var_id.get(),)
                   my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Succes Fully Delete',parent= self.root)
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent= self.root)

    # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_dob.set("")
        self.var_mail.set("")
        self.var_phone.set("")
        self.var_sereport.set("")
        self.var_gender.set("")
        self.var_id.set("ID Proof")
        self.var_doj.set("")
        self.var_pata.set("")
        self.var_eid.set("")

    # search
    def search_data(self):
        if self. var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error', 'Pleas Select Option')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='$@Gar0788', database='mydata')  
                my_cursor= conn.cursor()
                #my_cursor.execute('select * from employee whare ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'")) 
                rows = my_cursor.fetchall()
                if len(rows)!= 0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("", END, values=i)
                conn.commit
                conn.close()
            except Exception as es:
                messagebox.showerror('Error', f'Due To:{str(es)}',parent= self.root)

if __name__=="__main__":
    root=Tk()
    object=Employee(root)
    root.mainloop()        