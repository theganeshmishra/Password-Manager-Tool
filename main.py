from tkinter import *
import random
import pickle
import pyperclip
from tkinter import messagebox


class Qr:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x400+200+50")
        self.root.title("Password Manager Tool")
        self.root.resizable(False, False)

        # header of the appplication
        title = Label(self.root, text="Password Manager", font=("Consolas", 30), bg='#111111', fg='#F7EFEF',
                      anchor="w").place(x=0, y=0, relwidth=1)

        # variables
        self.id = StringVar()
        self.password = StringVar()

        # details of the employee(frame 1)
        details_frame = Frame(self.root, bd=3, relief=RIDGE, bg='#111111')
        details_frame.place(x=40, y=70, width=600, height=300)
        details_title = Label(details_frame, text="Details", font=("Verdana", 20), bg='#F7EFEF', fg='#111111').place(
            x=0, y=0, relwidth=1)

        # labels for the employee
        id = Label(details_frame, text="User Name", font=("Verdana", 15, 'bold'), bg='#111111', fg='#F7EFEF',
                   anchor="w").place(x=0, y=45, relwidth=1)
        password = Label(details_frame, text="Master Password", font=("Verdana", 15, 'bold'), bg='#111111',
                         fg='#F7EFEF', anchor="w").place(x=0, y=90, relwidth=1)
        # entries for the employee
        txt_id = Entry(details_frame, textvariable=self.id, font=("Verdana", 15, 'bold'), bg='#F7EFEF',
                       fg='#111111').place(x=230, y=45)
        txt_name = Entry(details_frame, textvariable=self.password, font=("Verdana", 15, 'bold'), bg='#F7EFEF',
                         fg='#111111').place(x=230, y=90)

        # buttons
        generate_btn = Button(details_frame, command=self.login, text="Login", font=("Verdana", 14, 'bold'),
                              bg='#F7EFEF', fg='#111111').place(x=30, y=180, height=50, width=160)
        clear_btn = Button(details_frame, command=self.clear, text="Clear", font=("Verdana", 14, 'bold'), bg='#F7EFEF',
                           fg='#111111').place(x=230, y=180, height=50, width=160)
        createNew_btn = Button(details_frame, command=self.createNew, text="Create New", font=("Verdana", 14, 'bold'),
                               bg='#F7EFEF', fg='#111111').place(x=430, y=180, height=50, width=160)

        # labels for message
        self.msg = ""
        self.lbl_msg = Label(details_frame, text=self.msg, font=("Verdana", 14), bg='#111111')
        self.lbl_msg.place(x=0, y=240, relwidth=1)

    def clear(self):
        self.id.set('')
        self.password.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg, bg='#111111')

    def createNew(self):
        self.newWindow2 = Toplevel(self.root)
        self.newWindow2.title("Password Manager|created by Ganesh Mishra")
        self.newWindow2.geometry("700x400+200+50")
        self.newWindow2.resizable(False, False)

        # header of the appplication
        title = Label(self.newWindow2, text=" Password Manager", font=("Consolas", 30), bg='#111111', fg='#F7EFEF',
                      anchor="w").place(x=0, y=0, relwidth=1)

        # variables
        self.username = StringVar()
        self.msg = ""

        # details of the employee(frame 1)
        details_frame2 = Frame(self.newWindow2, bd=3, relief=RIDGE, bg='#111111')
        details_frame2.place(x=40, y=70, width=600, height=300)
        details_title2 = Label(details_frame2, text="Create new Password Manager", font=("Verdana", 20), bg='#F7EFEF',
                               fg='#111111').place(x=0, y=0, relwidth=1)

        # labels for the employee
        username = Label(details_frame2, text="User Name", font=("Verdana", 15, 'bold'), bg='#111111', fg='#F7EFEF',
                         anchor="w").place(x=0, y=45, relwidth=1)
        # entries for the employee
        txt_username = Entry(details_frame2, textvariable=self.username, font=("Verdana", 15, 'bold'), bg='#F7EFEF',
                             fg='#111111').place(x=230, y=45)

        # buttons
        generate_pass = Button(details_frame2, command=self.generatepass, text="Generate Master Password",
                               font=("Verdana", 14, 'bold'), bg='#F7EFEF', fg='#111111').place(x=200, y=180, height=50,
                                                                                               width=300)

        # labels for message

        self.lbl_msg2 = Label(details_frame2, text=self.password, font=("Verdana", 14), bg='#111111')
        self.lbl_msg2.place(x=0, y=240, relwidth=1)

    def generatepass(self):
        if self.username.get() != "":
            info = {}
            with open("info.getdata", "br") as readfile:
                info = pickle.load(readfile)
            chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!@#$%^&*()"
            code = ""
            for x in range(0, 8):
                p_c = random.choice(chars)
                code = code + p_c
            info[self.username.get()] = code
            with open("info.getdata", "bw") as writefile:
                pickle.dump(info, writefile)
            self.msg = code
            pyperclip.copy(code)
            messagebox.showinfo("message", "Password copied!!")
            self.lbl_msg2.config(text=self.msg, fg="green", bg='#F7EFEF')
            ####################################################
            datadict = {}
            with open("pass.getdata", "br") as rfile:
                datadict = pickle.load(rfile)
                # website=self.datakey.get()
            # websitepass=self.datavalue.get()
            data_key = self.username.get()
            datadict[data_key] = {"-": "-"}
            with open("pass.getdata", "bw") as wfile:
                pickle.dump(datadict, wfile)
            ####################################################
        else:
            self.msg = "All fields are required!!!"
            self.lbl_msg2.config(text=self.msg, fg="red", bg='#F7EFEF')

        # 8888888888888888888888888888888888888888888888888888888888888888888888888

    def addbtn(self):
        if self.datakey.get() != "" and self.datavalue.get() != "":
            datadict = {}
            with open("pass.getdata", "br") as rfile:
                datadict = pickle.load(rfile)
            website = self.datakey.get()
            websitepass = self.datavalue.get()
            data_key = key
            datadict[data_key][website] = websitepass
            with open("pass.getdata", "bw") as wfile:
                pickle.dump(datadict, wfile)
            messagebox.showinfo("message", "Data added sucessfully!!")
        else:
            messagebox.showerror("Error", "All fields are required")

    def updatebtn(self):
        if self.datakey.get() != "" and self.datavalue.get() != "":
            datadict = {}
            with open("pass.getdata", "br") as rfile:
                datadict = pickle.load(rfile)
            website = self.datakey.get()
            websitepass = self.datavalue.get()
            data_key = key
            if website in datadict[data_key]:
                datadict[data_key][website] = websitepass
                with open("pass.getdata", "bw") as wfile:
                    pickle.dump(datadict, wfile)
                messagebox.showinfo("message", "Data updated successfully!!")
            else:
                messagebox.showerror("Error", "no data found")

        else:
            messagebox.showerror("Error", "All fields are required")

    def deletebtn(self):
        if self.datakey.get() != "" and self.datavalue.get() != "":
            datadict = {}
            with open("pass.getdata", "br") as rfile:
                datadict = pickle.load(rfile)
            website = self.datakey.get()
            websitepass = self.datavalue.get()
            data_key = key
            if website in datadict[data_key]:
                del datadict[data_key][website]
                with open("pass.getdata", "bw") as wfile:
                    pickle.dump(datadict, wfile)
                messagebox.showinfo("message", "Data deleted successfully!!")
            else:
                messagebox.showerror("Error", "no data found")
        else:
            messagebox.showerror("Error", "All fields are required")

    def viewbtn(self):
        if self.datakey.get() != "":
            datadict = {}
            with open("pass.getdata", "br") as rfile:
                datadict = pickle.load(rfile)
            website = self.datakey.get()
            data_key = key
            if website in datadict[data_key]:
                value = datadict[data_key][website]
                pyperclip.copy(value)
                messagebox.showinfo("message", "password copied sucessfully")
            else:
                messagebox.showerror("Error", "no data found")
        else:
            messagebox.showwarning("warning", "Website name is required")

    key = ""

    def login(self):
        if self.id.get() == "" or self.password.get() == "":
            self.msg = "All fields are required!!!"
            self.lbl_msg.config(text=self.msg, fg="red", bg='#F7EFEF')
        elif self.id.get() != "" or self.password.get() != "":
            info = {}
            with open("info.getdata", "br") as readfile:
                info = pickle.load(readfile)
            user = self.id.get()
            pas = self.password.get()
            if user in info:
                if info[user] == pas:
                    # Toplevel object which will
                    # be treated as a new window
                    self.newWindow = Toplevel(self.root)

                    # sets the title of the
                    # Toplevel widget
                    self.newWindow.title("Password Manager|created by Ganesh Mishra")

                    # sets the geometry of toplevel
                    self.newWindow.geometry("700x400+200+50")
                    self.newWindow.resizable(False, False)

                    #######################################################################3
                    # details of the employee(frame 1)
                    details_frame3 = Frame(self.newWindow, bd=3, relief=RIDGE, bg='#111111')
                    details_frame3.place(x=40, y=40, width=600, height=330)
                    details_title = Label(details_frame3, text="Data", font=("Verdana", 20), bg='#F7EFEF',
                                          fg='#111111').place(x=0, y=0, relwidth=1)

                    # entries for the data
                    self.datakey = StringVar()
                    self.datavalue = StringVar()
                    data_key = Entry(details_frame3, textvariable=self.datakey, font=("Verdana", 12, 'bold'),
                                     bg='#F7EFEF', fg='#111111').place(x=230, y=80)
                    data_value = Entry(details_frame3, textvariable=self.datavalue, font=("Verdana", 12, 'bold'),
                                       bg='#F7EFEF', fg='#111111').place(x=230, y=160)

                    # labels

                    self.lbl_key = Label(details_frame3, text="website name ", font=("Verdana", 14), fg='#F7EFEF',
                                         bg='#111111').place(x=230, y=40)
                    self.lbl_value = Label(details_frame3, text="password", font=("Verdana", 14), fg='#F7EFEF',
                                           bg='#111111').place(x=230, y=120)

                    # buttons
                    add_btn = Button(details_frame3, command=self.addbtn, text="Add", font=("Verdana", 14, 'bold'),
                                     bg='#F7EFEF', fg='#111111').place(x=20, y=50, height=50, width=140)
                    update_btn = Button(details_frame3, command=self.updatebtn, text="Update",
                                        font=("Verdana", 14, 'bold'), bg='#F7EFEF', fg='#111111').place(x=20, y=110,
                                                                                                        height=50,
                                                                                                        width=140)
                    delete_btn = Button(details_frame3, command=self.deletebtn, text="Delete",
                                        font=("Verdana", 14, 'bold'), bg='#F7EFEF', fg='#111111').place(x=20, y=170,
                                                                                                        height=50,
                                                                                                        width=140)
                    view_btn = Button(details_frame3, command=self.viewbtn, text="View", font=("Verdana", 14, 'bold'),
                                      bg='#F7EFEF', fg='#111111').place(x=20, y=230, height=50, width=140)
                    ######################

                    # password generator code
                    # self.msg="Login sucessfull!!"
                    # self.lbl_msg.config(text=self.msg,fg='green',bg='#F7EFEF')
                    global key
                    key = self.id.get()
                    self.id.set('')
                    self.password.set('')
                    self.msg = ""
                    self.lbl_msg.config(text=self.msg, bg='#111111')
            else:
                self.msg = "Invalid data!!!"
                self.lbl_msg.config(text=self.msg, fg="red", bg='#F7EFEF')


root = Tk()
obj = Qr(root)
root.mainloop()
