from tkinter import Tk, ttk
from tkinter.constants import CENTER, NO





root = Tk()
root.geometry('600x400')
root.title('Tree View')

student_tree = ttk.Treeview(root)
student_tree['columns'] = ("Name", "Roll", "Phone")

student_tree.column('#0', width=0, stretch=NO)
student_tree.column('Name')
student_tree.column('Roll')
student_tree.column('Phone')

student_tree.heading('Name', text="Name", anchor=CENTER)
student_tree.heading('Roll', text="Roll", anchor=CENTER)
student_tree.heading('Phone', text="Phone", anchor=CENTER)

student_tree.insert(parent='', index=0, iid=0, text='', values=('1','Vineet','Alpha'))
student_tree.insert(parent='', index=1, iid=1, text='', values=('2','Anil','Bravo'))
student_tree.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'))
student_tree.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
student_tree.insert(parent='', index=4, iid=4, text='', values=('5','Manjeet','Echo'))

student_tree.pack()


root.mainloop()



# global hospital_table
                # self.my_cursor.execute("SELECT * FROM hospital")
                # rows = self.my_cursor.fetchall()
                # if len(rows) != 0:
                        # self.hospital_table.delete(*self.hospital_table.get_children())
                        # self.hospital_table.delete(*self.hospital_table.get_children())
                # for i in rows:
                # self.hospital_table.insert(parent='', index=0, iid=0, text='', values=("NameOfTable", 
                #                 "Ref", 
                #                 "Dose", 
                #                 "NoofTablets", 
                #                 "Lot", 
                #                 "Issuedate", 
                #                 "ExpDate", 
                #                 "DailyDose", 
                #                 "Storage", 
                #                 "NHSNumber", 
                #                 "Pname", 
                #                 "Dob", 
                #                 "Address"
                #                 ))
                        # self.conn.commit()
                # self.conn.close()