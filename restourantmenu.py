import tkinter as tk

root = tk.Tk()
root.title("Restourant Menü")
root.geometry("385x680")
root.configure(bg="#333333")


frame = tk.Frame(bg="#333333")

siparis = []
tostt = []
hamburgerr = []
kebapp = []
pizzaa = []
makarnaa = []
pogacaa = []
ayrann = []
limonataa = []
suu = []


def hesapla():

    toplam = sum(siparis)
    label.config(text=f" Toplam Hesap= {toplam} TL")

def temizle ():
    
    siparis.clear()
    toplam = sum(siparis)
    tostt.clear()
    hamburgerr.clear()
    kebapp.clear()
    pizzaa.clear()
    makarnaa.clear()
    pogacaa.clear()
    ayrann.clear()
    limonataa.clear()
    suu.clear()
    
    label9.config(text=f"{len(tostt)} adet Tost")
    label1.config(text=f"{len(hamburgerr)} adet Hamburger")
    label2.config(text=f"{len(kebapp)} adet Kebap")
    label3.config(text=f"{len(pizzaa)} adet Pizza")
    label4.config(text=f"{len(makarnaa)} adet Makarna")
    label5.config(text=f"{len(pogacaa)} adet Poğaça")
    label6.config(text=f"{len(ayrann)} adet Ayran")
    label7.config(text=f"{len(limonataa)} adet Limonata")
    label8.config(text=f"{len(suu)} adet Su")
    label.config(text=f" Toplam Hesap= {toplam} TL")
    





def tost():
    siparis.append(45)
    tostt.append("Tost")
    label9.config(text=f"{len(tostt)} adet Tost")

def hamburger():
    siparis.append(60)
    hamburgerr.append("Hamburger")
    label1.config(text=f"{len(hamburgerr)} adet Hamburger")

def kebap():
    siparis.append(100)
    kebapp.append("Kebap")
    label2.config(text=f"{len(kebapp)} adet Kebap")

def pizza():
    siparis.append(80)
    pizzaa.append("Pizza")
    label3.config(text=f"{len(pizzaa)} adet Pizza")

def makarna():
    siparis.append(70)
    makarnaa.append("Makarna")
    label4.config(text=f"{len(makarnaa)} adet Makarna")

def pogaca():
    siparis.append(20)
    pogacaa.append("Poğaça")
    label5.config(text=f"{len(pogacaa)} adet Poğaça")

def ayran():
    siparis.append(15)
    ayrann.append("Ayran")
    label6.config(text=f"{len(ayrann)} adet Ayran")

def limonata():
    siparis.append(20)
    limonataa.append("Limonata")
    label7.config(text=f"{len(limonataa)} adet Limonata")

def su():
    siparis.append(5)
    suu.append("Su")
    label8.config(text=f"{len(suu)} adet Su")


    
        
buttonHesapla = tk.Button(frame, text="Hesapla", command=hesapla,bg="gray",fg="yellow",cursor="hand2")
buttonHesapla.grid(row=250,column=1,padx=3,pady=10)

buttonTemizle = tk.Button(frame, text="Temizle", command=temizle,bg="gray",fg="yellow",cursor="hand2")
buttonTemizle.grid(row=250,column=3,padx=3,pady=10)

button1 = tk.Button(frame , text="Tost \n 45TL" , height=8, width=16, command=tost,bg="teal",fg="yellow",cursor="hand2")
button1.grid(row=0, column=1,padx=3,pady=3)

button2 = tk.Button(frame , text="Hamburger \n 60TL" , height=8, width=16,command=hamburger,bg="teal",fg="yellow",cursor="hand2")
button2.grid(row=0, column=2,padx=3,pady=3)

button3 = tk.Button(frame , text="Ciğer Kebap \n 100TL" , height=8, width=16,command=kebap,bg="teal",fg="yellow",cursor="hand2")
button3.grid(row=0, column=3,padx=3,pady=3)

button4 = tk.Button(frame , text="Pizza \n 80TL" , height=8, width=16, command=pizza,bg="teal",fg="yellow",cursor="hand2")
button4.grid(row=1, column=1,padx=3,pady=3)

button5 = tk.Button(frame , text="Makarna \n 70TL" , height=8, width=16, command=makarna,bg="teal",fg="yellow",cursor="hand2")
button5.grid(row=1, column=2,padx=3,pady=3)

button6 = tk.Button(frame , text="Poğaça \n 20TL" , height=8, width=16, command=pogaca,bg="teal",fg="yellow",cursor="hand2")
button6.grid(row=1, column=3,padx=3,pady=3)

button7 = tk.Button(frame , text="Ayran \n 15TL" , height=8, width=16, command=ayran,bg="teal",fg="yellow",cursor="hand2")
button7.grid(row=2, column=1,padx=3,pady=3)

button8 = tk.Button(frame , text="Limonata \n 20TL" , height=8, width=16,command=limonata,bg="teal",fg="yellow",cursor="hand2")
button8.grid(row=2, column=2,padx=3,pady=3)

button9 = tk.Button(frame , text="Su \n 5TL" , height=8, width=16, command=su,bg="teal",fg="yellow",cursor="hand2")
button9.grid(row=2, column=3,padx=3,pady=3)


label = tk.Label(frame, text="",bg="#333333",fg="yellow")
label.grid(row=210,column=2,columnspan=1)

label1 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label1.grid(row=201,column=2,columnspan=1)

label2 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label2.grid(row=202,column=2,columnspan=1)

label3 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label3.grid(row=203,column=2,columnspan=1)

label4 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label4.grid(row=204,column=2,columnspan=1)

label5 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label5.grid(row=205,column=2,columnspan=1)

label6 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label6.grid(row=206,column=2,columnspan=1)

label7 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label7.grid(row=207,column=2,columnspan=1)

label8 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label8.grid(row=208,column=2,columnspan=1)

label9 = tk.Label(frame, text="",bg="#333333",fg="yellow")
label9.grid(row=200,column=2,columnspan=1)

frame.pack()


root.mainloop()