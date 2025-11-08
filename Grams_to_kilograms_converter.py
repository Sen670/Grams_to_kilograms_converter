from tkinter import *
root = Tk()
root.geometry("600x600")
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

root.mainloop()
