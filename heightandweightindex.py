import tkinter as tk 
from tkinter import messagebox


root = tk.Tk()
root.title("Vücut Kilo endeksi hesaplama")
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


def anasayfa ():

    for widget in root.winfo_children():
        widget.destroy()



    ad2Label = tk.Label(text="İsim")
    ad2Label.pack()    

    ad2Enter = tk.Entry()
    ad2Enter.pack()    

    soyad2Label = tk.Label(text="Soyisim")
    soyad2Label.pack()
    
    soyad2Enter = tk.Entry()
    soyad2Enter.pack()    

    boyLabel = tk.Label(text="Boy (m)")
    boyLabel.pack()
    
    boyEnter = tk.Entry()
    boyEnter.pack()       

    kiloLabel = tk.Label(text="Kilo")
    kiloLabel.pack()
    
    kiloEnter = tk.Entry()
    kiloEnter.pack()    

    def kaydet ():

        

        isim = ad2Enter.get()
        soyisim = soyad2Enter.get() 
        boy = float(boyEnter.get())
        kilo = int(kiloEnter.get())

        endeks = kilo / (boy * boy)

        bilgilendirmeLabel = tk.Label(text=f"{isim} {soyisim} adlı kişiye ait Boy-Kilo Endeksi Değeri : {endeks} ")
        bilgilendirmeLabel.pack()  

        sonucLabel2 = tk.Label(text="")
        sonucLabel2.pack()


        if endeks >= 40 :
            sonucLabel2.config(text="Aşırı Obezite")
            root.configure(bg="#860000")
        elif  30 <= endeks < 40:
            sonucLabel2.config(text="Obezite")
            root.configure(bg="#c26d22")
        elif  25 <= endeks < 30:
            sonucLabel2.config(text="Fazla Kilolu") 
            root.configure(bg="#fdf225") 
        elif  18.5 <= endeks < 25:
            sonucLabel2.config(text="Normal Ağırlık")
            root.configure(bg="#54ff24")
        else :   
            sonucLabel2.config(text="Zayıf")  
            root.configure(bg="#00ffea")     



        

    
    
    kaydetButton = tk.Button(text="Hesapla",command=kaydet)
    kaydetButton.pack()



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
      
