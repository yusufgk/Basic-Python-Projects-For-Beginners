import tkinter as tk 
from tkinter import messagebox


root = tk.Tk()
root.title("Çakma Atm")
root.geometry("500x500")
root.configure(bg="#333333")

dogrukullaniciAdi = "a"
dogrusifre = "a"


frame = tk.Frame(bg="#333333")


def girisyap ():

    kullaniciAdi = isimEnter.get()
    sifre= sifreEnter.get()

    if kullaniciAdi == dogrukullaniciAdi and sifre == dogrusifre:
        messagebox.showinfo(message="Giriş Başarılı")
        anasayfa()
    else:
        messagebox.showerror(message="Kullanıcı adı veya şifre yanlış")

bakiye = 5000

def anasayfa ():

   
     
    for widget in root.winfo_children():
        widget.destroy()

    islemlerLabel = tk.Label(text="İşlemler",font=1,pady=10,bg="#333333",fg="#ffffff")
    islemlerLabel.pack()
    def paracek ():
        global bakiye
        for widget in root.winfo_children():
            widget.destroy()
        cekisTutarLabel = tk.Label(text="Çekmek istediğiniz tutarı giriniz",bg="#333333",fg="#ffffff")
        cekisTutarLabel.pack()
        cekisTutarEntry = tk.Entry()
        cekisTutarEntry.pack()
        
        def cek ():
           
           global bakiye
           cekis = int(cekisTutarEntry.get())
           if cekis > bakiye:
                messagebox.showerror(message="Bakiye Yetersiz")
           else :
               messagebox.showinfo(message=f"{cekis} TL Hesabınızdan Çekildi")
               bakiye -= cekis

        def geridonus ():
            anasayfa()
                   
                   
               
        geridon = tk.Button(text="Geri Dön",command=geridonus)
        geridon.pack()
        cekbutton = tk.Button(text="Çek",command=cek)
        cekbutton.pack()
    paraCekButton = tk.Button(text="Para Çek",command=paracek)
    paraCekButton.pack()

    def paraYatir ():
        for widget in root.winfo_children():
            widget.destroy()
        yatirTutarLabel = tk.Label(text="Yatırmak istediğiniz tutarı giriniz",bg="#333333",fg="#ffffff")
        yatirTutarLabel.pack()
        yatirTutarEntry = tk.Entry()
        yatirTutarEntry.pack()

        def yatir ():
           global bakiye
           yatiris = int(yatirTutarEntry.get())
           messagebox.showinfo(message=f"{yatiris} TL Hesabınıza Yatırıldı")
           bakiye += yatiris

        def geridonus ():
            anasayfa()
                   
                   
               
        geridon = tk.Button(text="Geri Dön",command=geridonus)
        geridon.pack()
               
        yatirbutton = tk.Button(text="Yatir",command=yatir)
        yatirbutton.pack()
    paraYatırButton = tk.Button(text="Para Yatır",command=paraYatir)
    paraYatırButton.pack()

    def bakiyeSorgu ():
        for widget in root.winfo_children():
            widget.destroy()

        bakiyeTutarLabel = tk.Label(text=f"Güncel Bakiye : {bakiye} TL",bg="#333333",fg="#ffffff")
        bakiyeTutarLabel.pack()

        def geridonus ():
            anasayfa()
                   
                   
               
        geridon = tk.Button(text="Geri Dön",command=geridonus)
        geridon.pack()
        
    bakiyeButton = tk.Button(text="Bakiye sorgula",command=bakiyeSorgu)
    bakiyeButton.pack()

    def cikis ():
        root.destroy()
    cikisButton = tk.Button(text="Çıkış",command=cikis)
    cikisButton.pack()


def cikisButon():
    root.destroy()


girisbutton = tk.Button(frame, text="Giriş Yap",font=0.1,command=girisyap)
girisbutton.grid(row=2,column=1)

isimEnter = tk.Entry(frame)
isimEnter.grid(row=0,column=1)

sifreEnter = tk.Entry(frame,show="*")
sifreEnter.grid(row=1,column=1)

isimLabel = tk.Label(frame,text="Kullanıcı Adı :",padx=10,pady=5,font=0.1,bg="#333333",fg="#fffefe")
isimLabel.grid(row=0,column=0)

sifreLabel = tk.Label(frame,text="Şifre :",padx=10,pady=5,font=0.1,bg="#333333",fg="#fffefe")
sifreLabel.grid(row=1,column=0)

sonucLabel = tk.Label(frame,text="",padx=10,pady=5,font=0.1,bg="#333333",fg="#fffefe")
sonucLabel.grid(row=3,column=1)



frame.pack()
root.mainloop()  