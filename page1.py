from tkinter import *
from PIL import Image, ImageTk
import customtkinter
from tkcalendar import Calendar

def more_info1():
    root.withdraw()
    new_file=Toplevel(root)
    new_file.title=('Page2')
    new_file.geometry('600x600')
    new_file.resizable(False, False)
    new_file.configure(bg='#FAF1E4')

    image=Image.open('img1.webp')
    img=ImageTk.PhotoImage(image)
    image_label=Label(new_file,image=img,width=350,height=150)
    image_label.image=img
    image_label.place(x=130,y=20)

    customtkinter.CTkLabel(new_file,text='Marque:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=200)
    customtkinter.CTkLabel(new_file,text='Mercedes c-class',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=200)
    customtkinter.CTkLabel(new_file,text='Modéle:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=230)
    customtkinter.CTkLabel(new_file,text='2021',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=230)
    customtkinter.CTkLabel(new_file,text='Prix:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=260)
    customtkinter.CTkLabel(new_file,text='2900DH for day',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=260)
    customtkinter.CTkLabel(new_file,text='pick-:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=290)
    customtkinter.CTkLabel(new_file,text='15/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=290)
    customtkinter.CTkLabel(new_file,text='Date de retour:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=320)
    customtkinter.CTkLabel(new_file,text='20/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=320)
    def next():
            new_file.withdraw()
            login=Toplevel(new_file)
            login.title('Page3')
            login.geometry('600x700')
            login.resizable(False, False)
            login.configure(bg='#FAF1E4')
            sing=Label(login,text="Sign in",font=('Arial', 25),bg='#DED0B6')
            sing.place(x=250,y=5)
            image_path="remove.png"
            img=Image.open(image_path)
            img=ImageTk.PhotoImage(img)
            image_label=Label(login,image=img,width=170,height=170,bg='#FAF1E4')
            image_label.image=img
            image_label.place(x=0,y=0)
            Label(login,text="Nom & Prénom:",font=('Arial', 10)).place(x=180,y=100)
            
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre nom et prénom",width=200)
            entry.place(x=280,y=100)
            Label(login,text="CNI:").place(x=180,y=150)
            entry = customtkinter.CTkEntry(login, placeholder_text="Carte Nationale d'Identité",width=200).place(x=280,y=150)
            Label(login,text="Num de Rib:").place(x=180,y=200)
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre numéro de téléphone",width=200).place(x=280,y=200)
            Label(login,text="N de telephone:").place(x=180,y=250)
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre numéro de compte",width=200).place(x=280,y=250)
            Label(login,text="Date de domande").place(x=80,y=320)
            Label(login,text="Date de retour:").place(x=400,y=320)
            
 
            # Add Calendar1
            cal = Calendar(login, selectmode = 'day',year = 2024, month = 1,day = 19)            
            cal.place(x=10,y=350)
                        
            def grad_date():
                date1.config(text = "Selected Date is: " + cal.get_date())
                        
            Button(login, text = "Get Date",command = grad_date).place(x=80,y=550)
                        
            date1 = Label(login, text = "")
            date1.place(x=40,y=600)
            # Add Calendar2
            cal2 = Calendar(login,day = 19,year = 2024, month = 1,selectmode = 'day')
            cal2.place(x=320,y=350)
            
            def grad_date():
                date2.config(text = "Selected Date is: " + cal2.get_date())
            
            Button(login, text = "Get Date",command = grad_date).place(x=420,y=550)
            
            date2 = Label(login, text = "")
            date2.place(x=380,y=600)
            def back1():
                login.destroy()  
                new_file.deiconify()  
            customtkinter.CTkButton(login,text="valider").place(x=450,y=630)
            customtkinter.CTkButton(login,text="back",command=back1).place(x=0,y=630)

    def back2():
        new_file.destroy()  
        root.deiconify() 
    bt1=customtkinter.CTkButton(new_file,text="Next",command=next)
    bt1.place(x=450,y=470)
    bt2=customtkinter.CTkButton(new_file,text="Back",command=back2)
    bt2.place(x=0,y=470)

def more_info2():
    root.withdraw()
    new_file=Toplevel(root)
    new_file.title=('Page2')
    new_file.geometry('600x600')
    new_file.resizable(False, False)
    new_file.configure(bg='#FAF1E4')

    image=Image.open('img2.jpeg')
    img=ImageTk.PhotoImage(image)
    image_label=Label(new_file,image=img,width=350,height=150)
    image_label.image=img
    image_label.place(x=130,y=20)

    customtkinter.CTkLabel(new_file,text='Marque:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=200)
    customtkinter.CTkLabel(new_file,text='clio 4 automatique',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=200)
    customtkinter.CTkLabel(new_file,text='Modéle:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=230)
    customtkinter.CTkLabel(new_file,text='2019',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=230)
    customtkinter.CTkLabel(new_file,text='Prix:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=260)
    customtkinter.CTkLabel(new_file,text='350DH for day',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=260)
    customtkinter.CTkLabel(new_file,text='pick-:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=290)
    customtkinter.CTkLabel(new_file,text='18/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=290)
    customtkinter.CTkLabel(new_file,text='Date de retour:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=320)
    customtkinter.CTkLabel(new_file,text='24/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=320)
    def next():
            new_file.withdraw()
            login=Toplevel(new_file)
            login.title('Page3')
            login.geometry('600x700')
            login.resizable(False, False)
            login.configure(bg='#FAF1E4')
            sing=Label(login,text="Sign in",font=('Arial', 25),bg='#DED0B6')
            sing.place(x=250,y=5)
            image_path="remove.png"
            img=Image.open(image_path)
            img=ImageTk.PhotoImage(img)
            image_label=Label(login,image=img,width=170,height=170,bg='#FAF1E4')
            image_label.image=img
            image_label.place(x=0,y=0)
            Label(login,text="Nom & Prénom:",font=('Arial', 10)).place(x=180,y=100)
            
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre nom et prénom",width=200)
            entry.place(x=280,y=100)
            Label(login,text="CNI:").place(x=180,y=150)
            entry = customtkinter.CTkEntry(login, placeholder_text="Carte Nationale d'Identité",width=200).place(x=280,y=150)
            Label(login,text="Num de Rib:").place(x=180,y=200)
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre numéro de téléphone",width=200).place(x=280,y=200)
            Label(login,text="N de telephone:").place(x=180,y=250)
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre numéro de compte",width=200).place(x=280,y=250)
            Label(login,text="Date de domande").place(x=80,y=320)
            Label(login,text="Date de retour:").place(x=400,y=320)
            
 
            # Add Calendar1
            cal = Calendar(login, selectmode = 'day',year = 2024, month = 1,day = 19)            
            cal.place(x=10,y=350)
                        
            def grad_date():
                date1.config(text = "Selected Date is: " + cal.get_date())
                        
            Button(login, text = "Get Date",command = grad_date).place(x=80,y=550)
                        
            date1 = Label(login, text = "")
            date1.place(x=40,y=600)
            # Add Calendar2
            cal2 = Calendar(login,day = 19,year = 2024, month = 1,selectmode = 'day')
            cal2.place(x=320,y=350)
            
            def grad_date():
                date2.config(text = "Selected Date is: " + cal2.get_date())
            
            Button(login, text = "Get Date",command = grad_date).place(x=420,y=550)
            
            date2 = Label(login, text = "")
            date2.place(x=380,y=600)
            def back1():
                login.destroy()  
                new_file.deiconify()  
            customtkinter.CTkButton(login,text="valider").place(x=450,y=630)
            customtkinter.CTkButton(login,text="back",command=back1).place(x=0,y=630)

    def back2():
        new_file.destroy()  
        root.deiconify()   
        
    bt1=customtkinter.CTkButton(new_file,text="Next",command=next)
    bt1.place(x=450,y=470)
    bt2=customtkinter.CTkButton(new_file,text="Back",command=back2)
    bt2.place(x=0,y=470)

def more_info3():
    root.withdraw()
    new_file=Toplevel(root)
    new_file.title=('Page2')
    new_file.geometry('600x600')
    new_file.resizable(False, False)
    new_file.configure(bg='#FAF1E4')

    image=Image.open('voi2.jpeg')
    img=ImageTk.PhotoImage(image)
    image_label=Label(new_file,image=img,width=350,height=150)
    image_label.image=img
    image_label.place(x=130,y=20)

    customtkinter.CTkLabel(new_file,text='Marque:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=200)
    customtkinter.CTkLabel(new_file,text='BMW X6',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=200)
    customtkinter.CTkLabel(new_file,text='Modéle:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=230)
    customtkinter.CTkLabel(new_file,text='2016',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=230)
    customtkinter.CTkLabel(new_file,text='Prix:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=260)
    customtkinter.CTkLabel(new_file,text='2700dhDH for day',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=260)
    customtkinter.CTkLabel(new_file,text='pick-:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=290)
    customtkinter.CTkLabel(new_file,text='10/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=290)
    customtkinter.CTkLabel(new_file,text='Date de retour:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=150,y=320)
    customtkinter.CTkLabel(new_file,text='17/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20).place(x=350,y=320)
    def next():
            new_file.withdraw()
            login=Toplevel(new_file)
            login.title('Page3')
            login.geometry('600x700')
            login.resizable(False, False)
            login.configure(bg='#FAF1E4')
            sing=Label(login,text="Sign in",font=('Arial', 25),bg='#DED0B6')
            sing.place(x=250,y=5)
            image_path="remove.png"
            img=Image.open(image_path)
            img=ImageTk.PhotoImage(img)
            image_label=Label(login,image=img,width=170,height=170,bg='#FAF1E4')
            image_label.image=img
            image_label.place(x=0,y=0)
            Label(login,text="Nom & Prénom:",font=('Arial', 10)).place(x=180,y=100)
            
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre nom et prénom",width=200)
            entry.place(x=280,y=100)
            Label(login,text="CNI:").place(x=180,y=150)
            entry = customtkinter.CTkEntry(login, placeholder_text="Carte Nationale d'Identité",width=200).place(x=280,y=150)
            Label(login,text="Num de Rib:").place(x=180,y=200)
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre numéro de téléphone",width=200).place(x=280,y=200)
            Label(login,text="N de telephone:").place(x=180,y=250)
            entry = customtkinter.CTkEntry(login, placeholder_text="Entrer votre numéro de compte",width=200).place(x=280,y=250)
            Label(login,text="Date de domande").place(x=80,y=320)
            Label(login,text="Date de retour:").place(x=400,y=320)
            
 
            # Add Calendar1
            cal = Calendar(login, selectmode = 'day',year = 2024, month = 1,day = 19)            
            cal.place(x=10,y=350)
                        
            def grad_date():
                date1.config(text = "Selected Date is: " + cal.get_date())
                        
            Button(login, text = "Get Date",command = grad_date).place(x=80,y=550)
                        
            date1 = Label(login, text = "")
            date1.place(x=40,y=600)
            # Add Calendar2
            cal2 = Calendar(login,day = 19,year = 2024, month = 1,selectmode = 'day')
            cal2.place(x=320,y=350)
            
            def grad_date():
                date2.config(text = "Selected Date is: " + cal2.get_date())
            
            Button(login, text = "Get Date",command = grad_date).place(x=420,y=550)
            
            date2 = Label(login, text = "")
            date2.place(x=380,y=600)
            def back1():
                login.destroy()  
                new_file.deiconify()  
            customtkinter.CTkButton(login,text="valider").place(x=450,y=630)
            customtkinter.CTkButton(login,text="back",command=back1).place(x=0,y=630)

    def back2():
        new_file.destroy()  
        root.deiconify() 
    bt1=customtkinter.CTkButton(new_file,text="Next",command=next)
    bt1.place(x=450,y=470)
    bt2=customtkinter.CTkButton(new_file,text="Back",command=back2)
    bt2.place(x=0,y=470)
    


root = Tk()
root.title('Page1')
root.geometry('600x700')
root.resizable(False,False)
root.configure(bg='#FAF1E4')


lab = customtkinter.CTkLabel(root, text='Cars', width=15, height=2, bg_color='#FAEED1',font=('Arial', 25))
lab.place(x=250)

image = Image.open('img1.webp')
img = ImageTk.PhotoImage(image)

image_label = Label(root, image=img, width=300, height=150)
image_label.image = img
image_label.place(x=120,y=30)
btn1=customtkinter.CTkButton(root, width=150,height=40,corner_radius=30, text='more information', command=more_info1)
btn1.place(x=370,y=190)


image = Image.open('img2.jpeg')
img = ImageTk.PhotoImage(image)

image_label = Label(root, image=img, width=350, height=150)
image_label.image = img
image_label.place(x=100,y=240)

btn2=customtkinter.CTkButton(root, width=150,height=40,corner_radius=30, text='more information', command=more_info2)
btn2.place(x=370,y=400)

image = Image.open('voi2.jpeg')
img = ImageTk.PhotoImage(image)

image_label = Label(root, image=img, width=350, height=150)
image_label.image = img
image_label.place(x=100,y=450)

btn3=customtkinter.CTkButton(root, width=170,height=40,corner_radius=30, text='more information', command=more_info3)
btn3.place(x=370,y=610)




root.mainloop()
