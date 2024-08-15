import tkinter as tk

root = tk.Tk()
root.title("Alisveris Listesi")
root.geometry("300x200")

alisverisListesi = []


def sonuc():
    for i in range (20):
        girdi = enrty.get()
    alisverisListesi.append(girdi)
    resultLabel.config(text=f"Alışveriş Listesi : {alisverisListesi}, Toplam Eleman Sayısı : {len(alisverisListesi)}") 
   


label = tk.Label(root, text="Lütfen Liste Elemanlarını Giriniz")
label.pack()

resultLabel = tk.Label(root , text="")
resultLabel.pack()

enrty = tk.Entry(root)
enrty.pack()

button = tk.Button(root, text="Listeye Ekle", command=sonuc)
button.pack()

root.mainloop()
