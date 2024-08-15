import tkinter as tk
import random

app = tk.Tk()
app.title("Taş Kağıt Makas")
app.geometry("710x510")
app.configure(bg="#454545")

frame = tk.Frame(bg="#454545")


skor=0
def oyun(oyuncuSecimi):
    global skor
    secenekler = ["Taş","Kağıt","Makas"]
    pcSecimi = random.choice(secenekler)
    sonuc = str

    if oyuncuSecimi == pcSecimi:
        sonuc = "Berabere"
    elif (oyuncuSecimi == "Taş" and pcSecimi == "Makas") or \
         (oyuncuSecimi == "Kağıt" and pcSecimi == "Taş") or\
         (oyuncuSecimi == "Makas" and pcSecimi == "Kağıt"):
         sonuc = "Kazandınız"
         skor+=1
    else:
        sonuc="Kaybettiniz"
        skor-=1



    pcSecim.config(text=f"Bilgisayar Seçimi :{pcSecimi}")
    sonucLabel.config( text=f"Sonuç :{sonuc}")
    skorLabel.config( text=f"Skor :{str(skor)}")
        



pcSecim = tk.Label(frame , text="Bilgisayar Seçimi : ",font=("Arial0" , 15),bg="#454545",fg="yellow")
pcSecim.pack(pady=20)

sonucLabel = tk.Label(frame , text="Sonuç : ",font=("Arial0" , 15),bg="#454545",fg="yellow")
sonucLabel.pack(pady=20)

skorLabel = tk.Label(frame , text="Skor : ",font=("Arial0" , 15),bg="#454545",fg="yellow")
skorLabel.pack(pady=20)

secimLabel = tk.Label(frame , text="Sizin Seçiminiz : ",font=("Arial0" , 15),bg="#454545",fg="yellow")
secimLabel.pack(side=tk.LEFT,pady=20)

tasButton = tk.Button(frame , text="TAŞ",cursor="hand2",height=3,width=10,bg="Teal",fg="Yellow",font=1, command=lambda: oyun("Taş"))
tasButton.pack(side=tk.LEFT, pady=20,padx=20,)

kagitButton = tk.Button(frame , text="KAĞIT",cursor="hand2",height=3,bg="Teal",fg="Yellow",width=10,font=1,command=lambda: oyun("Kağıt"))
kagitButton.pack( side=tk.LEFT,pady=20,padx=20)

makasButton = tk.Button(frame , text="MAKAS",cursor="hand2",height=3,width=10,bg="Teal",fg="Yellow",font=1,command=lambda: oyun("Makas"))
makasButton.pack(side=tk.LEFT, pady=20,padx=20)

frame.pack()


app.mainloop()