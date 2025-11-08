from tkinter import *
root = Tk()
root.geometry("600x800")
root.configure(bg="Blue")

def get_Kilograms():
    Grams = int(grams.get())
    Kilograms_result = Grams/1000
    Kilograms.config(text="the weight in kilograms is " + str(Kilograms_result))

label1 = Label(root,text="Grams to Kilograms converter",font=("Comic Sans",26))
label1.place(x=20,y=50)
label2 = Label(root,text="Please enter the weight of the object in grams")
label2.place(x=25,y=200)
label3 = Label(root,text="The kilograms is...")
label3.place(x=25,y=250)

grams = Entry(root,width=30)
grams.place(x=300,y=200)
Kilograms = Label(root)
Kilograms.place(x=200,y=250)

button1 = Button(root,text="Convert",command=get_Kilograms)
button1.place(x=275,y=300)

def get_grams():
    kilograms = int(Kilograms_2.get())
    grams_result = kilograms * 1000
    grams_2.config(text="the weight in grams is " + str(grams_result))

label4 = Label(root,text="Kilograms to grams converter",font=("Comic Sans",26))
label4.place(x=20,y=350)
label5 = Label(root,text="Please enter the weight of the object in Kilograms")
label5.place(x=25,y=500)
label6 = Label(root,text="The grams is...")
label6.place(x=25,y=550)

Kilograms_2 = Entry(root,width=30)
Kilograms_2.place(x=300,y=500)
grams_2 = Label(root)
grams_2.place(x=200,y=550)

button2 = Button(root,text="Convert",command=get_grams)
button2.place(x=275,y=700)





root.mainloop()


