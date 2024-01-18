from tkinter import *
from PIL import Image, ImageTk
import customtkinter


def more_info():
    print("More information button pressed")

def more_info():
    root.withdraw()
    new_file=Toplevel(root)
    new_file.title=('Page2')
    new_file.geometry('600x700')
    new_file.resizable(False, False)
    new_file.configure(bg='#FAF1E4')
    

    image=Image.open('img1.jpg')
    img=ImageTk.PhotoImage(image)
    image_label=Label(new_file,image=img,width=350,height=150)
    image_label.image=img
    image_label.place(x=100,y=70)
    test = customtkinter.CTkLabel(new_file,text='Choose a car:',font=('Helvetica',20),text_color='black',fg_color='#562B08',corner_radius=20)
    test.grid(row=80,column=30,sticky="ew")
    test = customtkinter.CTkLabel(new_file,text='Marque:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=150,y=260)
    test= customtkinter.CTkLabel(new_file,text='Ford Focus',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=350,y=260)
    test= customtkinter.CTkLabel(new_file,text='Modéle:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=150,y=290)
    test= customtkinter.CTkLabel(new_file,text='2023',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=350,y=290)
    test= customtkinter.CTkLabel(new_file,text='Prix:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=150,y=320)
    test= customtkinter.CTkLabel(new_file,text='450 DH',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=350,y=320)
    test= customtkinter.CTkLabel(new_file,text='pick-:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=150,y=350)
    test= customtkinter.CTkLabel(new_file,text='12/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=350,y=350)
    test= customtkinter.CTkLabel(new_file,text='Date de retour:',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=150,y=380)
    test= customtkinter.CTkLabel(new_file,text='20/01/2024',font=('Helvetica',20),text_color='white',fg_color='black',corner_radius=20)
    test.place(x=350,y=380)
    def next():
        new_file.withdraw()
        login=Toplevel(new_file)
        login.title('Page3')
        login.geometry('600x700')
        login.resizable(False, False)
        login.configure(bg='#607274')
        sing=Label(login,text="Sign in")
        sing.place(x=250,y=5)
        image=Image.open('log.jpg')
        img=ImageTk.PhotoImage(image)
        image_label=Label(login,image=img,width=100,height=100)
        image_label.image=img
        image_label.place(x=0,y=50)
        Label(login,text="Nom & Prénom:").place(x=180,y=100)
        Entry(login).place(x=280,y=100)
        Label(login,text="CNI:").place(x=180,y=150)
        Entry(login).place(x=280,y=150)
        Label(login,text="Num de Rib:").place(x=180,y=200)
        Entry(login).place(x=280,y=200)
        Label(login,text="N de telephone:").place(x=180,y=250)
        Entry(login).place(x=280,y=250)
        Label(login,text="Date dedomande").place(x=180,y=300)
        Entry(login).place(x=280,y=300)
        Label(login,text="Date de retour:").place(x=180,y=350)
        Entry(login).place(x=280,y=350)
        Button(login,text="valider").place(x=400,y=450)
    def back():
        new_file.destroy()  
        root.deiconify()   
        
    custom_button = customtkinter.CTkButton(new_file,width=10,height=40,corner_radius=30,fg_color="#562B08",text="Next",command=next)
    custom_button.place(x=500,y=450)
    custom_button = customtkinter.CTkButton(new_file,width=10,height=40,corner_radius=30,fg_color="#562B08",text="Back",command=back)
    custom_button.place(x=500,y=500)

    

root = Tk()
root.title('Page1')
root.geometry('600x700')
root.resizable(False,False)
root.configure(bg='#F6F4EB')

custom_button = customtkinter.CTkButton(root,width=150,height=50,corner_radius=30, fg_color="#562B08", text='CAR Rental App', command="CAR Rental App")
custom_button.place(x=250)

image = Image.open('img1.jpg')
img = ImageTk.PhotoImage(image)

image_label = Label(root, image=img,width=250, height=150)
image_label.image = img
image_label.place(x=0,y=50)

custom_button = customtkinter.CTkButton(root, width=150,height=50,corner_radius=30,fg_color="#9E6F21", text='more information', command=more_info)
custom_button.place(x=370, y=210)




image = Image.open('img2.jpg')
img = ImageTk.PhotoImage(image)

image_label = Label(root, image=img, width=250, height=150)
image_label.image = img
image_label.place(x=0,y=250)

custom_button = customtkinter.CTkButton(root, width=150,height=50,corner_radius=30,fg_color="#9E6F21", text='more information', command=more_info)
custom_button.place(x=370, y=410)



image = Image.open('img3.jpg')
img = ImageTk.PhotoImage(image)

image_label = Label(root, image=img, width=250, height=150)
image_label.image = img
image_label.place(x=0,y=450)

custom_button = customtkinter.CTkButton(root, width=150,height=50,corner_radius=30,fg_color="#9E6F21", text='more information', command=more_info)
custom_button.place(x=370, y=610)




root.mainloop()


