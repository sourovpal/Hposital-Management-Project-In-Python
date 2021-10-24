from tkinter import Button, Entry, Frame, Label, LabelFrame, StringVar, Text, Tk, font, ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter.constants import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, TOP, VERTICAL, W, X, Y
from typing_extensions import IntVar
import mysql.connector
from tkinter.messagebox import askokcancel, showinfo, WARNING

class Hospital:
        def __init__(self, root):
                self.root = root
                self.root.title('Hospital Management Systme')
                self.root.geometry('1540x800+0+0')                

                self.row_id=StringVar()
                self.NameOfTable=StringVar()
                self.Ref=StringVar()
                self.Dose=StringVar()
                self.NoofTablets=StringVar()
                self.Lot=StringVar()
                self.Issuedate=StringVar()
                self.ExpDate=StringVar()
                self.DailyDose=StringVar()
                self.Storage=StringVar()
                self.NHSNumber=StringVar()
                self.Pname=StringVar()
                self.Dob=StringVar()
                self.Address=StringVar()                
                
                self.conn=mysql.connector.connect(host="localhost", username="root", password="", database="hms_software")
                self.my_cursor = self.conn.cursor()

                lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
                lbltitle.pack(side=TOP, fill=X)

# ==================> DATA FRAME <===================

                Dataframe = Frame(self.root, bd=20, relief=RIDGE)        
                Dataframe.place(x=0, y=130, width=1530, height=400)

                DataframeLeft = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("times new roman", 12, "bold"), text="Patient Information")
                DataframeLeft.place(x=0, y=5, width=980, height=350)

                DataframeRight = LabelFrame(Dataframe, bd=10, padx=20, relief=RIDGE, font=("times new roman", 12, "bold"), text="Prescription")
                DataframeRight.place(x=990, y=5, width=495, height=350)

# ==================> BUTTON FRAME <===================

                ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
                ButtonFrame.place(x=0, y=530, width=1530, height=70)

# ==================> DETAILS FRAME <===================

                DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
                DetailsFrame.place(x=0, y=600, width=1530, height=190)

