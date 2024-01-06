from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import scrolledtext
from tkinter import messagebox
from mydb import Database
from myapi import API
# from sign_up import Signup



class Login:
    def __init__(self,root):
        self.dob=Database()
        self.api=API()
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
        
        Rigister1=Button(Right_frame,text="Login",width=10,font=("times new roman",15,"bold"),bg="green",fg="white",command=self.login)
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
        if email=='' or password=='':
             messagebox.showerror('Error',"Fill all Values")
             return 
        responce=self.dob.search(email,password)    
        if responce:
            messagebox.showinfo('Success',"Login Succesful")
            self.main()
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
        if email=='' or password=='' or name=='':
             messagebox.showerror('Error',"Fill all Values")
             return 
        
        if respons:
            messagebox.showinfo('Success',"Registration success")
            self.Login(root)
            
            
        else:
            messagebox.showerror('Error',"Email alredy exist")
    
    def main(self):
        # sentiment analysis
        # name entry recognition
        # emotion prediction
        self.clear()
        
        title_ibl=Label(self.root,text="Analysis",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(root,bd=2)
        main_frame.place(x=0,y=50,width=1600,height=1000)
        
        
        #-----------------------------------------left lable frame---------------------------------------------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=0,width=1460,height=680)
        
        
        
        # =============================Buttans===================
        
        Sentiment=Button(Left_frame,text="Sentiment analysis",width=30,font=("times new roman",25,"bold"),bg="orange",fg="white",command=self.Sentiment_analysis)
        Sentiment.place(x=100,y=100)
        
        Ner=Button(Left_frame,text="Name Entry Recognition",width=30,font=("times new roman",25,"bold"),bg="White",fg="black",command=self.NER_Def)
        Ner.place(x=420,y=250)
        
        Emotion=Button(Left_frame,text="Emotion prediction",width=30,font=("times new roman",25,"bold"),bg="green",fg="white",command=self.Emotion_def)
        Emotion.place(x=750,y=400)
        
        logout=Button(Left_frame,text="logout",width=70,font=("times new roman",25,"bold"),bg="red",fg="white",command=self.logout)
        logout.place(x=20,y=550)
        
        
    def Sentiment_analysis(self):
        self.clear()
        title_ibl=Label(self.root,text="Sentiment Analysis",font=("times new roman",30,"bold"),bg="white",fg="red")
        title_ibl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(root,bd=2)
        main_frame.place(x=0,y=50,width=1600,height=1000)
        
        
        #-----------------------------------------left lable frame---------------------------------------------------------------
        Left_frame=LabelFrame(main_frame,bd=2,bg="light yellow",relief=RIDGE,font=("times new roman",12,"bold"))
        Left_frame.place(x=20,y=0,width=1460,height=680)
        
        
        
        # =============================RIGHT LABLE FRAME===================
     
        # labeles=Label(Left_frame,text="Sentiment Analysis",width=40,bg="light yellow",fg="green",font=("times new roman",25,"bold"))
        # labeles.pack(pady=10)
        
        # heading1=Label(Left_frame,text='Sentiment Analysis',bg='light Yellow',fg='green')
        # heading1.pack(pady=(50,10))
        # heading1.config(font=('verdana',34,'bold'))
        
        img=Image.open(r"C:\Users\theve\OneDrive\Desktop\git_projects\Sentiment_Analysis\resorces\logo.ico")
        img=img.resize((80,80))
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lb=Label(Left_frame,image=self.photoimg)
        f_lb.pack(pady=(30,10))
         
        
        self.labeli=Label(Left_frame,text="Enter Text",bg="light yellow")
        self.labeli.pack(pady=20)
        self.labeli.config(font=('verdana',34,'bold'))
        
        self.sentiment_input=Entry(Left_frame,width=100,bg='white',fg='red')
        self.sentiment_input.pack(pady=(20,20),ipady=20)
        
        sentiment_btn=Button(Left_frame,text="Analys",width=15,bg='red',fg='white',font=("times new roman",25,"bold"),command=self.do_sentiment)
        sentiment_btn.pack(pady=(30,30))
        
        
        self.result=Label(Left_frame,text="",bg='light yellow',fg='black')
        self.result.pack(pady=20)
        self.result.config(font=('verdana',16))
        
        goback=Button(Left_frame,text="Go Back",bg='green',fg='black',width=10,font=("times new roman",25,"bold"),command=self.main)
        goback.pack()
        
        
    def NER_Def(self):
        pass
        
        
    def Emotion_def(self):
        pass
    
    
    
    def logout(self):
        self.Login(self.root)  
        
    
    
    def do_sentiment(self):
        txt=self.sentiment_input.get()
        result=self.api.sentiment_analysis(txt)
        txt=""
        for i in result['sentiment']:
            txt=txt+i+" -> "+str(result['sentiment'][i])+'\n'
                
        self.result['text']=txt      
        
        
        
        
        

        




if __name__=="__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()
   
    