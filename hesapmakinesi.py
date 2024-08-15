import tkinter as tk

root = tk.Tk()
root.title("ÇAkma Hesap Makinesi")
root.geometry("400x100")


def topla():
    try:
        deger1= float(entry1.get())
        deger2= float(entry2.get())
        sonuc = deger1 + deger2

        resultLabel.config(text =f"Sonuç : {sonuc}")
    except ValueError:
        resultLabel.config(text = "Düzgün değer giriniz")

def cikar():
    try:
        deger1= float(entry1.get())
        deger2= float(entry2.get())
        sonuc = deger1 - deger2

        resultLabel.config(text =f"Sonuç : {sonuc}")
    except ValueError:
        resultLabel.config(text = "Düzgün değer giriniz")
     
def carp():
    try:
        deger1= float(entry1.get())
        deger2= float(entry2.get())
        sonuc = deger1 * deger2

        resultLabel.config(text =f"Sonuç : {sonuc}")
    except ValueError:
        resultLabel.config(text = "Düzgün değer giriniz")
     
def bolme():
    try:
        deger1= float(entry1.get())
        deger2= float(entry2.get())
        sonuc = deger1 / deger2

        resultLabel.config(text =f"Sonuç : {sonuc}")
    except ValueError:
        resultLabel.config(text = "Düzgün değer giriniz")
    except ZeroDivisionError:
        resultLabel.config(text ="Sıfıra bölünme hatası") 
        

label = tk.Label(root, text="Lütfen 1. sayıyı giriniz")
label.grid(row=0,column=0)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Lütfen 2. sayıyı giriniz")
label2.grid(row=1,column=0)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

buttonTopla = tk.Button(root , text="Topla", command=topla, height=1, width=4)
buttonTopla.grid(row=0, column=5)

buttonCikar = tk.Button(root, text="Çıkar", command=cikar,height=1, width=4)
buttonCikar.grid(row=1, column=5)

buttonCarp = tk.Button(root, text="Çarp", command=carp,height=1, width=4)
buttonCarp.grid(row=0, column=6)

buttonBolme = tk.Button(root, text="Böl", command=bolme,height=1, width=4)
buttonBolme.grid(row=1, column=6)

resultLabel = tk.Label(root, text="")
resultLabel.grid(row=4, column=0, columnspan=1)


root.mainloop()