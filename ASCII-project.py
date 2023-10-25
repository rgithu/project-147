from tkinter import *
root = Tk()
root.title("ASCII")
root.geometry("500x500")
root.configure(background="snow")

enter_word = Entry(root)
enter_word.place(relx=0.5 , rely=0.3 , anchor=CENTER)
label = Label(root,text="Name of ASCII ",bg="blue",fg="white")
label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2 = Label(root,text="Encrypted Value is : ",bg="blue",fg="white")
label2.place(relx=0.5,rely=0.7,anchor=CENTER)

def asciiconverter():
    input_word = enter_word.get()
    for letter in input_word:
        label["text"]+=str(ord(letter))+" "
        label2["text"]+=str(ord(letter))+" "
        
btn = Button(root,text="Display ASCII Value With Encrypted Code  ",command=asciiconverter,bg="red",fg="yellow")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
                

root.mainloop()
