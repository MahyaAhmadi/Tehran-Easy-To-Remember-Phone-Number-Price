from tkinter import messagebox
from tkinter import*
import os
import sys
import pickle
import numpy as np

module_path = os.path.abspath(os.path.join('.\\FeatureConstructor '))
if module_path not in sys.path:
    sys.path.append(module_path)

import FeatureConstructor as pn
mlp_reg = pickle.load(open('phoneNumberPredict_model.sav', 'rb'))
def get_args():
    global ticker, start_date, end_date, basics

    ticker = phonenumber.get()
    
    predictPrice(phonenumber)


def predictPrice(phoneNumber):
    try:
    #if phonenumber[0:4]=='0912'and len(phonenumber)==11:
            phoneNumber = str(phonenumber.get())
            featureDict, featureVector = pn.RoundFeatures(phoneNumber)
            #phoneNumber.set(featureDict,np.exp(mlp_reg.predict(featureVector.reshape(1,139))))
            #return featureDict, np.exp(mlp_reg.predict(featureVector.reshape(1,139)))
            p=np.exp(mlp_reg.predict(featureVector.reshape(1,139)))
            label1.config(text=list(featureDict.keys()))
            phoneNumber_label.config(text=p) 
            root.bind('<Configure>', lambda e: label1.config(wraplength=label1.winfo_width()))
    #else:
            #messagebox.showerror("SIM card pricing","Invalid Entry! Enter 11 numbers & only 0912!")  
    except Exception as error:
        print(error)
        messagebox.showerror("SIM card pricing","Invalid Entry! Enter 11 numbers & only 0912!")     

root=Tk()
root.title("SIM card pricing") 
root.geometry("900x500+300+200")   #abad pangere va nesbat safhe namayesh be on
root.resizable(False,False)
#search box
search_image = PhotoImage(file=".\\search.png")
search_image_label = Label(root,image=search_image)
search_image_label.pack(pady=20,side=TOP)
phonenumber = Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",fg="white",border=0)
phonenumber.place(x=280,y=40)
search_icon = PhotoImage(file=".\\search_icon.png")
search_icon_button = Button(root,image=search_icon,border=0,cursor="hand2",bg="#404040", text='Enter Number',command=get_args)
search_icon_button.place(x=590,y=34)
#logo
logo_image = PhotoImage(file=".\\download.png")
logo_label = Label(root,image=logo_image)
logo_label.pack(side=TOP)
#box 
box_image = PhotoImage(file=".\\box.png")
box_label = Label(root,image=box_image)
box_label.pack(pady=10,side=BOTTOM)
#price:
price_label=Label(root,text='predict price is:',font=("arial",15,"bold"),fg="#e355cd")
price_label.place(x=20,y=160)
phoneNumber_label=Label(root,font=("arial",15,'bold'),fg="#e355cd")
phoneNumber_label.place(x=70,y=250)
label1 = Label(root,font=("Helvetica",10,"bold"),fg="white",bg="#1ab5ef")
label1.place(x=100,y=400)
root.mainloop()   