# ==================> DATA FRAME LEFT <===================

                lblNameTablet = Label(DataframeLeft, text="Names OF Tablet", font=('arial', 12, 'bold'), padx=2, pady=6)
                lblNameTablet.grid(row=0, column=0)

                comNameTablet = ttk.Combobox(DataframeLeft, textvariable=self.NameOfTable, state='readonly', font=('times new roman', 12, 'bold'), width=33)
                comNameTablet["values"]=("Nice", "Corona Vacaine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
                comNameTablet.current(0)
                comNameTablet.grid(row=0, column=1)

                lblref=Label(DataframeLeft, font=("arial",12,"bold"), text="Refence No:", padx=2, pady=6)
                lblref.grid(row=1, column=0, sticky=W)
                txtref=Entry(DataframeLeft, textvariable=self.Ref, font=('arial', 13, 'bold'), width=35)
                txtref.grid(row=1, column=1)

                lblDose=Label(DataframeLeft, font=("arial",12,"bold"), text="Dose:", padx=2, pady=6)
                lblDose.grid(row=2, column=0, sticky=W)
                txtDose=Entry(DataframeLeft,  textvariable=self.Dose, font=('arial', 13, 'bold'), width=35)
                txtDose.grid(row=2, column=1)

                lblNoOftablets=Label(DataframeLeft, font=("arial",12,"bold"), text="No Of Tablets:", padx=2, pady=6)
                lblNoOftablets.grid(row=3, column=0, sticky=W)
                txtNoOftablets=Entry(DataframeLeft,  textvariable=self.NoofTablets, font=('arial', 13, 'bold'), width=35)
                txtNoOftablets.grid(row=3, column=1)

                lblLot=Label(DataframeLeft, font=("arial",12,"bold"), text="Lot:", padx=2, pady=6)
                lblLot.grid(row=4, column=0, sticky=W)
                txtLot=Entry(DataframeLeft, textvariable=self.Lot, font=('arial', 13, 'bold'), width=35)
                txtLot.grid(row=4, column=1)

                lblissueDate=Label(DataframeLeft, font=("arial",12,"bold"), text="Issue Date:", padx=2, pady=6)
                lblissueDate.grid(row=5, column=0, sticky=W)
                txtissueDate=Entry(DataframeLeft,  textvariable=self.Issuedate, font=('arial', 13, 'bold'), width=35)
                txtissueDate.grid(row=5, column=1)

                lblExpDate=Label(DataframeLeft, font=("arial",12,"bold"), text="Exp Date:", padx=2, pady=6)
                lblExpDate.grid(row=6, column=0, sticky=W)
                txtExpDate=Entry(DataframeLeft,  textvariable=self.ExpDate, font=('arial', 13, 'bold'), width=35)
                txtExpDate.grid(row=6, column=1)

                lblDailyDose=Label(DataframeLeft, font=("arial",12,"bold"), text="Daily Dose:", padx=2, pady=6)
                lblDailyDose.grid(row=7, column=0, sticky=W)
                txtDailyDose=Entry(DataframeLeft,  textvariable=self.DailyDose, font=('arial', 13, 'bold'), width=35)
                txtDailyDose.grid(row=7, column=1)

                lblSideEffect=Label(DataframeLeft, font=("arial",12,"bold"), text="Side Effect:", padx=2, pady=6)
                lblSideEffect.grid(row=8, column=0, sticky=W)
                txtSideEffect=Entry(DataframeLeft, font=('arial', 13, 'bold'), width=35)
                txtSideEffect.grid(row=8, column=1)

                lblFutherInfo=Label(DataframeLeft, font=("arial",12,"bold"), text="Further Info:", padx=2, pady=6)
                lblFutherInfo.grid(row=0, column=2, sticky=W)
                txtFutherInfo=Entry(DataframeLeft, font=('arial', 13, 'bold'), width=35)
                txtFutherInfo.grid(row=0, column=3)

                lblBloodPressure=Label(DataframeLeft, font=("arial",12,"bold"), text="Blood Pressure:", padx=2, pady=6)
                lblBloodPressure.grid(row=1, column=2, sticky=W)
                txtBloodPressure=Entry(DataframeLeft, font=('arial', 13, 'bold'), width=35)
                txtBloodPressure.grid(row=1, column=3)

                lblStorage=Label(DataframeLeft, font=("arial",12,"bold"), text="Storage Advice:", padx=2, pady=6)
                lblStorage.grid(row=2, column=2, sticky=W)
                txtStorage=Entry(DataframeLeft,  textvariable=self.Storage, font=('arial', 13, 'bold'), width=35)
                txtStorage.grid(row=2, column=3)

                lblMedicine=Label(DataframeLeft, font=("arial",12,"bold"), text="Medication:", padx=2, pady=6)
                lblMedicine.grid(row=3, column=2, sticky=W)
                txtMedicine=Entry(DataframeLeft, font=('arial', 13, 'bold'), width=35)
                txtMedicine.grid(row=3, column=3)

                lblPatientId=Label(DataframeLeft, font=("arial",12,"bold"), text="Patient Id:", padx=2, pady=6)
                lblPatientId.grid(row=4, column=2, sticky=W)
                txtPatientId=Entry(DataframeLeft, font=('arial', 13, 'bold'), width=35)
                txtPatientId.grid(row=4, column=3)

                lblNhsNumber=Label(DataframeLeft, font=("arial",12,"bold"), text="NHS Number:", padx=2, pady=6)
                lblNhsNumber.grid(row=5, column=2, sticky=W)
                txtNhsNumber=Entry(DataframeLeft,  textvariable=self.NHSNumber, font=('arial', 13, 'bold'), width=35)
                txtNhsNumber.grid(row=5, column=3)

                lblPatientName=Label(DataframeLeft, font=("arial",12,"bold"), text="Patient Name:", padx=2, pady=6)
                lblPatientName.grid(row=6, column=2, sticky=W)
                txtPatientName=Entry(DataframeLeft,  textvariable=self.Pname, font=('arial', 13, 'bold'), width=35)
                txtPatientName.grid(row=6, column=3)

                lblDateOfBirth=Label(DataframeLeft, font=("arial",12,"bold"), text="Date Of Birth:", padx=2, pady=6)
                lblDateOfBirth.grid(row=7, column=2, sticky=W)
                txtDateOfBirth=Entry(DataframeLeft,  textvariable=self.Dob, font=('arial', 13, 'bold'), width=35)
                txtDateOfBirth.grid(row=7, column=3)

                lblPatientAddress=Label(DataframeLeft, font=("arial",12,"bold"), text="Patient Address:", padx=2, pady=6)
                lblPatientAddress.grid(row=8, column=2, sticky=W)
                txtPatientAddress=Entry(DataframeLeft,  textvariable=self.Address, font=('arial', 13, 'bold'), width=35)
                txtPatientAddress.grid(row=8, column=3)

# ==================> DATA FRAME RIGHT <===================

                self.txtPrescription=Text(DataframeRight, font=('arial', 13, 'bold'), width=23, height=16, padx=2, pady=6)
                self.txtPrescription.grid(row=0, column=0)

# ========================> BUTTON <========================

                btnPrescription=Button(ButtonFrame, text="Prescription", bg='green', fg='white', width=34, padx=2, pady=6)
                btnPrescription.grid(row=0, column=0)

                btnPrescriptionData=Button(ButtonFrame, text="Save", bg='green', fg='white', width=34, padx=2, pady=6, command=self.iPresectptionData)
                btnPrescriptionData.grid(row=0, column=1)

                btnUpdate=Button(ButtonFrame, text="Update", bg='green', fg='white', width=34, padx=2, pady=6, command=self.update)
                btnUpdate.grid(row=0, column=2)

                btnDelete=Button(ButtonFrame, text="Delete", bg='red', fg='white', width=34, padx=2, pady=6, command=self.delete)
                btnDelete.grid(row=0, column=3)

                btnClear=Button(ButtonFrame, text="Clear", bg='green', fg='white', width=34, padx=2, pady=6, command=self.clear)
                btnClear.grid(row=0, column=4)

                btnExit=Button(ButtonFrame, text="Exit", bg='green', fg='white', width=33, padx=2, pady=6, command=self.window_exit)
                btnExit.grid(row=0, column=5)

# ========================> BUTTON <========================

                scroll_x=ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
                scroll_y=ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

                self.hospital_table=ttk.Treeview(DetailsFrame, columns=
                                ("id", 
                                "NameOfTable", 
                                "Ref", 
                                "Dose", 
                                "NoofTablets", 
                                "Lot", 
                                "Issuedate", 
                                "ExpDate", 
                                "DailyDose", 
                                "Storage", 
                                "NHSNumber", 
                                "Pname", 
                                "Dob", 
                                "Address"
                                ), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

                scroll_x.pack(side=BOTTOM, fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)

                scroll_x.config(command=self.hospital_table.xview)
                scroll_y.config(command=self.hospital_table.yview)

                self.hospital_table.heading('id', text="ID")
                self.hospital_table.heading('NameOfTable', text="Name Of Table")
                self.hospital_table.heading('Ref', text="Reference No.")
                self.hospital_table.heading('Dose', text="Dose")
                self.hospital_table.heading('NoofTablets', text="No Of Tablets")
                self.hospital_table.heading('Lot', text="Lot")
                self.hospital_table.heading('Issuedate', text="Issue Date")
                self.hospital_table.heading('ExpDate', text="Exp Date")
                self.hospital_table.heading('DailyDose', text="Dadily Date")
                self.hospital_table.heading('Storage', text="Storage")
                self.hospital_table.heading('NHSNumber', text="NHS Number")
                self.hospital_table.heading('Pname', text="Patient Name")
                self.hospital_table.heading('Dob', text="DOB")
                self.hospital_table.heading('Address', text="Address")

                self.hospital_table['show']="headings"

                self.hospital_table.column('id', width=200)
                self.hospital_table.column('NameOfTable', width=200)
                self.hospital_table.column('Ref', width=200)
                self.hospital_table.column('Dose', width=200)
                self.hospital_table.column('NoofTablets', width=200)
                self.hospital_table.column('Lot', width=200)
                self.hospital_table.column('Issuedate', width=200)
                self.hospital_table.column('ExpDate', width=200)
                self.hospital_table.column('DailyDose', width=200)
                self.hospital_table.column('Storage', width=200)
                self.hospital_table.column('NHSNumber', width=200)
                self.hospital_table.column('Pname', width=200)
                self.hospital_table.column('Dob', width=200)
                self.hospital_table.column('Address', width=200)

                self.hospital_table.pack(fill=BOTH, expand=1)
                self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
                self.fetch_data()
                
# ========================> FUNCTINALITY DECLRATION <========================

        def iPresectptionData(self):
                if self.NameOfTable.get() == "" or self.Ref.get() == "":
                        messagebox.showerror('Error', 'All Fields are required.')
                else:
                        self.conn=mysql.connector.connect(host="localhost", username="root", password="", database="hms_software")
                        self.my_cursor = self.conn.cursor()
                        self.my_cursor.execute(
                                "INSERT INTO hospital (`name_of_table`, `ref`, `dose`, `no_of_tablets`, `lot`, `issuedate`, `exp_date`, `daily_dose`, `storage`, `nhs_number`, `p_name`, `dob`, `address`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                                (
                                        self.NameOfTable.get(),
                                        self.Ref.get(),
                                        self.Dose.get(),
                                        self.NoofTablets.get(),
                                        self.Lot.get(),
                                        self.Issuedate.get(),
                                        self.ExpDate.get(),
                                        self.DailyDose.get(),
                                        self.Storage.get(),
                                        self.NHSNumber.get(),
                                        self.Pname.get(),
                                        self.Dob.get(),
                                        self.Address.get(),
                                ))
                        self.conn.commit()
                        self.fetch_data()
                        messagebox.showinfo('Success', 'insert successful.')

# ========================> FETCH DATA <========================

        def get_cursor(self, event=""):
                cursor_row = self.hospital_table.focus()
                content = self.hospital_table.item(cursor_row)
                row = content['values']
                self.row_id.set(row[0])
                self.NameOfTable.set(row[1])
                self.Ref.set(row[2])
                self.Dose.set(row[3])
                self.NoofTablets.set(row[4])
                self.Lot.set(row[5])
                self.Issuedate.set(row[6])
                self.ExpDate.set(row[7])
                self.DailyDose.set(row[8])
                self.Storage.set(row[9])
                self.NHSNumber.set(row[10])
                self.Pname.set(row[11])
                self.Dob.set(row[12])
                self.Address.set(row[13])

        def update(self):
                self.conn=mysql.connector.connect(host="localhost", username="root", password="", database="hms_software")
                self.my_cursor = self.conn.cursor()
                self.my_cursor.execute(
                        "UPDATE `hospital` SET `name_of_table`=%s,`ref`=%s,`dose`=%s,`no_of_tablets`=%s,`lot`=%s,`issuedate`=%s,`exp_date`=%s,`daily_dose`=%s,`storage`=%s,`nhs_number`=%s,`p_name`=%s,`dob`=%s WHERE id=%s", 
                        (
                                self.NameOfTable.get(),
                                self.Ref.get(),
                                self.Dose.get(),
                                self.NoofTablets.get(),
                                self.Lot.get(),
                                self.Issuedate.get(),
                                self.ExpDate.get(),
                                self.DailyDose.get(),
                                self.Storage.get(),
                                self.NHSNumber.get(),
                                self.Pname.get(),
                                self.Dob.get(),
                                self.row_id.get(),
                        ))
                self.conn.commit()
                self.conn.close()
                self.fetch_data()
                messagebox.showinfo('Success', 'Update Successful.')
# =====================
        def clear(self):
                self.row_id.set('')
                self.NameOfTable.set('')
                self.Ref.set('')
                self.Dose.set('')
                self.NoofTablets.set('')
                self.Lot.set('')
                self.Issuedate.set('')
                self.ExpDate.set('')
                self.DailyDose.set('')
                self.Storage.set('')
                self.NHSNumber.set('')
                self.Pname.set('')
                self.Dob.set('')
                self.Address.set('')
        
        def delete(self):
                answer = askokcancel(
                        title='Confirmation',
                        message='Deleting will delete the data.',
                        icon=WARNING)
                if answer:
                        self.conn=mysql.connector.connect(host="localhost", username="root", password="", database="hms_software")
                        self.my_cursor = self.conn.cursor()
                        self.my_cursor.execute("DELETE FROM `hospital` WHERE id=%s", (self.row_id.get(),))
                        self.conn.commit()
                        self.conn.close()
                        self.clear()
                        self.fetch_data()

# ========================> FETCH DATA <========================

        def fetch_data(self):
                self.conn=mysql.connector.connect(host="localhost", username="root", password="", database="hms_software")
                self.my_cursor = self.conn.cursor()
                self.my_cursor.execute("SELECT * FROM hospital")
                rows = self.my_cursor.fetchall()
                self.conn.commit()
                self.conn.close()
                if len(rows) != 0:
                        self.hospital_table.delete(*self.hospital_table.get_children())
                        for i in rows:
                                self.hospital_table.insert("",END, values=i)
        
        def window_exit(self):
                answer = askokcancel(
                        title='Confirmation',
                        message='Deleting will delete the data.',
                        icon=WARNING)
                if answer:
                      root.destroy()  
                      return

root = Tk()
ob=Hospital(root)
root.mainloop()