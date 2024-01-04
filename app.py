from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import scrolledtext
from tkinter import messagebox
from mydb import Database
# from sign_up import Signup



class Login:
    def __init__(self,root):
        self.dob=Database()
        # self.signup=Signup(root)
        self.root=root
        self.root.geometry("1500x780")
        self.root.title("Login Page")
        self.root.iconbitmap(r"C:\Users\theve\OneDrive\Desktop\git_projects\Sentiment_Analysis\resorces\logo.ico")
        self.Login(root)
    def Login(self,root):   
        self.clear()     
        title_ibl=Label(self.root,text="Analysis",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(root,bd=2)
        main_frame.place(x=0,y=50,width=1600,height=1000)
        
        
        #-----------------------------------------left lable frame---------------------------------------------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="light green",relief=RIDGE,font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=0,width=1460,height=680)
        
        
        
        # =============================RIGHT LABLE FRAME===================
        Right_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,text="Sign in",font=("times new roman",12,"bold"))
        Right_frame.place(x=480,y=50,width=600,height=580)
        
        labeles=Label(Right_frame,text="Sign in",width=40,bg="light yellow",fg="green",font=("times new roman",25,"bold"))
        labeles.pack(pady=10)
        
        img=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Sentiment_Analysis\resorces\logo.ico")
        img=img.resize((40,40))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lb=Label(Right_frame,image=self.photoimg)
        f_lb.pack(pady=(10,10))
        
        
        labele=Label(Right_frame,text="Enter Email",width=40,bg="light yellow",font=("times new roman",25,"bold"))
        labele.pack(pady=10)
        
        self.email_input=Entry(Right_frame,width=50,font=("times new roman",15,"bold"))
        self.email_input.pack(pady=(5,10),ipady=4)
        
        labelp=Label(Right_frame,text="Enter Password",width=40,bg="light yellow",font=("times new roman",25,"bold"))
        labelp.pack(pady=10)
        
        self.password_input=Entry(Right_frame,width=50,font=("times new roman",15,"bold"))
        self.password_input.pack(pady=(5,5),ipady=4)
        
        login=Button(Right_frame,text="Sign in",width=20,font=("times new roman",20,"bold"),bg="red",fg="white",command=self.login)
        login.pack(pady=10)
        
        labelr=Label(Right_frame,text="Don't have account ",width=40,bg="light yellow",font=("times new roman",15,"bold"))
        labelr.place(x=-20,y=445)
        
        Rigister=Button(Right_frame,text="Rigister Now",width=10,font=("times new roman",15,"bold"),bg="green",fg="white",command=self.register)
        Rigister.place(x=325,y=440)
        
    def Sign_up(self,root):
        self.clear()
        
        title_ibl=Label(self.root,text="Analysis",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(root,bd=2)
        main_frame.place(x=0,y=50,width=1600,height=1000)
        
        
        #-----------------------------------------left lable frame---------------------------------------------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="light green",relief=RIDGE,font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=0,width=1460,height=680)
        
        
        
        # =============================RIGHT LABLE FRAME===================
        Right_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,text="Sign Up",font=("times new roman",12,"bold"))
        Right_frame.place(x=480,y=50,width=600,height=590)
        
        labeles=Label(Right_frame,text="Sign Up",width=30,bg="light yellow",fg="green",font=("times new roman",18,"bold"))
        labeles.pack(pady=10)
        
        img1=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Sentiment_Analysis\resorces\logo.ico")
        img1=img1.resize((40,40))
        self.photoimg=ImageTk.PhotoImage(img1)
        
        f_lb=Label(Right_frame,image=self.photoimg)
        f_lb.pack(pady=(5,5))
        
        
        labelen=Label(Right_frame,text="Enter Email",width=30,bg="light yellow",font=("times new roman",18,"bold"))
        labelen.pack(pady=10)
        
        self.name_input=Entry(Right_frame,width=50,font=("times new roman",15,"bold"))
        self.name_input.pack(pady=(5,10),ipady=4)
        
        labele=Label(Right_frame,text="Enter Email",width=30,bg="light yellow",font=("times new roman",18,"bold"))
        labele.pack(pady=10)
        
        self.email_input=Entry(Right_frame,width=50,font=("times new roman",15,"bold"))
        self.email_input.pack(pady=(5,10),ipady=4)
        
        labelp=Label(Right_frame,text="Enter Password",width=30,bg="light yellow",font=("times new roman",18,"bold"))
        labelp.pack(pady=10)
        
        self.password_input=Entry(Right_frame,width=50,font=("times new roman",15,"bold"))
        self.password_input.pack(pady=(5,5),ipady=4)
        
        rigester1=Button(Right_frame,text="Sign up",width=20,font=("times new roman",20,"bold"),bg="red",fg="white",command=self.register1)
        rigester1.pack(pady=10)
        
        labelr=Label(Right_frame,text="Alrady have a account ",width=40,bg="light yellow",font=("times new roman",15,"bold"))
        labelr.place(x=-20,y=500)
        
        Rigister1=Button(Right_frame,text="Login",width=10,font=("times new roman",15,"bold"),bg="green",fg="white",command=self.login1)
        Rigister1.place(x=325,y=500)
    # ===========================================
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    # ====================
    
    
    def login(self):
        # pass
        email=self.email_input.get()
        password=self.password_input.get()
        
        responce=self.dob.search(email,password)    
        if responce:
            messagebox.showinfo('Success',"Login Succesful")
            # self.Sign_up(root)
        else:
            messagebox.showerror('Error',"Envlid User")
    def login1(self):
        self.Login(root)
            
    def register(self):
        self.Sign_up(root)
        
    def register1(self):
        name=self.name_input.get()
        email=self.email_input.get()
        password=self.password_input.get()
        respons=self.dob.add_data(name,email,password)
        
        if respons:
            messagebox.showinfo('Success',"Registration success")
            self.Login(root)
            
        else:
            messagebox.showerror('Error',"Email alredy exist")
        
        
        
        
        
        
        

        




if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
   
    